def Powerglove():
  # WE CONNECT THE POWER GLOVE TO THE SENSOR SHIELD
  if isRightHandActivated==1:
    inMoov.startedGesture()
    inMoov.setRightHandVelocity(80,80,80,80,80,80)
    
    #TO BE CONTINUED
    
    
    inMoov.finishedGesture()
  
