def rest():
   global MoveBodyRandom
   MoveBodyRandom=0
   global MoveHeadRandom
   MoveHeadRandom=0
   i01.setHeadSpeed(1.0, 1.0)
   i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
   i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
   i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
   i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
   i01.setTorsoSpeed(1.0, 1.0, 1.0)
   i01.moveHead(90,90,90,90,43)
   rollneck.moveTo(90)
   i01.moveArm("left",5,90,30,10)
   i01.moveArm("right",5,90,30,12)
   i01.moveHand("left",2,2,2,2,2,90)
   i01.moveHand("right",2,2,2,2,2,90)
   i01.moveTorso(90,90,90)

