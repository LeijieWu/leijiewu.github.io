# 个人资料库与岗位 CV 维护

## 三层结构

1. **主页** _pages/about.md：身份、研究主线、少量新闻和导航。
2. **通用学术 CV** _includes/cv-content.md：学历、职位、三项代表性华为贡献、完整论文、教学、指导和服务，供 /cv/ 和 /cv/print/ 共用。
3. **研究资料库** _pages/research.md，网址 /research/：R1-R7 的问题、贡献、状态、评测范围和方向标签。详细资料长期维护在此，申请时按需选择。

通用 CV 不再重复放完整成果报告。Full_CV.docx 和下载 PDF 保留原文件名以兼容入口，其内容是通用学术 CV，不是资料库全文。

## 按岗位取材

| 岗位重点 | 优先素材 | 取舍建议 |
| --- | --- | --- |
| 泛 AI / 教学与科研并重的 AP | R7、R3、R4，加教学指导 | 华为经历保留 2-3 项代表贡献，论文与教学为主体 |
| LLM / AI Systems | R1、R2 | 保留模型、硬件、基线；区分 prefill、output 与端到端指标 |
| Agent / RAG / NLP | R3、R4、R5 | 强调检索、记忆和知识更新；prototype 与论文分开 |
| 软件工程 / Coding Agent | R6、R4 | 强调 repository-level reasoning，保留基线限定 |
| 可信 / 分布式 AI | R7、R1、R5 | 串联 privacy、unlearning、资源约束和可靠性 |
| 多模态与应用研究 | R2 的视觉应用、R4 | 写真实交集，不扩展成没有证据的专业方向 |

先读 JD，选 2-3 个匹配项目，再调整排序和一两条有上下文的指标。岗位版本另存申请目录，通用导出脚本不会覆盖 SFU 版本。

## 本地预览

本机不需要安装 Ruby 即可进行内容预览，在 PowerShell 运行：

    cd D:/Personal_Project/leijiewu.github.io
    & 'D:/miniconda3/envs/lawagent/python.exe' -X utf8 scripts/preview_site.py

打开 http://127.0.0.1:4000/，研究页 /research/，CV /cv/。按 Ctrl+C 停止，编辑后刷新即可。工具明确标注为内容预览，只提供生成页面与 CV PDF，不开放整个仓库目录；正式主题与插件效果以上线版为准。

完整 Jekyll 预览需安装 Ruby 与 Bundler 后运行：

    bundle install
    bundle exec jekyll serve --host 127.0.0.1 --port 4000

不要同时在 4000 端口启动两种预览。当前本机未检测到 Ruby/Bundler，Python 内容预览可直接使用。

## Export and source details

This repository holds the general academic profile and full CV. The tailored SFU application lives separately in D:/Personal_Project/SFU_CIS_AP.

## Sources of truth

- _pages/about.md: homepage introduction and research translation summary.
- _includes/cv-content.md: general academic CV with selected contributions, publications, teaching, mentoring and service. Both /cv/ and /cv/print/ include this file.
- _pages/research.md: detailed project portfolio with evaluation context and status, separate from the CV.
- _publications/*.md: publication records and citations, shared by the publication page and CV exports. File dates and permalinks retain their original early-access chronology; final issue details appear in citations.
- _talks/*.md: conference presentations.
- _config.yml: contact details and website description.

## Generated files

- Full_CV.docx: editable full CV generated from the shared sources.
- files/Leijie_Wu_Full_CV.pdf: downloadable full CV, linked from both CV pages.

Regenerate the DOCX with:

    python scripts/export_full_cv.py

Dependencies: python-docx, PyYAML, markdown-it-py and beautifulsoup4. On this workstation the existing Python environment is D:/miniconda3/envs/lawagent/python.exe.

On Windows with Microsoft Word installed, regenerate the PDF with:

    powershell -NoProfile -File scripts/export_full_cv_pdf.ps1

Review every PDF page after changes, check hyperlinks and page breaks, and commit the updated source and generated files together. The export scripts do not commit or publish the repository.

## Source reconciliation

The original Full_CV.docx is preserved under local/cv_archive/ before the first regenerated export. The current website is the main source for personal facts. Differences in EPFL and Dahua month ranges remain in the original materials; no new month dates are inferred by the exporter. Historical items unique to the old Word file are retained in that archive rather than silently treated as current research or teaching claims.

Journal issue details were verified on 2026-10-30 when preparing the SFU CV and are now synchronized to the shared publication records. L4L uses its 2022 issue; Long-Term Adaptive VCG uses its 2024 issue. The incentive-mechanism survey explicitly identifies its 2021 early-access record.

The technology-transfer summary is based on huawei_transfer.md. Quantitative claims retain their internal-evaluation scope and relevant model/hardware/baseline information. The original note is now both Git-ignored and excluded from Jekyll; it remains on this workstation. Local working files are also Git-ignored. Export scripts, this guide and the editable DOCX are stored in the repository but excluded from Jekyll output. Jekyll exclusions alone do not prevent a file from being committed to Git.
