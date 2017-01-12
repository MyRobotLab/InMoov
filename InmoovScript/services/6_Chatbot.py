# ##############################################################################
# 								CHATBOT PROGRAM.AB SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

chatBot=Runtime.createAndStart("chatBot", "ProgramAB")
if EarInterpretEngine=="chatbot":
	if (os.path.isdir(RuningFolder+'bots/'+MyLanguage+'/aiml')):
		try:
			shutil.rmtree(RuningFolder+'bots/'+MyLanguage+'/aimlif')
		except: 
			pass
		chatBot.setPath(RuningFolder)
		chatBot.startSession("default",MyLanguage)
		talkEvent(lang_chatbotActivated)
	else:
		errorSpokenFunc('lang_ChatbotError')
else:
	talkEvent(lang_chatbotDesactivated)
	