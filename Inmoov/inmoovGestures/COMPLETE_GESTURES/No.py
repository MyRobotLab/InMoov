def No(data):
  global MoveHeadRandom
  MoveHeadRandom=0
  # WE MOVE THE ROTHEAD OR PISTONMOD
  if IsInmoovArduino==1:
    if random.randint(0,1)==1:
      #i01.attach()
      i01.setHeadSpeed(0.3, 0.3)
      i01.moveHead(80,130)
      sleep(0.5)
      i01.moveHead(80,50)
      sleep(0.5)
      i01.moveHead(81,130)
      sleep(0.5)
      i01.moveHead(79,50)
      sleep(0.5)
      i01.moveHead(83,130)
      sleep(1)
      i01.moveHead(80,90)
      i01.head.jaw.rest()
    else:
      rollneck.setSpeed(0.3)
      rollneck.moveTo(50)
      sleep(0.5)
      rollneck.moveTo(120)
      sleep(1)
      rollneck.moveTo(90)
      i01.head.jaw.rest()