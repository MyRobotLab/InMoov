# ##############################################################################
# 								TIMER ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
WebkitSpeachReconitionFix = Runtime.start("WebkitSpeachReconitionFix","Clock")
WebkitSpeachReconitionFix.setInterval(15000)

def WebkitSpeachReconitionON(timedata):

	if RobotIsActualySpeaking==0:
		ear.resumeListening()
	

WebkitSpeachReconitionFix.addListener("pulse", python.name, "WebkitSpeachReconitionON")

WebkitSpeachReconitionFix.startClock()


