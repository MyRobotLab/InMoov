##						   ___  ________   _____ ______   ________  ________  ___      ___ 
##						  |\  \|\   ___  \|\   _ \  _   \|\   __  \|\   __  \|\  \    /  /|
##						  \ \  \ \  \\ \  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \  /  / /
##						   \ \  \ \  \\ \  \ \  \\|__| \  \ \  \\\  \ \  \\\  \ \  \/  / / 
##						    \ \  \ \  \\ \  \ \  \    \ \  \ \  \\\  \ \  \\\  \ \    / /  
##						     \ \__\ \__\\ \__\ \__\    \ \__\ \_______\ \_______\ \__/ /   
##						      \|__|\|__| \|__|\|__|     \|__|\|_______|\|_______|\|__|/    
version='1.0.0'

# this will run with versions of MRL above :
mrlCompatible='2685'

# ###################################################################################
# This is the full configurable launcher script for Inmoov service :
# MORE informations here : http://myrobotlab.org/service/InMoov
# At this time configurable things are inside the config folder. 
# By default virtual environment is started, so you can test things with no risk ! 
#
# To start using the Finger Starter with real hardware, set : 
# ( The Finger Starter is considered here to be right index, 
# so make sure your servo is connected to pin3 of you Arduino )
##
#   ScriptType=RightSide | inside config/_InMoov.config
#   MyRightPort=COMx | inside config/_service_6_Arduino.config
#   isRightHandActivated=True | inside config/skeleton_rightHand.config
#   voice command sample : OPEN HAND
##
# Check your configuration inside Inmoov.config
# Change voice and speech engine inside mouth.config
# If you setup 2 arduino + configs in skeleton folder, it can run full Inmoov or separated parts ( right hand / head ... )
# ###################################################################################


##############
# Main inmoov service
i01 = Runtime.createAndStart("i01", "InMoov")

##############
# robot checkup and initialisation ( skeleton & services )
RuningFolder="InMoov"
execfile(RuningFolder+'/system/InitCheckup.py')


# ###################################################################################
# SAMPLE COMMANDS 
#
# WARNING : basic vocal commands ( activated only if chatbot is disable inside config/service_A_Chatbot.config )
#
# Go further ! you can find more basic vocal commands into inmoovVocal/ear.addCommand
# Go further !! you can find more associated functions into inmoovGestures
# Go further !!! you can find almost all chatbot vocal command into chatbot\bots\[lang]\aiml\_inmoovGestures.aiml
# ###################################################################################

ear.addCommand("attach your finger", "i01.rightHand.index", "attach") #to remove soon
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("open your finger", "python", "fingeropen")
ear.addCommand("close your finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")

# functions called by the basic vocal commands engine
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
#Go further !!!! and write some code lines inside custom/InMoov_custom.py
execfile(RuningFolder+'custom/InMoov_custom.py')