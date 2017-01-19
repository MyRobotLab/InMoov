#autorestart 15 seconds
def WebkitSpeechRecognitionON(timedata):
	try:
		ear.startListening()
	except:
		pass

WebkitSpeechRecognitionFix.addListener("pulse", python.name, "WebkitSpeechRecognitionON")		

