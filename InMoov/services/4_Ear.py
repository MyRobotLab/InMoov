# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

i01.ear=Runtime.createAndStart("i01.ear", EarEngine)
i01.startEar()
ear = i01.ear
ear.setAutoListen(True)

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")

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
  global lastRecognized
  lastRecognized=text
  if DEBUG==1:
    print "onRecognized : ",text,RobotneedUpdate
  if isChatbotActivated and i01.RobotIsStarted and not i01.RobotIsSleeping:
    chatBot.getResponse(text.replace("'", " ").replace("-", " "))
  

# ##############################################################################
# EAR RELATED FUNCTIONS
# ##############################################################################
