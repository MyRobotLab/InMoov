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
  if chatBot.wasCleanyShutdowned:
    if chatBot.wasCleanyShutdowned=="nok":errorSpokenFunc('lang_BadShutdown')
  chatBot.repetition_count(10)
  chatBot.setPath(RuningFolder+"chatbot/")
  chatBot.startSession("default",Language)
  talkEvent(lang_chatbotActivated)
  chatBot.addTextListener(htmlFilter)
  htmlFilter.addListener("publishText", python.name, "talk")
  chatBot.setPredicate("default","topic","default")
  chatBot.setPredicate("default","questionfirstinit","")
  chatBot.setPredicate("default","tmpname","")
  chatBot.setPredicate("default","null","")
  chatBot.setPredicate("default","MagicCommandToWakeUp",MagicCommandToWakeUp)
  if chatBot.getPredicate("default","name")!="" and (chatBot.getPredicate("default","lastUsername")=="" or chatBot.getPredicate("default","lastUsername")=="unknown"):
    chatBot.setPredicate("default","lastUsername",unicode(chatBot.getPredicate("default","name"),'utf-8'))
  chatBot.savePredicates()
  #start session based on last recognized person
  if chatBot.getPredicate("default","lastUsername")!="" and chatBot.getPredicate("default","lastUsername")!="unknown":chatBot.setUsername(unicode(chatBot.getPredicate("default","lastUsername"),'utf-8'))
  
else:
  errorSpokenFunc('lang_ChatbotError')

def writeAIML():  
  chatBot.writeAIMLIF()
  
# wikidata helper
WikiFile="WIKIDATA_propEN.txt"
if Language=="fr":WikiFile="WIKIDATA_propFR.txt"