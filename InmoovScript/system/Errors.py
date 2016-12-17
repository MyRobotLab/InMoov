# ##############################################################################
# ERRORS FILE
# ##############################################################################

# FingerStarter doesnt use Chatbot, so we hardcode language to english for few error functions


def errorSpokenFunc(errorType):
	
	
	subconsciousMouth.speakBlocking("Alert! Alert! Alert! This is my subconscious speaking, can I have your attention please ! ")
	
	if errorType=="RightPortIsConnected":
		errorSpoken="There is a problem ! with my communication port, "+MyRightPort+" , check your arduino"
	
			
		
	if errorType=="voiceType":
		errorSpoken="There is a problem with the voice you have choosen !"

		
	if errorType=="MyLanguage":
		errorSpoken="There is a problem with the language you have choosen !"
	
	subconsciousMouth.speakBlocking(errorSpoken)
	subconsciousMouth.speakBlocking("My system run degraded now, please fix me as soon as possible ! ")
	print errorSpoken
		
