def loop():  
  inMoov.startedGesture()
  for x in range(500):
    print "this is magic"
    sleep(1)
  inMoov.finishedGesture()