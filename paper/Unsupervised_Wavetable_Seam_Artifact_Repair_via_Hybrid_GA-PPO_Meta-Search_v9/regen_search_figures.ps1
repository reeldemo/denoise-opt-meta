# Regenerate search-campaign learning curves + dataset distribution figures (run from anywhere)
$ErrorActionPreference = "Stop"
$Reel = "C:\Users\Julian\Documents\Programming\github\reeldemo\reelsynth"
$Meta = "C:\Users\Julian\Documents\Programming\github\reeldemo\denoise-opt-meta\paper\v7\figures"
$Py = Join-Path $Reel ".venv_gpu\Scripts\python.exe"
if (-not (Test-Path $Py)) { $Py = "python" }

# Dataset distribution histograms (holdout seed 20260719, n=4096)
& $Py (Join-Path $Reel "scripts\plot_dataset_statistics.py") --also-meta-v7

$Latest = Get-Content (Join-Path $Reel "brand\artifacts\overnight_gpu_rl_arch_latest.json") -Raw | ConvertFrom-Json
$Hist = Join-Path $Latest.run_dir "history.jsonl"
$Base = [string]$Latest.baseline_dual_cosine
$FreezeIter = 5000
& $Py (Join-Path $Reel "scripts\plot_overnight_history.py") $Hist --baseline $Base --max-iter $FreezeIter --out-dir $Meta --also-meta-v7
Write-Host "OK figures in $Meta (max_iter=$FreezeIter, latest iter=$($Latest.iter))"
