# -- coding: utf-8 --
def givetheglass():
  i01.startedGesture()
  sleep(2)
  i01.setHandVelocity("left", 19, 19, 19, 19, 19, 19)
  i01.setHandVelocity("right", 19, 36, 19, 19, 19, 19)
  i01.setArmVelocity("left", 19, -1, 19, 19)
  i01.setArmVelocity("right", 19, 19, 19, 19)
  i01.setHeadVelocity(22.0, 22.0)
  i01.moveHead(84,79)
  i01.moveArm("left",77,75,45,17)
  i01.moveArm("right",21,80,77,10)
  i01.moveHand("left",109,138,180,164,180,60)
  i01.moveHand("right",102,86,105,105,143,133)
  i01.mouth.speakBlocking("Hello please take the glass")
  #i01.mouth.speakBlocking(u"Привет, пожалуйста, возьмите стакан")
  sleep(1)
  i01.finishedGesture()

