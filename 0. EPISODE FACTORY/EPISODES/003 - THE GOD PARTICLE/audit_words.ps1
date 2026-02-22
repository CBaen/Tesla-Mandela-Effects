$f = 'C:\Users\baenb\Desktop\Tesla Mandela Effects\0. EPISODE FACTORY\EPISODES\003 - THE GOD PARTICLE\003-THE_GOD_PARTICLE-SCRIPT.md'
$c = Get-Content $f -Raw

$words = @('something', 'felt', 'watched', 'silence', 'version', 'memory', 'memories', 'pattern', 'change', 'detail', 'detail', 'frequency', 'resonan', 'body', 'wound', 'scar', 'baseline', 'reality', 'evidence')
foreach ($w in $words) {
    $n = ([regex]::Matches($c, $w, 'IgnoreCase')).Count
    Write-Output "$w : $n"
}

Write-Output "---"
$paras = ($c -split '\r?\n\r?\n' | Where-Object { $_.Trim() -ne '' })
Write-Output "Paragraph count: $($paras.Count)"

Write-Output "---"
$asif = ([regex]::Matches($c, 'as if', 'IgnoreCase')).Count
Write-Output "as if : $asif"
