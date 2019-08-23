def No():
  # WE MOVE THE ROTHEAD OR ROLLNECK
  if isHeadActivated==1:
    i01.startedGesture()
    i01.setHeadVelocity(80,80,80)  
    if random.randint(0,1)==1:
      i01.moveHead(80,130)
      sleep(0.3)
      i01.moveHead(80,50)
      sleep(0.3)
      i01.moveHead(83,130)
      sleep(0.3)
      i01.moveHead(80,90)
    else:
      i01.head.rollNeck.moveTo(50)
      sleep(0.4)
      i01.head.rollNeck.moveTo(120)
      sleep(0.4)
      i01.head.rollNeck.moveTo(90)
    i01.finishedGesture()
