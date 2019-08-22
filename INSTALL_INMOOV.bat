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

echo "Done."
echo ------------------------------------------------------
echo UPDATE MRL INSTALLATION
echo ------------------------------------------------------
timeout 1 > NUL
echo .
if exist %cd%\InMoov\system\updated RMDIR /S /Q .myrobotlab
if exist %cd%\InMoov\system\updated del %cd%\InMoov\system\updated
move /y %cd%\myrobotlab-*.jar %cd%\myrobotlab.jar > NUL
if exist %cd%\mrlNeedReinstall RMDIR /S /Q haarcascades
if exist %cd%\mrlNeedReinstall RMDIR /S /Q hogcascades
if exist %cd%\mrlNeedReinstall RMDIR /S /Q lbpcascades
if exist %cd%\mrlNeedReinstall RMDIR /S /Q libraries
if exist %cd%\mrlNeedReinstall RMDIR /S /Q pythonModules
if exist %cd%\mrlNeedReinstall RMDIR /S /Q resource
if exist %cd%\mrlNeedReinstall RMDIR /S /Q tessdata
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\de\aimlif
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\es\aimlif
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\en\aimlif
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\fr\aimlif
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\hi\aimlif
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\nl\aimlif
if exist %cd%\mrlNeedReinstall RMDIR /S /Q InMoov\chatbot\bots\ru\aimlif
if exist %cd%\mrlNeedReinstall del ivychain.xml
if exist %cd%\mrlNeedReinstall del myrobotlab.log
if exist %cd%\mrlNeedReinstall del repo.json
if exist %cd%\mrlNeedReinstall del %cd%\.myrobotlab\serviceData.json
if exist %cd%\mrlNeedReinstall del mrlNeedReinstall
COLOR 2F
cls
echo ------------------------------------------------------
echo          !!!         INMOOV INSTALLER        !!!
echo          !!!            PLEASE WAIT          !!!
echo          !!!       IT CAN TAKE LONG TIME     !!!
echo          !!!            DO NOT CLOSE         !!!
echo ------------------------------------------------------
timeout 2 > NUL
java -Dfile.encoding=UTF-8 -jar myrobotlab.jar --install RasPi InMoov VoiceRss WikiDataFetcher Polly ProgramAB AzureTranslator LocalSpeech IndianTts
timeout 20 > NUL
COLOR 3F
cls
echo ------------------------------------------------------
echo You can now run START_INMOOV.bat
echo ------------------------------------------------------
timeout 5 > NUL
