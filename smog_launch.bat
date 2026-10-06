@echo off
setlocal
cd /d "%~dp0"
if not defined LOCALAPPDATA (
  echo THRESHOLD could not locate your Local AppData folder.
  exit /b 1
)
set "THRESHOLD_USER_DIR=%LOCALAPPDATA%\ThresholdProtocol\THRESHOLD"
if not exist "%THRESHOLD_USER_DIR%" mkdir "%THRESHOLD_USER_DIR%"
if not exist "%THRESHOLD_USER_DIR%" (
  echo THRESHOLD could not create its persistent save folder.
  exit /b 1
)
rem Invoke the actual game synchronously so SMOG tracks the entire session.
rem UserDir keeps saves, settings, and logs outside SMOG's version directories.
"%~dp0BackroomsGame\Binaries\Win64\BackroomsGame.exe" "-UserDir=%THRESHOLD_USER_DIR%" %*
exit /b %errorlevel%
