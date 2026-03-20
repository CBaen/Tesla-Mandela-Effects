$file = 'C:\Users\baenb\Desktop\Tesla Mandela Effects\0. EPISODE FACTORY\EPISODES\003 - THE GOD PARTICLE\003-THE_GOD_PARTICLE-SCRIPT-v4.md'
$text = Get-Content $file -Raw
$words = ($text -split '\s+' | Where-Object { $_ -ne '' }).Count
$negations = [regex]::Matches($text, '\b(does not|is not|do not|did not|are not|was not|were not|have not|has not|had not|cannot|could not|would not|will not)\b', 'IgnoreCase').Count
$baseline = [regex]::Matches($text, '\bbaseline\b', 'IgnoreCase').Count
$something = [regex]::Matches($text, '\bsomething\b', 'IgnoreCase').Count
$you_count = [regex]::Matches($text, '\byou\b', 'IgnoreCase').Count
Write-Host "Words: $words"
Write-Host "Negations: $negations"
Write-Host "Baseline: $baseline"
Write-Host "Something: $something"
Write-Host "You: $you_count"
