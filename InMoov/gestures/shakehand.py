global noHumanLeft
noHumanLeft=0
global getCloserLeft
getCloserLeft=0
global distanceLeftOK
distanceLeftOK=0

global noHumanRight
noHumanRight=0
global getCloserRight
getCloserRight=0
global distanceRightOK
distanceRightOK=0

def shakehand():
  rest()
  i01.startedGesture()
  ##move arm and hand
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setArmSpeed("right", 31.0, 43.0, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadSpeed(100.0, 100.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",50,40,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(3)
   ##optional, detect if there is a human ( waiting finger sensor, we use ultrasonic distance as test )
  if ultraSonicRightActivated:
    distanceRight=200
    timeoutRight=0
    timeoutRightGetCloser=0
    while (not distanceRight or distanceRight > 100):
      timeoutRight+=1
      timeoutRightGetCloser+=1
      distanceRight=i01.getUltrasonicRightDistance()
      print "==Ultrasonic=distanceRight=Distance:", distanceRight
      if timeoutRight > 20:
        global noHumanRight
        noHumanRight=1
        noHuman()
        break  
      sleep(0.5)
      # ask GET CLOSER
      if timeoutRightGetCloser> 10:
        global getCloserRight
        getCloserRight=1
        getCloser()   
      sleep(1)
    # great, human detected
    if distanceRight<=90:
      global distanceRightOK
      distanceRightOK=1
      goShake()
  
  elif ultraSonicLeftActivated:
    distanceLeft=200
    timeoutLeft=0
    timeoutLeftGetCloser=0
    while (not distanceLeft or distanceLeft > 100): 
      timeoutLeft+=1
      timeoutLeftGetCloser+=1
      distanceLeft=i01.getUltrasonicLeftDistance()
      print "==Ultrasonic=distanceLeft=Distance:", distanceLeft
      if timeoutLeft > 20:
        global noHumanLeft
        noHumanLeft=1
        noHuman()
        break  
      sleep(0.5)
      # ask GET CLOSER
      if timeoutLeftGetCloser> 10:
        global getCloserLeft
        getCloserLeft=1
        getCloser()  
      sleep(1)
    # great, human detected
    if distanceLeft<=90:
      global distanceLeftOK
      distanceLeftOK=1
      goShake()
  else:
    if ultraSonicRightActivated==0 and ultraSonicLeftActivated==0:
      sleep(3)
      shakehandAnimation()

def noHuman():
  if noHumanLeft==1 or noHumanRight==1:
    chatBot.getResponse("SYSTEM_SHAKE_HAND_NOHUMAN")
    timeoutRight=0
    timeoutLeft=0
    sleep(2)
    shakehandFinish()

def getCloser():
  if getCloserLeft==1 or getCloserRight==1:
    chatBot.getResponse("SYSTEM_SHAKE_HAND_GET_CLOSER")
    timeoutLeftGetCloser=0
    timeoutRightGetCloser=0
    sleep(2)

def goShake():
  if distanceLeftOK==1 or distanceRightOK==1:
    shakehandAnimation()


def shakehandAnimation():
  ##set hand up
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(100.0, 100.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(90,90)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  i01.moveHand("right",80,70,70,50,50,180)
  sleep(3)
  ##close the hand
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setArmSpeed("right", 31.0, 43.0, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 31.0, 43.0)
  i01.setHeadSpeed(100.0, 100.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  if rightHandSensorActivated:
    rightHandSensorON()
    sleep(1.5)
    rightThumbPressure=1 # Pressure range between 0-3
    rightIndexPressure=1
    rightMajeurePressure=1
    rightRingFingerPressure=1
    rightPinkyPressure=1
    i01.rightHand.moveTo(79,170,160,160,160,180)
    sleep(2)
    rightHandSensorOFF()
  else:
    i01.rightHand.moveTo(79,90,140,130,122,180)
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(31.0, 31.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(70,53)
  sleep(0.2)
  i01.moveHead(39,70)
  sleep(0.2)
  i01.moveHead(70,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(0.5) 
  ##shake hand up
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(43.0, 43.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(80,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,65,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(0.7)
  chatBot.getResponse("SYSTEM_SHAKE_HAND")
  ##shake hand down
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(43.0, 43.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(80,88)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(0.7)
  ##shake hand up
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(43.0, 43.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(80,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,65,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(0.7)
  ##shake hand down
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(43.0, 43.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(80,88)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(0.7)
  ##shake hand up
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(43.0, 43.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(80,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,65,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(0.7)
  ## release hand
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 59, 59, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadSpeed(100.0, 100.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,77)
  i01.moveHand("right",0,0,0,0,0,180)
  i01.moveTorso(95,95,90)
  shakehandFinish()

def shakehandFinish():
  sleep(0.5)
  i01.finishedGesture()
  rest()
  relax()
