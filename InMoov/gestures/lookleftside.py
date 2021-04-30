def lookleftside():
  i01.startedGesture()
  i01.setHeadSpeed(80, 80, 50, 50, 100.0)
  i01.moveHead(90,160,170,90,0,90)
  sleep(1)
  i01.finishedGesture()
  relax()