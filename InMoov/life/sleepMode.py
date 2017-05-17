# ##############################################################################
#                 ROBOT SLEEP MODE
# ##############################################################################

###############################################################################
# check if robot can sleep or wakeup
# only based on pir at this time
###############################################################################


def sleepModeWakeUp():
  ear.setAutoListen(True)
  if isPirActivated:
      PirControlerArduino.enablePin(PirPin,1)
      SleepTimer.startClock()
  
  if RobotIsStarted:
    
    ImageDisplay.exitFS()
    ImageDisplay.closeAll()
    
    if LoadingPicture:r=ImageDisplay.displayFullScreen(RuningFolder+'/system/pictures/loading_1024-600.jpg',1)
    
    rdmWakup=random.randint(1,3)
    if rdmWakup==1:
      sleep(0.5)
      if PlayCurstomSoundIfDetection:AudioPlayer.playFile(RuningFolder+'/system/sounds/Notifications/'+random.choice(os.listdir(RuningFolder+'/system/sounds/Notifications')),False)
    elif rdmWakup==2:
      PlayNeopixelAnimation("Larson Scanner", 255, 255, 0, 1)
      sleep(2)
      StopNeopixelAnimation()
    else: welcomeMessage()
    #optional switchon nervoboard
    switchOnAllNervo()
    #head up
    if isHeadActivated:
      head.neck.setVelocity(50)
      head.neck.rest()
  else:
    if talkToInmoovFrQueue("MRLALIVE")=="OK":talkEvent(lang_OsSynced)
    welcomeMessage()
  
  global RobotIsSleeping
  RobotIsSleeping=0
  StopNeopixelAnimation()



def sleepModeSleep():
  ear.setAutoListen(False)
  global RobotIsSleeping
  ImageDisplay.exitFS()
  ImageDisplay.closeAll()
    
  #display sleeping robot on screen
  r=ImageDisplay.displayFullScreen(RuningFolder+'/system/pictures/sleeping_1024-600.jpg',1)
  #head down
  if isHeadActivated:
    head.neck.setVelocity(60)
    head.neck.moveTo(10)
    sleep(5)
    i01.disable()
  switchOffAllNervo()
  StopNeopixelAnimation()
  sleep(2)
  PlayNeopixelAnimation("Color Wipe", 10, 12, 12, 50)
  
  RobotIsSleeping=1
  #restart pir poling
  if isPirActivated:
    PirControlerArduino.enablePin(PirPin,1)
    
    
def welcomeMessage():
  global RobotIsStarted
  
  if isChatbotActivated:
    if str(chatBot.getPredicate("default","firstinit"))=="unknown" or str(chatBot.getPredicate("default","firstinit"))=="started":
      chatBot.setPredicate("default","topic","default")
      chatBot.getResponse("FIRST_INIT")
    else:
      chatBot.getResponse("WAKE_UP")
  else:
    talk(lang_ready)
  RobotIsStarted=1
    
def humanDetected():    
  global SleepTimerAction    
  SleepTimerAction="restart"
  SleepTimer.stopClock()
  
  
  
def SleepTimerRoutine(timedata):
  global pirTimerStarted
  print "started"    
  if pirTimerStarted and not RobotIsSleeping:
    PlayNeopixelAnimation("Larson Scanner", 0, 0, 255, 1)
    PirControlerArduino.disablePin(PirPin)
    #sleep function to call
    SleepTimer.stopClock()
    
    sleepModeSleep()
  pirTimerStarted=1
  
def SleepTimerRoutineStopped():
  global SleepTimerAction
  global pirTimerStarted
  pirTimerStarted=0
  if SleepTimerAction=="restart":
    SleepTimerAction=""
    SleepTimer.startClock()
    

#pir starting  
if isPirActivated:
  SleepTimer = Runtime.createAndStart("SleepTimer","Clock")
  SleepTimer.addListener("pulse", python.name, "SleepTimerRoutine")
  SleepTimer.addListener("clockStopped", python.name, "SleepTimerRoutineStopped")
  SleepTimer.setInterval(HumanPresenceTimeout)
  PirControlerArduino.addListener("publishPinArray","python","publishPinPir")
  PirControlerArduino.enablePin(PirPin,1)




