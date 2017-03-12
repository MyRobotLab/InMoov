# ##############################################################################
# 								CHATBOT PROGRAM.AB SERVICE
# ##############################################################################

# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=inspect.getfile(inspect.currentframe()).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isChatbotActivated=0

isChatbotActivated=ThisServicePartConfig.getboolean('MAIN', 'isChatbotActivated')

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

Runtime.createAndStart("htmlFilter", "HtmlFilter")
chatBot=Runtime.start("chatBot", "ProgramAB")
if isChatbotActivated:
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
		chatBot.addTextListener(htmlFilter)
		htmlFilter.addListener("publishText", python.name, "talk") 
	else:
		errorSpokenFunc('lang_ChatbotError')

def writeAIML():	
	chatBot.writeAIMLIF()
	