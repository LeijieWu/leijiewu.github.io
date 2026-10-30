"""Local content preview, intentionally distinct from a full Jekyll build."""
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
import argparse
import html
import re
import yaml
from markdown_it import MarkdownIt
from export_full_cv import cv_html, records

ROOT = Path(__file__).resolve().parents[1]
MD = MarkdownIt('commonmark', {'html': True}).enable('table')
STYLE = '''
*{box-sizing:border-box}body{margin:0;background:#fff;color:#263238;font:16px/1.65 Arial,sans-serif}
header{border-bottom:1px solid #dae1e4;padding:18px max(24px,calc((100% - 1140px)/2));background:#f5f8f9}
nav{display:flex;gap:24px;flex-wrap:wrap}a{color:#237d95;text-decoration:none}a:hover{text-decoration:underline}
.notice{background:#fff6dd;padding:10px 24px;font-size:13px;color:#574b2b}
.shell{max-width:1140px;margin:36px auto;display:grid;grid-template-columns:210px 1fr;gap:48px;padding:0 24px}
aside{font-size:14px}aside h2{color:#263238;font-size:20px}main{min-width:0}h1{font-size:30px;line-height:1.2}main h2{margin-top:36px;color:#1e6475;font-size:23px}main h3{margin-top:26px;font-size:19px}
li{margin:7px 0}table{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0}td,th{padding:9px;border:1px solid #d3dde1;text-align:left}th{background:#eef3f5}img{max-width:100%}
.links{display:flex;gap:18px;margin:20px 0}footer{margin-top:36px;border-top:1px solid #ddd;padding:16px 0;font-size:13px;color:#607078}
@media(max-width:720px){.shell{grid-template-columns:1fr;gap:12px;margin-top:20px}aside{display:none}body{font-size:15px}nav{gap:18px}h1{font-size:27px}}
@media print{header,aside,.notice,.links{display:none}.shell{display:block;margin:0}body{font-size:10pt}h1,h2,h3{break-after:avoid}li{break-inside:avoid}}
'''

def markdown_page(path):
    text = (ROOT / path).read_text(encoding='utf-8')
    _, front, body = text.split('---', 2)
    meta = yaml.safe_load(front)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    body = re.sub(r"\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*\}\}", r'\1', body)
    return meta['title'], MD.render(body)

def render(path):
    cfg = yaml.safe_load((ROOT/'_config.yml').read_text(encoding='utf-8'))
    if path == '/':
        title, content = markdown_page('_pages/about.md')
    elif path == '/research/':
        title, content = markdown_page('_pages/research.md')
    elif path in ('/cv/', '/cv/print/'):
        title = 'Curriculum Vitae'
        content = '<div class="links"><a href="/files/Leijie_Wu_Full_CV.pdf">Download CV PDF</a><a href="/research/">Detailed research portfolio</a></div>'+cv_html()
    elif path == '/publications/':
        title = 'Publications'
        content = ''.join('<p>'+r['citation']+' <a href="'+r['paperurl']+'">[Paper]</a></p>' for r in records('_publications'))
    elif path == '/talks/':
        title='Talks'
        content=''.join('<h2>'+html.escape(r['title'])+'</h2><p>'+html.escape(r['type']+' | '+str(r['date']))+'</p>' for r in records('_talks'))
    else:
        raise KeyError(path)
    nav=''.join('<a href="'+url+'">'+label+'</a>' for label,url in [('Home','/'),('Research','/research/'),('CV','/cv/'),('Publications','/publications/'),('Talks','/talks/')])
    author=cfg['author']
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+' | Local Preview</title><style>'+STYLE+'</style></head><body><div class="notice">Local content preview. Full Jekyll theme and plugins are verified on the deployed site. Refresh after editing source files.</div><header><nav>'+nav+'</nav></header><div class="shell"><aside><h2>'+html.escape(author['name'])+'</h2><p>Research Scientist<br>Huawei Hong Kong Research Center</p><a href="mailto:'+author['email']+'">'+author['email']+'</a></aside><main><h1>'+html.escape(title)+'</h1>'+content+'<footer>Leijie Wu · Personal research portfolio and academic CV</footer></main></div></body></html>'

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path=urlsplit(self.path).path
        if path=='/files/Leijie_Wu_Full_CV.pdf':
            data=(ROOT/'files/Leijie_Wu_Full_CV.pdf').read_bytes(); content_type='application/pdf'
        else:
            try: data=render(path).encode('utf-8');content_type='text/html; charset=utf-8'
            except KeyError:self.send_error(404,'This route is not part of the content preview');return
        self.send_response(200);self.send_header('Content-Type',content_type);self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--port',type=int,default=4000);args=parser.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    print(f'Content preview: http://127.0.0.1:{args.port}/ (Ctrl+C to stop)',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
