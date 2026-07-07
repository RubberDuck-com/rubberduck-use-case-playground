# Run one lab (Windows)
# Usage: .\scripts\setup.ps1 -Uc 02

param(
    [Parameter(Mandatory = $true)]
    [string]$Uc,
    [switch]$Verify,
    [switch]$StartServer
)

$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

$args = @("scripts/run-lab.py", "--uc", $Uc)
if ($Verify) { $args += "--verify" }
if ($StartServer) { $args += "--server" }

python @args
