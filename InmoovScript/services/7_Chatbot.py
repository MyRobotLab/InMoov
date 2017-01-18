# ##############################################################################
# 								CHATBOT PROGRAM.AB SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################
Runtime.start("htmlFilter", "HtmlFilter")
chatBot=Runtime.createAndStart("chatBot", "ProgramAB")
if EarInterpretEngine=="chatbot":
	if (os.path.isdir(RuningFolder+'bots/'+MyLanguage+'/aiml')):
		try:
			#waiting a fix we sould remove csv files
			shutil.rmtree(RuningFolder+'bots/'+MyLanguage+'/aimlif')
		except: 
			pass
		chatBot.setPath(RuningFolder)
		chatBot.cleanOutOfDateAimlIFFiles(MyLanguage)
		chatBot.startSession("default",MyLanguage)
		talkEvent(lang_chatbotActivated)
		chatBot.addTextListener(htmlFilter)
		htmlFilter.addListener("publishText", python.name, "talk") 
	else:
		errorSpokenFunc('lang_ChatbotError')
else:
	talkEvent(lang_chatbotDesactivated)

def writeAIML():	
	chatBot.writeAIMLIF()
	