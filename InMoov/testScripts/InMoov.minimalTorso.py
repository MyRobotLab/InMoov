#file : InMoov.minimalTorso.py
#MRL version above 1.0.2000
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the skeleton.config
# although this script is very short you can still
# do voice control of the Torso
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Change to the port that you use
leftPort = "COM9"

#to tweak the default voice
Voice="cmu-bdl-hsmm" #Male US voice 
#Voice="cmu-slt-hsmm" #Default female for MarySpeech
voiceType = Voice
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
#mouth.installComponentsAcceptLicense(Voice)
mouth.setVoice(voiceType)
##############
# starting InMoov service
i01 = Runtime.create("i01", "InMoov")
#Force Arduino to connect (fix Todo)
left = Runtime.createAndStart("i01.left", "Arduino")
left.connect(leftPort)
##############
# starting parts
i01.startEar()
# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")
i01.startMouth()
##############
torso = Runtime.create("i01.torso","InMoovTorso")
# tweaking default torso settings
#Velocity
torso.topStom.setMaxVelocity(-1)
torso.midStom.setMaxVelocity(-1)
#torso.lowStom.setMaxVelocity(-1)
#Mapping
torso.topStom.map(0,180,65,120)
torso.midStom.map(0,180,70,110)
#torso.lowStom.map(0,180,60,110)
#Rest position
torso.topStom.setRest(90)
torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
#################
i01 = Runtime.start("i01","InMoov")
################# 
i01.startTorso(leftPort)
i01.torso.enableAutoDisable(False)
i01.torso.enableAutoEnable(True)
#################
# verbal commands
ear = i01.ear

ear.addCommand("attach everything", "i01", "enable")
ear.addCommand("disconnect everything", "i01", "disable")
ear.addCommand("attach torso", "i01.torso", "enable")
ear.addCommand("disconnect torso", "i01.torso", "disable")
ear.addCommand("rest", "i01.torso", "rest")#Hardcoded gesture
ear.addCommand("relax", "python", "relax")
ear.addCommand("full speed", "python", "fullspeed")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("test your stomach", "python", "teststomach")
ear.addCommand("to the right", "python", "totheright")
ear.addCommand("to the left", "python", "totheleft")
ear.addCommand("turn to the right side", "python", "turnrightside")
ear.addCommand("turn to the left side", "python", "turnleftside")
#file : InMoov.minimalTorso.py
#MRL version above 1.0.2000
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the skeleton.config
# although this script is very short you can still
# do voice control of the Torso
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Change to the port that you use
leftPort = "COM9"

#to tweak the default voice
Voice="cmu-bdl-hsmm" #Male US voice 
#Voice="cmu-slt-hsmm" #Default female for MarySpeech
voiceType = Voice
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
mouth.installComponentsAcceptLicense(Voice)
mouth.setVoice(voiceType)
##############
# starting InMoov service
i01 = Runtime.create("i01", "InMoov")
#Force Arduino to connect (fix Todo)
left = Runtime.createAndStart("i01.left", "Arduino")
left.connect(leftPort)
##############
# starting parts
i01.startEar()
# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")
##############
i01.startMouth()
##############
torso = Runtime.create("i01.torso","InMoovTorso")
# tweaking default torso settings
# Velocity
torso.topStom.setMaxVelocity(-1)
torso.midStom.setMaxVelocity(-1)
#torso.lowStom.setMaxVelocity(-1)
# Mapping
torso.topStom.map(0,180,65,120)
torso.midStom.map(0,180,70,110)
#torso.lowStom.map(0,180,60,110)
# Rest position
torso.topStom.setRest(90)
torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
#################
i01 = Runtime.start("i01","InMoov")
################# 
i01.startTorso(leftPort)
i01.torso.enableAutoDisable(False)
i01.torso.enableAutoEnable(True)
#################
# verbal commands
ear = i01.ear

ear.addCommand("attach everything", "i01", "enable")
ear.addCommand("disconnect everything", "i01", "disable")
ear.addCommand("attach torso", "i01.torso", "enable")
ear.addCommand("disconnect torso", "i01.torso", "disable")
ear.addCommand("rest", "i01.torso", "rest")#Hardcoded gesture
ear.addCommand("relax", "python", "relax")
ear.addCommand("full speed", "python", "fullspeed")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("test your stomach", "python", "teststomach")
ear.addCommand("to the right", "python", "totheright")
ear.addCommand("to the left", "python", "totheleft")
ear.addCommand("turn to the right side", "python", "turnrightside")
ear.addCommand("turn to the left side", "python", "turnleftside")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","ya","yeah", "yes please", "yes of course")
ear.addNegations("no","wrong","nope","nah","no thank you", "no thanks")

ear.startListening()

def relax():
  i01.setTorsoSpeed(0.75,0.55,0.75)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.disable()

def fullspeed():
  i01.setTorsoSpeed( 1.0, 1.0, 1.0)
  i01.mouth.speak("All my servos are set to full speed")    

def totheright():
  i01.setTorsoSpeed(0.75,0.55,0.75)
  i01.moveTorso(135,90,90)
  sleep(3)
  i01.disable()

def totheleft():
  i01.setTorsoSpeed(0.75,0.55,0.75)
  i01.moveTorso(45,90,90)
  sleep(3)
  i01.disable()

def turnrightside():
  i01.setTorsoSpeed(0.75,0.55,0.75)
  i01.moveTorso(90,45,90)
  sleep(3)
  i01.disable()

def turnleftside():
  i01.setTorsoSpeed(0.75,0.55,0.75)
  i01.moveTorso(90,135,90)
  sleep(3)
  i01.disable()          

def teststomach():
  i01.setTorsoSpeed(0.75,0.55,0.75)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.moveTorso(45,90,90)
  sleep(4)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.moveTorso(135,90,90)
  sleep(4)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.moveTorso(90,45,90)
  sleep(3)
  i01.moveTorso(90,135,90)
  sleep(3)
  i01.moveTorso(90,90,45)
  sleep(3)
  i01.moveTorso(90,90,135)
  sleep(3)
  i01.disable()
