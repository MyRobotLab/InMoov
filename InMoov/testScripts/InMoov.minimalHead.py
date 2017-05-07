#file : InMoov.minimalHead.py
#MRL version above 1.0.2000
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the skeleton.config
# although this script is very short you can still
# do voice control of a InMoov head
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Change to the port that you use
leftPort = "COM9"
rightPort = "COM7"

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
right = Runtime.createAndStart("i01.right", "Arduino")
right.connect(rightPort)
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
head = Runtime.create("i01.head","InMoovHead")
eyelids = Runtime.create("i01.eyelids", "InMoovEyelids")
##############
# tweaking defaults settings of right hand
# Velocity
head.jaw.setMaxVelocity(-1)
head.eyeY.setMaxVelocity(-1)
head.eyeX.setMaxVelocity(-1)
head.neck.setMaxVelocity(-1)
head.rothead.setMaxVelocity(-1)
head.rollNeck.setMaxVelocity(-1)
eyelids.eyelidleft.setMaxVelocity(-1)
eyelids.eyelidright.setMaxVelocity(-1)
# Mapping
head.jaw.map(0,180,55,95)
head.eyeY.map(0,180,85,110)
head.eyeX.map(0,180,75,120)
head.neck.map(0,180,75,128)
head.rothead.map(0,180,60,130)
head.rollNeck.map(0,180,65,125)
eyelids.eyelidleft.map(0,180,55,135)
eyelids.eyelidright.map(0,180,55,135)
# Rest position
head.jaw.setRest(0)
head.eyeY.setRest(90)
head.eyeX.setRest(90)
head.neck.setRest(90)
head.rothead.setRest(90)
head.rollNeck.setRest(90)
eyelids.eyelidleft.setRest(90)
eyelids.eyelidright.setRest(90)
#################
i01 = Runtime.start("i01","InMoov")
################# 
i01.startHead(leftPort)
i01.startEyelids(rightPort)
#################
#We attach these three parts to the right Arduino
i01.head.rollNeck.attach(right,12)
i01.eyelids.eyelidleft.attach(right,22)
i01.eyelids.eyelidright.attach(right,24)
#################
i01.head.enableAutoDisable(False)
i01.head.enableAutoEnable(True)
#################
i01.startEyesTracking(leftPort,22,24)
i01.startHeadTracking(leftPort,12,13)
i01.startMouthControl(leftPort)
i01.mouthControl.setmouth(0,80)
############################################################
#to tweak the default PID values
i01.eyesTracking.pid.setPID("eyeX",12.0,1.0,0.1)
i01.eyesTracking.pid.setPID("eyeY",12.0,1.0,0.1)
i01.headTracking.pid.setPID("rothead",5.0,1.0,0.1)
i01.headTracking.pid.setPID("neck",5.0,1.0,0.1)
#################
# verbal commands
ear = i01.ear
 
ear.addCommand("rest", "i01.head", "rest")#hardcoded gesture
ear.addCommand("full speed", "python", "fullspeed")
ear.addCommand("relax", "python", "relax")

ear.addCommand("attach everything", "i01", "enable")
ear.addCommand("disconnect everything", "i01", "disable")
ear.addCommand("attach head", "i01.head", "enable")
ear.addCommand("disconnect head", "i01.head", "disable")
ear.addCommand("attach eyelids", "i01.eyelids", "enable")
ear.addCommand("disconnect eyelids", "i01.eyelids", "disable")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.addCommand("search humans", "python", "trackHumans")
ear.addCommand("quit search", "python", "stopTracking")
ear.addCommand("track", "python", "trackPoint")
ear.addCommand("freeze track", "python", "stopTracking")
ear.addCommand("face recognizer", "python", "facerecognizer")

ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look in the middle", "python", "lookinmiddle")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def relax():
  i01.setHeadVelocity(30, 30, 30)
  i01.moveHead(90,90,90)
  i01.mouth.speak("I am relaxed")
  sleep(5)
  i01.disable()

def fullspeed():
  i01.setHeadVelocity(-1, -1, -1, -1, -1, -1)
  i01.setEyelidsVelocity(-1, -1)
  i01.mouth.speak("All my servos are set to full speed")  

def lookrightside():
  i01.setHeadVelocity(40, 40, 40)
  i01.moveHead(80,40,20)
  sleep(3)
  i01.disable()

def lookleftside():
  i01.setHeadVelocity(40, 40, 40)
  i01.moveHead(80,140,160)
  sleep(3)
  i01.disable()

def lookinmiddle():
  i01.setHeadVelocity(40, 40, 40)
  i01.moveHead(90,90,90)
  sleep(3)
  i01.disable()

def trackHumans():
  i01.headTracking.faceDetect()
  i01.eyesTracking.faceDetect()
  i01.mouth.speak("I start my tracking")
  fullspeed()

def trackPoint():
  i01.headTracking.startLKTracking()
  i01.eyesTracking.startLKTracking()
  i01.mouth.speak("I am tracking the point")
  fullspeed()

def stopTracking():
  i01.headTracking.stopTracking()
  i01.eyesTracking.stopTracking()
  i01.mouth.speak("I am stoping my tracking")

def facerecognizer():
  i01.mouth.speak("I need to be trained with at least two faces")
  sleep(3)
  if (i01.eyesTracking.getOpenCV().capturing):
    i01.headTracking.stopTracking()
    i01.eyesTracking.stopTracking()
    i01.opencv.addFilter("PyramidDown")
    i01.opencv.setDisplayFilter("FaceRecognizer")
    fr=i01.opencv.addFilter("FaceRecognizer")
    fr.train()

  else:
    i01.opencv.capture()
    i01.opencv.addFilter("PyramidDown")
    i01.opencv.setDisplayFilter("FaceRecognizer")
    fr=i01.opencv.addFilter("FaceRecognizer")
    fr.train()
  i01.disable()
