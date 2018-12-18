def howdoyoudo():
  global helvar
  if helvar < 1:
    helvar += 1
  elif helvar == 1:
    i01.moveArm("left",43,88,22,10)
    i01.moveArm("right",20,90,30,10)
    i01.moveHand("left",0,0,0,0,0,119)
    i01.moveHand("right",0,0,0,0,0,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar == 2:
    i01.moveArm("left",30,83,22,10)
    i01.moveArm("right",40,85,30,10)
    i01.moveHand("left",130,180,180,180,180,119)
    i01.moveHand("right",130,180,180,180,180,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar >= 3:
    helvar=4
    unhappy()
    sleep(4)
    relax()    
  i01.chatBot.setPredicate("parameterHowDoYouDo",str(helvar))