@echo off
python "%~dp0Tools\CreateExcel.py"
if errorlevel 1 (
    pause
    exit /b 1
)
pause