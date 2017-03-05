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
def onRecognized(text):
	if DEBUG==1:
		print "onRecognized : ",text
	if EarInterpretEngine=="chatbot" and RobotIsStarted and not RobotIsSleeping:
		chatBot.getResponse(text.replace("'", " ").replace("-", " "))

# ##############################################################################
# EAR RELATED FUNCTIONS
# ##############################################################################
