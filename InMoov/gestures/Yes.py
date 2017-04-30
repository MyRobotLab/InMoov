def Yes(data):
  global MoveHeadRandom
  MoveHeadRandom=0
  if IsInmoovArduino==1:
    #i01.attach()
    i01.setHeadSpeed(0.3, 0.3)
    i01.moveHead(130,90)
    sleep(0.5)
    i01.moveHead(50,93)
    sleep(0.5)
    i01.moveHead(130,90)
    sleep(0.5)
  #Light(0,1,1)
  if IsInmoovArduino==1:
    i01.moveHead(60,91)
    sleep(0.5)
    i01.moveHead(120,88)
  if IsInmoovArduino==1:
    i01.moveHead(70,90)
    sleep(0.5)
    i01.moveHead(95,90)
  sleep(0.5)
  #Light(1,1,1)
  if IsInmoovArduino==1:
    i01.moveHead(90,90)
  if IsInmoovArduino==1:
    i01.head.jaw.rest()