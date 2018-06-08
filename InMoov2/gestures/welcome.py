
def welcome():
  sleep(1)
  inMoov.setHandVelocity("left", 19, 19, 19, 19, 19, 19)
  inMoov.setHandVelocity("right", 19, 36, 19, 19, 19, 19)
  inMoov.setArmVelocity("left", 19, 19, 19, 19)
  inMoov.setArmVelocity("right", 19, 19, 19, 19)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.moveHead(80,90)
  inMoov.moveArm("left",26,105,30,25)
  inMoov.moveArm("right",37,124,30,27)
  inMoov.moveHand("left",2,2,2,2,2,90)
  inMoov.moveHand("right",2,2,2,2,2,90)
  sleep(1)
  inMoov.mouth.speakBlocking("Welcome to the inmoov nation")
  #inMoov.mouth.speakBlocking(u"Добро пожаловать в страну Инмоов")
  sleep(1)


