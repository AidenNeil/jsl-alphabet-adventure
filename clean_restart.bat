@echo off
echo ========================================
echo Cleaning and Restarting JSL Game
echo ========================================
echo.

echo [1/4] Stopping any Python processes...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/4] Cleaning Python cache...
if exist __pycache__ rmdir /s /q __pycache__
if exist .pytest_cache rmdir /s /q .pytest_cache
for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
del /s /q *.pyc 2>nul

echo [3/4] Verifying image directory...
if exist src\jsl_alphabet_test (
    echo    [OK] Found src\jsl_alphabet_test
) else (
    echo    [ERROR] Missing src\jsl_alphabet_test
)

echo [4/4] Starting fresh server...
echo.
echo ========================================
echo Starting JSL Alphabet Adventure...
echo ========================================
echo.

npm run dev

