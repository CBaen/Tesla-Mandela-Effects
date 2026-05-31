param(
  [switch]$Force
)

$ErrorActionPreference = "Stop"

$Root = "C:\Users\baenb\Desktop\Tesla Mandela Effects"
$Delivery = Join-Path $Root "14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery"
New-Item -ItemType Directory -Force -Path $Delivery | Out-Null

$Jobs = @(
  @{
    Id = "S1E1-rumble-1440p"
    Input = Join-Path $Root "11. MASTER COMPOSITIONS\TESLA S1E1\Tesla 001 v2\Tesla 001 v2.mp4"
    Output = Join-Path $Delivery "TME-S1E1-rumble-1440p-h264.mp4"
    Width = 2560; Height = 1440; Bitrate = "12000k"; Maxrate = "16000k"; Bufsize = "32000k"; Cq = "20"; Level = "5.1"
  },
  @{
    Id = "S1E2-rumble-1440p"
    Input = Join-Path $Root "11. MASTER COMPOSITIONS\TESLA S1E2\S1E2 V2\TESLA S1E2 V2\TESLA S1E2 V2.mp4"
    Output = Join-Path $Delivery "TME-S1E2-rumble-1440p-h264.mp4"
    Width = 2560; Height = 1440; Bitrate = "12000k"; Maxrate = "16000k"; Bufsize = "32000k"; Cq = "20"; Level = "5.1"
  },
  @{
    Id = "S1E3-rumble-1440p"
    Input = Join-Path $Root "11. MASTER COMPOSITIONS\TESLA S1E3\TESLA S1E3 V3\TESLA S1E3\TESLA S1E3 v3.mp4"
    Output = Join-Path $Delivery "TME-S1E3-rumble-1440p-h264.mp4"
    Width = 2560; Height = 1440; Bitrate = "12000k"; Maxrate = "16000k"; Bufsize = "32000k"; Cq = "20"; Level = "5.1"
  },
  @{
    Id = "S1E1-spotify-1080p"
    Input = Join-Path $Root "11. MASTER COMPOSITIONS\TESLA S1E1\Tesla 001 v2\Tesla 001 v2.mp4"
    Output = Join-Path $Delivery "TME-S1E1-spotify-1080p-h264.mp4"
    Width = 1920; Height = 1080; Bitrate = "8000k"; Maxrate = "10000k"; Bufsize = "20000k"; Cq = "22"; Level = "4.2"
  },
  @{
    Id = "S1E2-spotify-1080p"
    Input = Join-Path $Root "11. MASTER COMPOSITIONS\TESLA S1E2\S1E2 V2\TESLA S1E2 V2\TESLA S1E2 V2.mp4"
    Output = Join-Path $Delivery "TME-S1E2-spotify-1080p-h264.mp4"
    Width = 1920; Height = 1080; Bitrate = "8000k"; Maxrate = "10000k"; Bufsize = "20000k"; Cq = "22"; Level = "4.2"
  },
  @{
    Id = "S1E3-spotify-1080p"
    Input = Join-Path $Root "11. MASTER COMPOSITIONS\TESLA S1E3\TESLA S1E3 V3\TESLA S1E3\TESLA S1E3 v3.mp4"
    Output = Join-Path $Delivery "TME-S1E3-spotify-1080p-h264.mp4"
    Width = 1920; Height = 1080; Bitrate = "8000k"; Maxrate = "10000k"; Bufsize = "20000k"; Cq = "22"; Level = "4.2"
  }
)

$StatusPath = Join-Path $Delivery "transcode-status.json"
$ManifestPath = Join-Path $Delivery "delivery-manifest.json"
$Results = @()

foreach ($Job in $Jobs) {
  if ((Test-Path -LiteralPath $Job.Output) -and -not $Force) {
    $Results += [pscustomobject]@{
      id = $Job.Id
      status = "skipped_existing"
      output = $Job.Output
    }
    $Results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $StatusPath -Encoding UTF8
    continue
  }

  if (-not (Test-Path -LiteralPath $Job.Input)) {
    throw "Missing source file for $($Job.Id): $($Job.Input)"
  }

  $LogPath = Join-Path $Delivery "$($Job.Id).ffmpeg.log"
  $Results += [pscustomobject]@{
    id = $Job.Id
    status = "running"
    output = $Job.Output
    started_at = (Get-Date).ToString("o")
  }
  $Results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $StatusPath -Encoding UTF8

  $Scale = "scale=$($Job.Width):$($Job.Height):flags=lanczos,format=yuv420p"
  $Args = @(
    "-y",
    "-hide_banner",
    "-loglevel", "warning",
    "-stats",
    "-i", $Job.Input,
    "-map", "0:v:0",
    "-map", "0:a:0",
    "-vf", $Scale,
    "-c:v", "h264_nvenc",
    "-preset", "p5",
    "-tune", "hq",
    "-profile:v", "high",
    "-level", $Job.Level,
    "-rc", "vbr",
    "-cq", $Job.Cq,
    "-b:v", $Job.Bitrate,
    "-maxrate", $Job.Maxrate,
    "-bufsize", $Job.Bufsize,
    "-r", "30",
    "-g", "30",
    "-keyint_min", "30",
    "-c:a", "aac",
    "-b:a", "320k",
    "-ac", "2",
    "-ar", "48000",
    "-movflags", "+faststart",
    $Job.Output
  )

  $PreviousErrorActionPreference = $ErrorActionPreference
  $ErrorActionPreference = "Continue"
  & ffmpeg @Args *> $LogPath
  $ErrorActionPreference = $PreviousErrorActionPreference
  if ($LASTEXITCODE -ne 0) {
    throw "ffmpeg failed for $($Job.Id). See $LogPath"
  }

  $Probe = ffprobe -v error -show_entries format=duration,size,bit_rate -show_entries stream=codec_name,width,height,sample_rate,channels -of json $Job.Output | ConvertFrom-Json
  $Results = @($Results | Where-Object { $_.id -ne $Job.Id })
  $Results += [pscustomobject]@{
    id = $Job.Id
    status = "complete"
    output = $Job.Output
    duration_sec = [math]::Round([double]$Probe.format.duration, 2)
    size_bytes = [int64]$Probe.format.size
    codec_video = ($Probe.streams | Where-Object { $_.width } | Select-Object -First 1).codec_name
    width = ($Probe.streams | Where-Object { $_.width } | Select-Object -First 1).width
    height = ($Probe.streams | Where-Object { $_.height } | Select-Object -First 1).height
    codec_audio = ($Probe.streams | Where-Object { $_.sample_rate } | Select-Object -First 1).codec_name
    completed_at = (Get-Date).ToString("o")
  }
  $Results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $StatusPath -Encoding UTF8
}

$Results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $ManifestPath -Encoding UTF8
