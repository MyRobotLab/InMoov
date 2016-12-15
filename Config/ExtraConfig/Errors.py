# -- coding: utf-8 --

# ##############################################################################
# ERRORS FILE
# ##############################################################################

# FingerStarter doesnt use Chatbot, so we hardcode language for few error functions
# THIS FILE NEED TO BE UTF8 IF YOU GRAB IT FROM GITHUB
# BECAUSE THERE IS ACCENT INSIDE IT
def defaultSystemVoiceAndLanguage():
	voiceType="cmu-slt-hsmm"
	mouth.setVoice(voiceType)

def errorSpokenFunc(errorType):
	
	if errorType=="RightPortIsConnected":
		errorSpoken="There is a connection problem ! with your communication port, "+MyRightPort+" , check your arduino"
		
		if MyLanguage.lower()=="fr":
			errorSpoken="Impossible de se connecter au port, "+MyRightPort+" de l'arduino"
			
		if MyLanguage.lower()=="es":	
			errorSpoken="Imposible de conectar al puerto, "+MyRightPort
		
		if MyLanguage.lower()=="de":	
			errorSpoken="Kommunikationsproblem mit dem Hafen, "+MyRightPort
			
		
	if errorType=="voiceType":
		defaultSystemVoiceAndLanguage()
		errorSpoken="There is a problem with the voice you have choosen !"

		
	if errorType=="MyLanguage":
		defaultSystemVoiceAndLanguage()
		errorSpoken="There is a problem with the language you have choosen !"
	
	talkBlocking(errorSpoken)
	print errorSpoken
		
