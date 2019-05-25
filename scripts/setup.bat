:: This is a setup script to create the dev environment for windows.
:: Run this script in the directory where you want the project folder.
cd C:\User\%USERNAME%
mkdir DndTemp
cd DndTemp
If (path | find /C /I "python") = 0 (
    curl -O https://www.python.org/ftp/python/3.5.3/python-3.5.3-amd64.exe
)
msiexec  "python-3.5.3-amd64.exe" /qn
