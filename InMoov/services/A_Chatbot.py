# ##############################################################################
#                 CHATBOT PROGRAM.AB SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('chatbot',ThisServicePart+'.config')
###############################################################################

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
  if (os.path.isdir(RuningFolder+'chatbot/bots/'+MyLanguage+'/aiml')):
    try:
      #waiting a fix we sould remove csv files
      shutil.rmtree(RuningFolder+'chatbot/bots/'+MyLanguage+'/aimlif')
    except: 
      pass
    chatBot.repetition_count(10)
    chatBot.setPath(RuningFolder+"chatbot/")
    chatBot.cleanOutOfDateAimlIFFiles(MyLanguage)
    talkEvent(lang_chatbotLoading)
    chatBot.startSession("default",MyLanguage)
    talkEvent(lang_chatbotActivated)
    chatBot.addTextListener(htmlFilter)
    htmlFilter.addListener("publishText", python.name, "talk")
    chatBot.setPredicate("default","topic","default")
    chatBot.setPredicate("default","questionfirstinit","")
    chatBot.setPredicate("default","tmpname","")
    chatBot.savePredicates()
  else:
    errorSpokenFunc('lang_ChatbotError')

def writeAIML():  
  chatBot.writeAIMLIF()
  