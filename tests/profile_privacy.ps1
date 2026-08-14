$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$files = @(
    (Join-Path $repoRoot 'README.md'),
    (Join-Path $repoRoot 'profile/README.md'),
    (Join-Path $repoRoot 'profile/README_de.md'),
    (Join-Path $repoRoot 'llms.txt'),
    (Join-Path $repoRoot 'CHANGELOG.md'),
    (Join-Path $repoRoot 'BEFUNDE.md'),
    (Join-Path $repoRoot 'tests/profile_privacy.ps1')
)
$publicRepoNames = @('ChatAndChess', 'rpx', 'KlangpultLight', '.github')
$publicContextNames = $publicRepoNames + @('entertain-and-more')
$privateRepoDenylist = @(
    $env:PROFILE_PRIVATE_REPO_DENYLIST -split ';' |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ }
)
$utf8Strict = [System.Text.UTF8Encoding]::new($false, $true)

foreach ($path in $files) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Missing profile file: $path"
    }
    $content = $utf8Strict.GetString([System.IO.File]::ReadAllBytes($path))
    foreach ($pattern in @(
        'https://github\.com/entertain-and-more/([A-Za-z0-9_.-]+)',
        'https://raw\.githubusercontent\.com/entertain-and-more/([A-Za-z0-9_.-]+)',
        'https://api\.github\.com/repos/entertain-and-more/([A-Za-z0-9_.-]+)'
    )) {
        foreach ($match in [regex]::Matches(
            $content,
            $pattern,
            [System.Text.RegularExpressions.RegexOptions]::IgnoreCase
        )) {
            if ($match.Groups[1].Value -notin $publicRepoNames) {
                throw "Non-public repository reference in $path"
            }
        }
    }
    foreach ($line in $content -split "`r?`n") {
        if ($line -notmatch '(?i)(?:private|internal|privat|nicht öffentlich)') { continue }
        if ($line -match '(?i)entertain-and-more/[A-Za-z0-9_.-]+') {
            throw "Named private/internal repository disclosure in $path"
        }
        foreach ($token in [regex]::Matches($line, '`([A-Za-z0-9_.-]+)`')) {
            $name = $token.Groups[1].Value
            if ($name -notin $publicContextNames -and $name -notmatch '(?i)\.(?:md|txt|json|ya?ml|ps1)$') {
                throw "Named private/internal repository disclosure in $path"
            }
        }
    }
    foreach ($privateRepoName in $privateRepoDenylist) {
        $privatePattern = '(?i)(?<![A-Za-z0-9_-])' + [regex]::Escape($privateRepoName) + '(?![A-Za-z0-9_-])'
        if ([regex]::IsMatch($content, $privatePattern)) {
            throw "Externally denied private repository reference in $path"
        }
    }
}

Write-Output ('PASS profile privacy: {0} files, public_count=4' -f $files.Count)
