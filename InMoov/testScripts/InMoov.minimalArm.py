#file : InMoov.minimalArm.py

#MRL version above 1.0.2000
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the skeleton.config
# although this script is very short you can still
# do voice control of a right Arm or a left Arm or both together
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work


#leftPort = "COM20"  #modify port according to your board
rightPort = "COM7" #modify port according to your board

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
#left = Runtime.createAndStart("i01.left", "Arduino")
#left.connect(leftPort)
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
i01.startMouth()
##############
#leftArm = Runtime.create("i01.leftArm","InMoovArm")
#tweak defaults LeftArm
#Velocity
#leftArm.bicep.setMaxVelocity(-1)
#leftArm.rotate.setMaxVelocity(-1)
#leftArm.shoulder.setMaxVelocity(-1)
#leftArm.omoplate.setMaxVelocity(-1)
#Mapping
#leftArm.bicep.map(0,90,45,96)
#leftArm.rotate.map(40,180,60,142)
#leftArm.shoulder.map(0,180,44,150)
#leftArm.omoplate.map(10,80,42,80)
#Rest position
#leftArm.bicep.setRest(5)
#leftArm.rotate.setRest(90)
#leftArm.shoulder.setRest(30)
#leftArm.omoplate.setRest(10)
#################
rightArm = Runtime.create("i01.rightArm","InMoovArm")
# tweak default RightArm
#Velocity
rightArm.bicep.setMaxVelocity(-1)
rightArm.rotate.setMaxVelocity(-1)
rightArm.shoulder.setMaxVelocity(-1)
rightArm.omoplate.setMaxVelocity(-1)
#Mapping
rightArm.bicep.map(0,90,45,96)
rightArm.rotate.map(40,180,75,130)
rightArm.shoulder.map(0,180,44,150)
rightArm.omoplate.map(10,80,43,80)
#Rest position
rightArm.bicep.setRest(5)
rightArm.rotate.setRest(90)
rightArm.shoulder.setRest(30)
rightArm.omoplate.setRest(10)
#################
i01 = Runtime.start("i01","InMoov")
################# 
#i01.startLeftArm(leftPort)
i01.startRightArm(rightPort)
#################
#i01.leftArm.enableAutoDisable(True)
#i01.leftArm.enableAutoEnable(True)
i01.rightArm.enableAutoDisable(False)
i01.rightArm.enableAutoEnable(True)
#################
# verbal commands
ear = i01.ear

ear.addCommand("attach everything", "i01", "enable")
ear.addCommand("disconnect everything", "i01", "disable")
ear.addCommand("attach left arm", "i01.leftArm", "enable")
ear.addCommand("disconnect left arm", "i01.leftArm", "disable")
ear.addCommand("attach right arm", "i01.rightArm", "enable")
ear.addCommand("disconnect right arm", "i01.rightArm", "disable")
ear.addCommand("rest", "python", "rest")
ear.addCommand("full speed", "python", "fullspeed")
ear.addCommand("arms front", "python", "armsFront")
ear.addCommand("da vinci", "python", "daVinci")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","ya","yeah", "yes please", "yes of course")
ear.addNegations("no","wrong","nope","nah","no thank you", "no thanks")

############

ear.startListening()

def rest():
  #i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  #i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.mouth.speak("Ok, taking rest")
  sleep(4)
  i01.disable()

def fullspeed():
  #i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.mouth.speak("All my servos are set to full speed")  

def armsFront():
  #i01.moveArm("left",13,115,100,20)
  i01.moveArm("right",13,115,100,20)
  i01.mouth.speak("Moving my arms in front of me")
  sleep(4)
  i01.disable()

def daVinci():
  #i01.setArmSpeed("left", 0.80, 0.80, 0.80, 0.80)
  i01.setArmSpeed("right", 0.80, 0.80, 0.80, 0.80)
  #i01.moveArm("left",0,118,29,74)
  i01.moveArm("right",0,118,29,74)
  i01.mouth.speak("This is the pose of Leonardo Da Vinci")
  sleep(10)
  #i01.setArmSpeed("left", 0.70, 0.70, 0.70, 0.70)
  i01.setArmSpeed("right", 0.70, 0.70, 0.70, 0.70)
  #i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  sleep(4)
  i01.disable()

