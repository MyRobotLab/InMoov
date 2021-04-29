def welcome():
  sleep(1)
  i01.setHandSpeed("left", 19, 19, 19, 19, 19, 19)
  i01.setHandSpeed("right", 19, 36, 19, 19, 19, 19)
  i01.setArmSpeed("left", 19, 19, 19, 19)
  i01.setArmSpeed("right", 19, 19, 19, 19)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(80,90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  sleep(1)
  i01.mouth.speakBlocking("Welcome to the inmoov nation")
  #i01.mouth.speakBlocking(u"Добро пожаловать в страну Инмоов")
  sleep(1)


