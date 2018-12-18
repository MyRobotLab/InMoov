# ##############################################################################
#                 CHATBOT PROGRAM.AB SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')
CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isChatbotActivated=ThisServicePartConfig.getboolean('MAIN', 'isChatbotActivated')

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if isChatbotActivated:
  i01.chatBot=Runtime.start("i01.chatBot", "ProgramAB")
  htmlFilter=Runtime.start("htmlFilter", "HtmlFilter")
  i01.chatBot.addTextListener(htmlFilter)
  htmlFilter.addListener("publishText", "i01", "speak")
  i01.chatBot.attach(i01.ear)
  i01.startBrain()