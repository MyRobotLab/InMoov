REG ADD HKCU\Console /v CodePage /t REG_DWORD /d 0xfde9 /f
REG ADD HKCU\Console /v FaceName /t REG_SZ /d "Lucida Console" /f
@chcp 65001>nul
@echo off
echo ------------------------------------------------------
echo 			INMOOV BATCH INSTALLER 0.3 Nixie - 1.1.190+
echo ------------------------------------------------------
echo .
echo KILL JAVA to clean reborn
taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
echo ------------------------------------------------------
echo LOG CLEAN UP to free space disk and send clean noworky
echo ------------------------------------------------------
del myrobotlab.log.1 > NUL
mv myrobotlab.log myrobotlab.log.1

timeout 1 > NUL
COLOR 2F
cls
echo ------------------------------------------------------
echo          !!!         INMOOV INSTALLER        !!!
echo          !!!            PLEASE WAIT          !!!
echo          !!!       IT CAN TAKE LONG TIME     !!!
echo          !!!            DO NOT CLOSE         !!!
echo ------------------------------------------------------
timeout 2 > NUL
java -Dfile.encoding=UTF-8 -jar myrobotlab.jar --install
timeout 10 > NUL
COLOR 3F
cls
echo ------------------------------------------------------
echo You can now run START_INMOOV.bat
echo ------------------------------------------------------
timeout 5 > NUL
