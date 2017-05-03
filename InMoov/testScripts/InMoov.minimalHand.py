#file : InMoov.minimalHand.py
#MRL version above 1.0.2000
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the skeleton.config
# although this script is very short you can still
# do voice control of a right hand or finger box
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Change to the port that you use
rightPort = "COM7"

#to tweak the default voice
Voice="cmu-bdl-hsmm" #Male US voice 
#Voice="cmu-slt-hsmm" #Default female for MarySpeech
voiceType = Voice
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
mouth.installComponentsAcceptLicense(Voice)
mouth.setVoice(voiceType)
#i01.mouth.installComponentsAcceptLicense(Voice)
##############
# starting parts
i01 = Runtime.createAndStart("i01", "InMoov")
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
i01.startRightHand(rightPort)
# tweaking defaults settings of right hand
i01.rightHand.thumb.setMaxVelocity(-1)
i01.rightHand.index.setMaxVelocity(-1)
i01.rightHand.majeure.setMaxVelocity(-1)
i01.rightHand.ringFinger.setMaxVelocity(-1)
i01.rightHand.pinky.setMaxVelocity(-1)
i01.rightHand.wrist.setMaxVelocity(-1)
i01.rightHand.thumb.map(0,180,64,135)
i01.rightHand.index.map(0,180,42,160)
i01.rightHand.majeure.map(0,180,35,165)
i01.rightHand.ringFinger.map(0,180,45,135)
i01.rightHand.pinky.map(0,180,45,130)
i01.rightHand.wrist.map(0,180,30,135)
#################
i01.rightHand.enableAutoDisable(True)
i01.rightHand.enableAutoEnable(True)
#################
# verbal commands
ear = i01.ear

ear.addCommand("attach your right hand", "i01.rightHand", "enable")
ear.addCommand("disconnect your right hand", "i01.rightHand", "disable")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()


def handopen():
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.moveHand("right",0,0,0,0,0,0)
  i01.mouth.speak("ok I open my hand")

def handclose():
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.moveHand("right",180,180,180,180,180,180)
  i01.mouth.speak("a nice and wide open hand that is")
