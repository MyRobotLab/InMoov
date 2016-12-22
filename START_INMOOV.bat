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
echo INSTALL DEPENDENCIES AND MRL SERVICES because you need it
echo PLEASE WAIT SOME MINUTES with a cofee is a good idea
echo ------------------------------------------------------
echo .
timeout 2 > NUL
java -jar myrobotlab.jar -install
echo ------------------------------------------------------
echo START MRL & INMOOV
echo ------------------------------------------------------
cls
if not exist %cd%\InmoovScript\Inmoov.py (
    echo ERROR : %cd%\InmoovScript\Inmoov.py DOES NOT EXIST
    echo PLEASE PUT SCRIPT AND FOLDERS INSIDE InmoovScript FOLDER
    timeout 10 > NUL
) else (
java -jar myrobotlab.jar -invoke python execFile %cd%/InmoovScript/Inmoov.py -service GUIService GUIService python Python
)

