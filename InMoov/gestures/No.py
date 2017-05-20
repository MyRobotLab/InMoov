def No():
  i01.disableRobotCanMoveHeadRandom(30)
  # WE MOVE THE ROTHEAD OR PISTONMOD
  if isHeadActivated==1:
    i01.setHeadVelocity(40,40,40)
    
    if random.randint(0,1)==1:
      #i01.attach()
      i01.moveHead(80,130)
      sleep(0.5)
      i01.moveHead(80,50)
      sleep(0.8)
      i01.moveHead(81,130)
      sleep(0.8)
      i01.moveHead(79,50)
      sleep(0.8)
      i01.moveHead(83,130)
      sleep(1)
      i01.moveHead(80,90)
    else:
      rollneck.moveTo(50)
      sleep(1)
      rollneck.moveTo(120)
      sleep(1)
      rollneck.moveTo(90)
  
