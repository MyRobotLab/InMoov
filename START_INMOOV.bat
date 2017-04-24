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
if not exist %cd%\repo.json (
RMDIR /S /Q .myrobotlab
RMDIR /S /Q haarcascades
RMDIR /S /Q hogcascades
RMDIR /S /Q lbpcascades
RMDIR /S /Q libraries
RMDIR /S /Q pythonModules
RMDIR /S /Q repo
RMDIR /S /Q resource
RMDIR /S /Q tessdata
del ivychain.xml
del myrobotlab.log
del repo.json
)
echo ------------------------------------------------------
echo INSTALL DEPENDENCIES AND MRL SERVICES because you need it
echo PLEASE WAIT SOME MINUTES with a cofee is a good idea
echo ------------------------------------------------------
timeout 2 > NUL
java -jar myrobotlab.jar -install InMoov VoiceRss WikiDataFetcher Polly ProgramAB
echo ------------------------------------------------------
echo START MRL & INMOOV
echo ------------------------------------------------------
cls
if not exist %cd%\Inmoov\Inmoov.py (
    echo ERROR : %cd%\Inmoov\Inmoov.py DOES NOT EXIST
    echo PLEASE PUT SCRIPT AND FOLDERS INSIDE Inmoov FOLDER
    timeout 10 > NUL
) else (
java -jar myrobotlab.jar -invoke python execFile %cd%/Inmoov/Inmoov.py -service python Python
)

