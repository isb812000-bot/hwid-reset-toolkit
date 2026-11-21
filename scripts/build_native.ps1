param([string]$Configuration = "Release")
Push-Location "$PSScriptRoot/../src-native/HwidNative"
dotnet build -c $Configuration
Pop-Location