<#
.SYNOPSIS
  Run one cold full-data monolithic manuscript case from the repository root.
.EXAMPLE
  .\scripts\run_monolithic_manuscript.ps1 -CaseName S03_R
.EXAMPLE
  .\scripts\run_monolithic_manuscript.ps1 -CaseName S03_speed10 -NodeFileDir 'D:\local_scratch\gurobi_monolithic_nodefiles'
#>
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet(
        'S01_NR', 'S01_R', 'S02_NR', 'S02_R', 'S03_NR', 'S03_R',
        'S03_speed10', 'S03_speed20', 'S03_speed40',
        'S03_vot50', 'S03_vot100', 'S03_dist1p2', 'S03_dist2p0'
    )]
    [string]$CaseName,
    [string]$NodeFileDir = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if ([string]::IsNullOrWhiteSpace($NodeFileDir)) {
    $NodeFileDir = Join-Path $RepoRoot 'runs\gurobi_monolithic_nodefiles'
}
New-Item -ItemType Directory -Path $NodeFileDir -Force | Out-Null
$NodeFileDir = (Resolve-Path $NodeFileDir).Path

$Scenario = 'with_redirection'
$DisablePv = $false
$DisableBess = $false
$Speed = '30'
$ValueOfTime = '80'
$Distance = '1.5'

switch ($CaseName) {
    'S01_NR'      { $Scenario = 'no_redirection'; $DisablePv = $true; $DisableBess = $true }
    'S01_R'       { $DisablePv = $true; $DisableBess = $true }
    'S02_NR'      { $Scenario = 'no_redirection'; $DisableBess = $true }
    'S02_R'       { $DisableBess = $true }
    'S03_NR'      { $Scenario = 'no_redirection' }
    'S03_speed10' { $Speed = '10' }
    'S03_speed20' { $Speed = '20' }
    'S03_speed40' { $Speed = '40' }
    'S03_vot50'   { $ValueOfTime = '50' }
    'S03_vot100'  { $ValueOfTime = '100' }
    'S03_dist1p2' { $Distance = '1.2' }
    'S03_dist2p0' { $Distance = '2.0' }
}

$ArgsForPython = @(
    '--dataset', 'full',
    '--scenario', $Scenario,
    '--threads', '10',
    '--mip-gap', '0.0002',
    '--time-limit', '1684800',
    '--soft-mem-limit-gb', '200',
    '--nodefile-start', '0.5',
    '--nodefile-dir', $NodeFileDir,
    '--root-method', 'dual',
    '--node-method', 'dual',
    '--pre-sparsify', '1',
    '--solver-cuts', '1',
    '--speed-car-kmh', $Speed,
    '--value-time-sek-per-h', $ValueOfTime,
    '--max-redirection-distance-km', $Distance,
    '--sensitivity-name', $CaseName,
    '--skip-figures'
)
if ($DisablePv) { $ArgsForPython += '--disable-pv' }
if ($DisableBess) { $ArgsForPython += '--disable-bess' }

Push-Location $RepoRoot
try {
    Write-Host "Case: $CaseName; code revision: $(& git rev-parse HEAD)"
    Write-Host "Node-file directory: $NodeFileDir"
    Write-Host "Solver threads: 10; Gurobi SoftMemLimit: 200 GB; NodefileStart: 0.5 GB"
    Write-Host "Requested relative MIP gap: 0.0002; solve time limit: 1684800 s"
    Write-Host 'The solver certificate determines whether the requested gap was reached.'
    & python (Join-Path $RepoRoot 'src\run_optimization.py') @ArgsForPython
    if ($LASTEXITCODE -ne 0) { throw "Monolithic run exited with code $LASTEXITCODE" }
}
finally {
    Pop-Location
}
