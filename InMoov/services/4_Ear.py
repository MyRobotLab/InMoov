# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

EarEngine=ThisServicePartConfig.get('MAIN', 'EarEngine')
setContinuous=ThisServicePartConfig.getboolean('MAIN', 'setContinuous')
setAutoListen=ThisServicePartConfig.getboolean('MAIN', 'setAutoListen')
ForceMicroOnIfSleeping=True
MagicCommandToWakeUp="wake up"
try:
  ForceMicroOnIfSleeping=ThisServicePartConfig.getboolean('MAIN', 'ForceMicroOnIfSleeping')
  MagicCommandToWakeUp=unicode(ThisServicePartConfig.get('MAIN', 'MagicCommandToWakeUp'),'utf-8')
except:
  pass

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

i01.ear=Runtime.createAndStart("i01.ear", EarEngine)
i01.startEar()
ear = i01.ear
ear.setAutoListen(setAutoListen)
if EarEngine=="WebkitSpeechRecognition":ear.setContinuous(setContinuous)

if not isWebGuiActivated and EarEngine=="WebkitSpeechRecognition":
# start the browsers and show the WebkitSpeechRecognition service named i01.ear
  webgui = Runtime.create("webgui","WebGui")
  webgui.autoStartBrowser(False)
  webgui.startService()
  isWebGuiActivated=True
  
if isWebGuiActivated and EarEngine=="WebkitSpeechRecognition":webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

python.subscribe(ear.getName(),"recognized")
chatBot=Runtime.create("chatBot", "ProgramAB")
# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

# this function catch the ear listening
isChatbotActivated=0
global lastRecognized
lastRecognized=""
def onRecognized(text):
  #RobotneedUpdate : fix about first question do you want to update
  if text!="":
    global lastRecognized
    lastRecognized=text
    text=text.replace("'", " ").replace("-", " ")
    if DEBUG==1:print "onRecognized : ",text,RobotneedUpdate
    if isChatbotActivated and i01.RobotIsStarted:
      if i01.RobotIsSleeping and unicode(text,'utf-8')==MagicCommandToWakeUp:sleepModeWakeUp()        
      if not i01.RobotIsSleeping and text!=MagicCommandToWakeUp:
        chatBot.getResponse(text)
        humanDetected()
  
# ##############################################################################
# EAR RELATED FUNCTIONS
# ##############################################################################