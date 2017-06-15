REG ADD HKCU\Console /v CodePage /t REG_DWORD /d 0xfde9 /f
REG ADD HKCU\Console /v FaceName /t REG_SZ /d "Lucida Console" /f
@echo off
echo ------------------------------------------------------
echo 			INMOOV LAUNCHER
echo ------------------------------------------------------
echo .
echo KILL JAVA to clean reborn
taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
echo ------------------------------------------------------
echo LOG CLEAN UP to free space disk and send clean noworky
echo ------------------------------------------------------
del myrobotlab.log
echo .
echo ------------------------------------------------------
echo UPDATE MRL INSTALLATION
echo ------------------------------------------------------
echo .
move /y %cd%\myrobotlab-*.jar %cd%\myrobotlab.jar
if exist %cd%\mrlNeedReinstall (
RMDIR /S /Q .myrobotlab
RMDIR /S /Q haarcascades
RMDIR /S /Q hogcascades
RMDIR /S /Q lbpcascades
RMDIR /S /Q libraries
RMDIR /S /Q pythonModules
RMDIR /S /Q resource
RMDIR /S /Q tessdata
del ivychain.xml
del myrobotlab.log
del repo.json
del mrlNeedReinstall
)
COLOR 4F
cls
echo ------------------------------------------------------
echo          !!!            MRL UPDATER          !!!
echo          !!!            PLEASE WAIT          !!!
echo          !!!       IT CAN TAKE LONG TIME     !!!
echo          !!!            DO NOT CLOSE         !!!
echo ------------------------------------------------------
timeout 3 > NUL
java -Dfile.encoding=UTF-8 -jar myrobotlab.jar -install InMoov VoiceRss WikiDataFetcher Polly ProgramAB AzureTranslator
cls
COLOR 0F
echo ------------------------------------------------------
echo START MRL & INMOOV
echo ------------------------------------------------------
if not exist %cd%\Inmoov\InMoov.py (
    echo ERROR : %cd%\InMoov\InMoov.py DOES NOT EXIST
    echo PLEASE PUT SCRIPT AND FOLDERS INSIDE InMoov FOLDER
    timeout 10 > NUL
) else (
java -Dfile.encoding=UTF-8 -jar myrobotlab.jar -invoke python execFile %cd%/InMoov/InMoov.py -service python Python
)

