##						   ___  ________   _____ ______   ________  ________  ___      ___ 
##						  |\  \|\   ___  \|\   _ \  _   \|\   __  \|\   __  \|\  \    /  /|
##						  \ \  \ \  \\ \  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \  /  / /
##						   \ \  \ \  \\ \  \ \  \\|__| \  \ \  \\\  \ \  \\\  \ \  \/  / / 
##						    \ \  \ \  \\ \  \ \  \    \ \  \ \  \\\  \ \  \\\  \ \    / /  
##						     \ \__\ \__\\ \__\ \__\    \ \__\ \_______\ \_______\ \__/ /   
##						      \|__|\|__| \|__|\|__|     \|__|\|_______|\|_______|\|__|/    OS - [wip]
version='0.3.5'

# this will run with versions of MRL above :
mrlCompatible='2237'

# ###################################################################################
# This is a very minimal script for Inmoov
# ( also called FINGERSTARTER : A legend tells that when Inmoov came to life he did not shout, but moved a finger first )
# although this script is very short you can still
# do voice control of a finger starter
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# The Finger Starter is considered here to be right index, 
# so make sure your servo is connected to pin3 of you Arduino
# check your configuration inside Inmoov.config
# If you setup 2 arduino + configs in skeleton folder, it can run full Inmoov or separated parts ( right hand / head ... )
# ###################################################################################



##############
# Main inmoov service declaration
i01 = Runtime.createAndStart("i01", "InMoov")

##############
# robot checkup and initialisation ( skeleton & services)
RuningFolder="InMoov"
execfile(RuningFolder+'/system/InitCheckup.py')




# ###################################################################################
# SAMPLE COMMANDS 
# Go further you can find more vocal commands into inmoovVocal/ear.addCommand
# Go further you can find more associated functions into inmoovGestures
# ###################################################################################

ear.addCommand("attach your finger", "i01.rightHand.index", "attach") #to remove soon
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("open your finger", "python", "fingeropen")
ear.addCommand("close your finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")

# functions called by the vocal commands
def fingeropen():
  i01.moveHand("right",0,0,0,0,0)
  talkBlocking("ok I open my finger")

def fingerclose():
  i01.moveHand("right",180,180,180,180,180)
  talkBlocking("my finger is closed")

def fingermiddle():
  i01.moveHand("right",90,90,90,90,90)
  talkBlocking("ok you have my attention")
  
  
  

##############
#Go more further ! and code your own script in this file
execfile(RuningFolder+'custom/InMoov_custom.py')