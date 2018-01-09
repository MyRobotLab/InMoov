def No():
  # WE MOVE THE ROTHEAD OR ROLLNECK
  if isHeadActivated==1:
    i01.startedGesture()
    i01.setHeadVelocity(40,40,40)
    
    if random.randint(0,1)==1:
      i01.moveHeadBlocking(80,130)
      i01.moveHeadBlocking(80,50)
      i01.moveHeadBlocking(83,130)
      i01.moveHeadBlocking(80,90)
    else:
      rollneck.moveToBlocking(50)
      rollneck.moveToBlocking(120)
      rollneck.moveToBlocking(90)
    i01.finishedGesture()