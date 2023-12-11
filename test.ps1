param (
    # [System.IO.FileInfo]$App
    [System.String]$App
)

try {
    $AppExe = [string]($App.Split("\")[-1])
    $App
    Write-Host "AppExe: $AppExe"
    Write-Host "Process: $Process"

    Start-Sleep -Seconds 10
    taskkill.exe /F /IM $AppExe
}
catch {
    Write-Error "App not found: $App"
    exit 1
}