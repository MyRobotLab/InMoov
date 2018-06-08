
def givetheglass():
  inMoov.startedGesture()
  sleep(2)
  inMoov.setHandVelocity("left", 19, 19, 19, 19, 19, 19)
  inMoov.setHandVelocity("right", 19, 36, 19, 19, 19, 19)
  inMoov.setArmVelocity("left", 19, -1, 19, 19)
  inMoov.setArmVelocity("right", 19, 19, 19, 19)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.moveHead(84,79)
  inMoov.moveArm("left",77,75,45,17)
  inMoov.moveArm("right",21,80,77,10)
  inMoov.moveHand("left",109,138,180,164,180,60)
  inMoov.moveHand("right",102,86,105,105,143,133)
  inMoov.mouth.speakBlocking("Hello please take the glass")
  #inMoov.mouth.speakBlocking(u"Привет, пожалуйста, возьмите стакан")
  sleep(1)
  inMoov.finishedGesture()

