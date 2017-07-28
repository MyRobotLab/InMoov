REG ADD HKCU\Console /v CodePage /t REG_DWORD /d 0xfde9 /f
REG ADD HKCU\Console /v FaceName /t REG_SZ /d "Lucida Console" /f
@echo off
echo ------------------------------------------------------
echo 			INMOOV BATCH LAUNCHER 0.2
echo ------------------------------------------------------
echo .
echo KILL JAVA to clean reborn
taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
echo ------------------------------------------------------
echo LOG CLEAN UP to free space disk and send clean noworky
echo ------------------------------------------------------
del myrobotlab.log > NUL
echo .
echo ------------------------------------------------------
echo UPDATE MRL INSTALLATION
echo ------------------------------------------------------
timeout 1 > NUL
echo .
move /y %cd%\myrobotlab-*.jar %cd%\myrobotlab.jar > NUL
if exist %cd%\mrlNeedReinstall RMDIR /S /Q haarcascades
if exist %cd%\mrlNeedReinstall RMDIR /S /Q hogcascades
if exist %cd%\mrlNeedReinstall RMDIR /S /Q lbpcascades
if exist %cd%\mrlNeedReinstall RMDIR /S /Q libraries
if exist %cd%\mrlNeedReinstall RMDIR /S /Q pythonModules
if exist %cd%\mrlNeedReinstall RMDIR /S /Q resource
if exist %cd%\mrlNeedReinstall RMDIR /S /Q tessdata
if exist %cd%\mrlNeedReinstall del ivychain.xml
if exist %cd%\mrlNeedReinstall del myrobotlab.log
if exist %cd%\mrlNeedReinstall del repo.json
if exist %cd%\mrlNeedReinstall del mrlNeedReinstall
COLOR 2F
cls
echo ------------------------------------------------------
echo          !!!            MRL UPDATER          !!!
echo          !!!            PLEASE WAIT          !!!
echo          !!!       IT CAN TAKE LONG TIME     !!!
echo          !!!            DO NOT CLOSE         !!!
echo ------------------------------------------------------
timeout 3 > NUL
java -Dfile.encoding=UTF-8 -jar myrobotlab.jar -install InMoov VoiceRss WikiDataFetcher Polly ProgramAB AzureTranslator
COLOR 0F
cls
echo ------------------------------------------------------
echo START MRL AND INMOOV
echo ------------------------------------------------------
if not exist %cd%\Inmoov\InMoov.py (
COLOR 4F
echo ERROR : %cd%\InMoov\InMoov.py is not available
echo CHECK ABOUT SPACES INSIDE FOLDERS NAME or SPECIAL CHARACTERS 
echo "c:\mrl" is a great place to start
timeout 10 > NUL
) else (java -Dfile.encoding=UTF-8 -jar myrobotlab.jar -invoke python execFile %cd%/InMoov/InMoov.py -service python Python)