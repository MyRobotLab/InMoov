# ##############################################################################
# 								CHATBOT PROGRAM.AB SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

chatBot=Runtime.createAndStart("chatBot", "ProgramAB")
if EarInterpretEngine=="chatbot":
	if (os.path.isdir(RuningFolder+'inmoovChatbot/'+MyLanguage+'/aiml')):
		chatBot.startSession(RuningFolder+'inmoovChatbot', "default", MyLanguage)
		talkEvent(lang_chatbotActivated)
	else:
		errorSpokenFunc('lang_ChatbotError')
else:
	talkEvent(lang_chatbotDesactivated)
	

