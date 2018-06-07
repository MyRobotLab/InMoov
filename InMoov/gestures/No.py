def No():
  # WE MOVE THE ROTHEAD OR ROLLNECK
  if isHeadActivated==1:
    inMoov.startedGesture()
    inMoov.setHeadVelocity(40,40,40)
    
    if random.randint(0,1)==1:
      inMoov.moveHeadBlocking(80,130)
      inMoov.moveHeadBlocking(80,50)
      inMoov.moveHeadBlocking(83,130)
      inMoov.moveHeadBlocking(80,90)
    else:
      rollneck.moveToBlocking(50)
      rollneck.moveToBlocking(120)
      rollneck.moveToBlocking(90)
    inMoov.finishedGesture()