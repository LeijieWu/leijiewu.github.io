$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$inputFile = Join-Path $repoRoot 'Full_CV.docx'
$outputFile = Join-Path $repoRoot 'files/Leijie_Wu_Full_CV.pdf'
$inputFile = [System.IO.Path]::GetFullPath($inputFile).Replace([char]92, [char]47)
$outputFile = [System.IO.Path]::GetFullPath($outputFile).Replace([char]92, [char]47)
if (-not (Test-Path -LiteralPath $inputFile)) { throw 'Run scripts/export_full_cv.py first.' }
$temporaryDirectory = Join-Path $repoRoot 'local/cv_export'
New-Item -ItemType Directory -Path $temporaryDirectory -Force | Out-Null
$temporaryPdf = (Join-Path $temporaryDirectory ([Guid]::NewGuid().ToString() + '.pdf')).Replace([char]92, [char]47)
$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.Options.SaveNormalPrompt = $false
    $word.AutomationSecurity = 3
    $document = $word.Documents.Open($inputFile, $false, $true, $false)
    $document.ExportAsFixedFormat($temporaryPdf, 17)
} finally {
    if ($document -ne $null) { $document.Close(0); [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($document) }
    if ($word -ne $null) { $word.Quit(); [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
}
Copy-Item -LiteralPath $temporaryPdf -Destination $outputFile -Force
if ((Get-FileHash -LiteralPath $temporaryPdf).Hash -ne (Get-FileHash -LiteralPath $outputFile).Hash) { throw 'PDF verification failed.' }
Remove-Item -LiteralPath $temporaryPdf
Write-Output ('Exported ' + $outputFile)
