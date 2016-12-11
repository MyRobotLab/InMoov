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
java -jar myrobotlab.jar -invoke python execFile %cd%/BaseScript/Main_Script1.py -service GUIService GUIService python Python