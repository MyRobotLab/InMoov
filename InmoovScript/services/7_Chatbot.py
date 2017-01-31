# ##############################################################################
# 								CHATBOT PROGRAM.AB SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

Runtime.createAndStart("htmlFilter", "HtmlFilter")
chatBot=Runtime.start("chatBot", "ProgramAB")
if EarInterpretEngine=="chatbot":
	if (os.path.isdir(RuningFolder+'inmoovVocal/bots/'+MyLanguage+'/aiml')):
		try:
			#waiting a fix we sould remove csv files
			shutil.rmtree(RuningFolder+'inmoovVocal/bots/'+MyLanguage+'/aimlif')
		except: 
			pass
		chatBot.setPath(RuningFolder+"inmoovVocal/")
		chatBot.cleanOutOfDateAimlIFFiles(MyLanguage)
		talkEvent(lang_chatbotLoading)
		chatBot.startSession("default",MyLanguage)
		talkEvent(lang_chatbotActivated)
		talkEvent(lang_earaddcomandsDeactivated)
		chatBot.addTextListener(htmlFilter)
		htmlFilter.addListener("publishText", python.name, "talk") 
	else:
		errorSpokenFunc('lang_ChatbotError')
else:
	talkEvent(lang_chatbotDeactivated)
	talkEvent(lang_earaddcomandsActivated)
def writeAIML():	
	chatBot.writeAIMLIF()
	