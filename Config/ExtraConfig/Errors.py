# -- coding: utf-8 --

# ##############################################################################
# ERRORS FILE
# ##############################################################################

# FingerStarter doesnt use Chatbot, so we hardcode language for few error functions
# THIS FILE NEED TO BE UTF8 IF YOU GRAB IT FROM GITHUB
# BECAUSE THERE IS ACCENT INSIDE IT
def errorSpokenFunc(errorType):
	
	if errorType=="RightPortIsConencted":
		errorSpoken="There is a connection problem ! with your communication port, "+MyRightPort+" , check your arduino"
		
		if MyLanguage=="FR":
			errorSpoken="Impossible de se connecter au port, "+MyRightPort+" de l'arduino"
			
		if MyLanguage=="ES":	
			errorSpoken="Imposible de conectar al puerto, "+MyRightPort
		
		if MyLanguage=="DE":	
			errorSpoken="Kommunikationsproblem mit dem Hafen, "+MyRightPort
			
		talkBlocking(errorSpoken)
		print errorSpoken
		
		
	if errorType=="VoiceError":
		errorSpoken="There is a problem with the voice you have choosen !"
		talkBlocking(errorSpoken)
		print errorSpoken
		
