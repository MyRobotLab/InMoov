
REG ADD HKCU\Console /v CodePage /t REG_DWORD /d 0xfde9 /f
REG ADD HKCU\Console /v FaceName /t REG_SZ /d "Lucida Console" /f
@chcp 65001>nul
@echo off
echo ------------------------------------------------------
echo 			INMOOV BATCH LAUNCHER 0.3 Nixie - 1.1.190+
echo ------------------------------------------------------
echo KILL JAVA to clean reborn

taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
if exist %cd%\mrlNeedReinstall del mrlNeedReinstall

echo ------------------------------------------------------
echo Rotate log files for clean no worky

del myrobotlab.log.1 > NUL
mv myrobotlab.log myrobotlab.log.1

echo "Done."
echo ------------------------------------------------------
COLOR 0F
cls
echo ------------------------------------------------------
echo START MRL AND INMOOV
echo ------------------------------------------------------

REM This is the command to start up the agent jar, specify the memory and run the default InMoov script

SET script=%cd%\InMoov\InMoov.py
timeout 2 > NUL
echo Executing file %script%
java -Dfile.encoding=UTF-8 -jar myrobotlab.jar -m 1024m --service python Python --invoke python execFile %script%
