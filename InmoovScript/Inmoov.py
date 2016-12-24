###############################################################################
#  ___  ________   _____ ______   ________  ________  ___      ___ 
# |\  \|\   ___  \|\   _ \  _   \|\   __  \|\   __  \|\  \    /  /|
# \ \  \ \  \\ \  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \  /  / /
#  \ \  \ \  \\ \  \ \  \\|__| \  \ \  \\\  \ \  \\\  \ \  \/  / / 
#   \ \  \ \  \\ \  \ \  \    \ \  \ \  \\\  \ \  \\\  \ \    / /  
#    \ \__\ \__\\ \__\ \__\    \ \__\ \_______\ \_______\ \__/ /   
#     \|__|\|__| \|__|\|__|     \|__|\|_______|\|_______|\|__|/    
version='0.0.4'
mrlCompatible='1834'
RuningFolder="InmoovScript"
# This is a basic Inmoov script file ( based on fingerstarter )
# If you setup configs in skeleton folder, it can run full Inmoov or separated parts ( right hand / head ... )
# this will run with versions of MRL above 1834
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger starter
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# The Finger Starter is considered here to be right index, 
# so make sure your servo is connected to pin3 of you Arduino
# check your configuration inside BasicConfig.ini

###############################################################################



# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")


##############
# inmoov service declaration
i01 = Runtime.createAndStart("i01", "InMoov")

##############
# health checkup & startup functions
execfile(RuningFolder+'/system/InitCheckup.py')


##############
# sample commands used by fingerstarter

ear.addCommand("attach your finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open your finger", "python", "fingeropen")
ear.addCommand("close your finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")


def fingeropen():
  attachDetachThread(rightHand,2)
  i01.moveHand("right",0,0,0,0,0)
  talkBlocking("ok I open my finger")

def fingerclose():
  attachDetachThread(rightHand,2)
  i01.moveHand("right",180,180,180,180,180)
  talkBlocking("my finger is closed")

def fingermiddle():
  attachDetachThread(rightHand,2)
  i01.moveHand("right",90,90,90,90,90)
  talkBlocking("ok you have my attention")

talkBlocking("ok you have my attention")

