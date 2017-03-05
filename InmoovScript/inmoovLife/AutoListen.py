# ##############################################################################
# 								TIMER ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
WebkitSpeechRecognitionFix = Runtime.start("WebkitSpeechRecognitionFix","Clock")
WebkitSpeechRecognitionFix.setInterval(AutolistenTimerValue)

def WebkitSpeechRecognitionON(timedata):

	if not RobotIsActualySpeaking and not RobotIsSleeping and AutolistenActivated:ear.resumeListening()
	
WebkitSpeechRecognitionFix.addListener("pulse", python.name, "WebkitSpeechRecognitionON")




