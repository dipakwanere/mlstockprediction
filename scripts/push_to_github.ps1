Param(
    [string]$RemoteUrl
)

if (-not $RemoteUrl) {
    Write-Host "Usage: .\push_to_github.ps1 -RemoteUrl 'https://github.com/youruser/yourrepo.git'"
    exit 1
}

git remote add origin $RemoteUrl 2>$null
git branch -M main
git push -u origin main

Write-Host "Pushed to $RemoteUrl"
