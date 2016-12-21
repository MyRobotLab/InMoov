###############################################################################
# 								INMOOV SCRIPT
# This is base Inmoov script file ( minimal )
# this will run with versions of MRL above 1850
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a complete hand
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# Thumb------pin 2
# Index------pin 3
# Majeure----pin 4
# RingFinger-pin 5
# Pinky------pin 6
# wrist------pin 7
# check your configuration inside BasicConfig.ini
version='0.0.1'
mrlCompatible='1851'
RuningFolder="InmoovScript"
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
# robot start & checkup
execfile(RuningFolder+'/system/InitCheckup.py')

##############
# verbal commands
ear.addCommand("attach your right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect your right hand", "i01.rightHand", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.startListening()

##############
#Arduino is ok ? lets go !
if RightPortIsConnected:
	i01.startRightHand(MyRightPort)
	

def handopen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)
