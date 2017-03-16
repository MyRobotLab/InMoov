# ##############################################################################
# 								EAR SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

i01.ear=Runtime.createAndStart("i01.ear", EarEngine)
i01.startEar()
ear = i01.ear
sleep(0.1)
ear.pauseListening()


python.subscribe(ear.getName(),"recognized")
chatBot=Runtime.create("chatBot", "ProgramAB")
# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

# this function catch the ear listening
isChatbotActivated=0

def onRecognized(text):
	#RobotneedUpdate : fix about first question do you want to update
	global RobotneedUpdate

	if DEBUG==1:
		print "onRecognized : ",text,RobotneedUpdate
	if isChatbotActivated and RobotIsStarted and not RobotIsSleeping and not RobotneedUpdate:
		chatBot.getResponse(text.replace("'", " ").replace("-", " "))
		
	if (text=="no" or text=="yes") and RobotneedUpdate:
		print "test"
		RobotneedUpdate=0

# ##############################################################################
# EAR RELATED FUNCTIONS
# ##############################################################################
