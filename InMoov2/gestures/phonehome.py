def phonehome():
  relax()
  inMoov.startedGesture()
  sleep(1)
  inMoov.setHeadVelocity(-1,-1,-1,-1,-1)
  inMoov.setArmVelocity("left",-1.0,-1.0,-1.0,-1.0)
  inMoov.setArmVelocity("right",-1.0,-1.0,-1.0,-1.0)
  inMoov.setHandVelocity("left",-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
  inMoov.setHandVelocity("right",-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
  inMoov.setTorsoVelocity(-1.0,-1.0,-1.0)
  inMoov.moveHead(160,68)
  inMoov.moveArm("left",5,86,30,20)
  inMoov.moveArm("right",86,140,83,80)
  inMoov.moveHand("left",99,140,173,167,130,26)
  inMoov.moveHand("right",135,6,170,145,168,180)
  inMoov.moveTorso(25,80,90)
  sleep(2)
  #inMoov.mouth.speakBlocking("E,T phone the big home of the inmoov nation")
  AudioPlayer.playFile(RuningFolder+'/system/sounds/E,T phone the big home of the inmoov nation.mp3')
  sleep(2)
  inMoov.finishedGesture()
  rest()
  sleep(1)
  relax()
