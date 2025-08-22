Param(
    [string]$RemoteUrl
)

if (-not $RemoteUrl) {
    Write-Host "Usage: .\push_to_github.ps1 -RemoteUrl 'https://github.com/youruser/yourrepo.git'"
    exit 1
}

# Check if remote 'origin' exists
$existing = git remote get-url origin 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "Remote 'origin' already exists: $existing"
    if ($existing -ne $RemoteUrl) {
        Write-Host "Updating origin to $RemoteUrl"
        git remote set-url origin $RemoteUrl
    }
} else {
    git remote add origin $RemoteUrl
}

git branch -M main
$push = git push -u origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "Push failed. See git output above."
    exit 1
}

Write-Host "Pushed to $RemoteUrl"
