def studyball():
  i01.startedGesture()
  ##keepball():
  sleep(3)
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setArmSpeed("right", 31.0, 43.0, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadSpeed(50.0, 50.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,20)
  i01.moveArm("right",54,77,45,10)
  i01.moveHand("left",0,50,40,20,20,90)
  i01.moveTorso(90,90,90)
  if rightHandSensorActivated:
    rightHandSensorON()
    sleep(1.5)
    rightThumbPressure=1 # Pressure range between 0-3
    rightIndexPressure=1
    rightMajeurePressure=1
    i01.moveHand("right",110,160,150,40,40,11)
    sleep(3)
    rightHandSensorOFF()
  else:
    i01.moveHand("right",110,110,120,40,40,11)
  sleep(2)
  ##approachlefthand():
  i01.setHandSpeed("left", 100.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 6.0, 6.0, 6.0, 6.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(20,84)
  i01.moveArm("left",65,52,62,23)
  i01.moveArm("right",60,50,35,10)
  i01.moveHand("left",0,0,0,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
  ##uselefthand():
  i01.setHandSpeed("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 6.0, 6.0, 6.0, 6.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(10,80)
  i01.moveArm("left",80,45,59,23)
  i01.moveArm("right",75,40,50,10)
  if leftHandSensorActivated:
    leftHandSensorON()
    sleep(1.5)
    leftThumbPressure=1 # Pressure range between 0-3
    leftIndexPressure=1
    leftMajeurePressure=1
    i01.moveHand("left",180,0,40,10,10,0)
    sleep(2)
    leftHandSensorOFF()
  else:
    i01.moveHand("left",180,0,40,10,10,0)
  sleep(4)
  ##more():
  i01.setHandSpeed("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  i01.setArmSpeed("left", 43.0, 36, 43.0, 59)
  i01.setArmSpeed("right", 31.0, 22.0, 22.0, 22.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(13,80)
  i01.moveArm("left",80,45,59,23)
  i01.moveArm("right",75,40,50,10)
  if leftHandSensorActivated:
    leftHandSensorON()
    sleep(1.5)
    leftThumbPressure=1 # Pressure range between 0-3
    leftIndexPressure=1
    leftMajeurePressure=1
    #i01.leftHand.thumb.moveTo(180)
    #i01.leftHand.index.moveTo(180)
    #i01.leftHand.majeure.moveTo(180)
    i01.moveHand("left",180,180,10,10,10,0)
    sleep(2)
    leftHandSensorOFF()
  else:
    i01.moveHand("left",180,148,140,10,10,0)
  i01.moveHand("right",60,120,120,40,40,11)
  sleep(3)
  ##handdown():
  i01.setHandSpeed("left", 31.0, 31.0, 31.0, 31.0, 31.0, 31.0)
  i01.setHandSpeed("right", 26.00, 26.00, 26.00, 26.00, 26.00, 100.0)
  i01.setArmSpeed("right", 43.0, 22.0, 22.0, 22.0)
  i01.moveHead(18,75)
  i01.moveArm("left",75,45,59,23)
  i01.moveArm("right",50,40,50,10)
  i01.moveHand("left",180,148,140,10,10,0)
  i01.moveHand("right",40,60,40,0,0,11)
  sleep(2)
  #isitaball():
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 36.0, 36.0, 50)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 59, 59, 43.0)
  i01.setArmSpeed("left", 59, 100.0, 50, 43.0)
  i01.setHeadSpeed(22.0, 31.0)
  i01.moveHead(70,82,40)
  i01.moveArm("left",80,59,95,15)
  i01.moveArm("right",12,74,33,15)
  if leftHandSensorActivated:
    leftHandSensorON()
    sleep(1.5)
    leftThumbPressure=1 # Pressure range between 0-3
    leftIndexPressure=1
    leftMajeurePressure=1
    #i01.leftHand.thumb.moveTo(180)
    #i01.leftHand.index.moveTo(180)
    #i01.leftHand.majeure.moveTo(180)
    i01.moveHand("left",180,180,180,180,180,164)
    sleep(2)
    leftHandSensorOFF()
  else:
    i01.moveHand("left",180,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  i01.mouth.speakBlocking("I will start tracking the object")
  #i01.mouth.speakBlocking(u"Я начну отслеживать объект")
  fullspeed()
  #trackPoint()
  sleep(2)
  #i01.mouth.speakBlocking("you need to set the point")
  #i01.mouth.speakBlocking(u"Вам нужно установить точку")
  #Now we use Use Yolo
  i01.mouth.speakBlocking("I think it is a ball")
  #i01.mouth.speakBlocking(u"Я думаю, что это мяч")
  i01.finishedGesture()
