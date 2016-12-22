# ##############################################################################
# ERRORS FILE
# ##############################################################################

# FingerStarter doesnt use Chatbot, so we hardcode language to english for few error functions


def errorSpokenFunc(errorType,param):
	
	
	subconsciousMouth.speakBlocking("Alert! Alert! Alert! This is my subconscious speaking, can I have your attention please ! ")
	
	if errorType=="ArduinoNotConnected":
		errorSpoken="There is a problem ! with my communication port, "+param+" , check your arduino"

	if errorType=="VoiceDownloaded":
		errorSpoken="I have downloaded a new voice, I will stop the system, please restart me. please do it"
	
	if errorType=="MyvoiceType":
		errorSpoken="There is a problem with the voice you have choosen !"

		
	if errorType=="MyLanguage":
		errorSpoken="There is a problem with the language you have choosen !"
		
	if errorType=="MrlNeedUpdate":
		errorSpoken="You My Robotlab version is too old, please update it"
	
	subconsciousMouth.speakBlocking(errorSpoken)
	
	print errorSpoken
		
