@echo off
echo ------------------------------------------------------
echo 			MRL INSTALLER
echo ------------------------------------------------------
echo .
echo KILL JAVA to clean reborn
taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
echo ------------------------------------------------------
echo LOG CLEAN UP to free space disk and send clean noworky
echo ------------------------------------------------------
cd..

del myrobotlab.log
echo .
echo ------------------------------------------------------
echo INSTALL DEPENDENCIES AND MRL SERVICES because you need it
echo PLEASE WAIT SOME MINUTES with a cofee is a good idea
echo ------------------------------------------------------
echo .
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
START_INMOOV.bat