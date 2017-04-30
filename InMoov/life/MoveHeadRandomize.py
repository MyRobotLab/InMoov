# ##############################################################################
#            *** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):

  if RobotCanMoveHeadWhileSpeaking:
    #redefine next loop
    MoveHeadTimer.setInterval(random.randint(200,1000))
    if isHeadActivated:
      i01.setHeadVelocity(random.randint(5,25),random.randint(5,25),random.randint(5,25))
      #wait servo last move
      if not head.rothead.isMoving():head.rothead.moveTo(random.uniform(60,120))
      if not head.neck.isMoving():head.neck.moveTo(random.uniform(60,120))
      if not head.rollNeck.isMoving():head.rollNeck.moveTo(random.uniform(60,120))
    else:
      MoveHeadTimer.stopClock()
  
#initial function
def MoveHeadStart():
  print "MoveHeadStart"

  if RobotCanMoveHeadWhileSpeaking:
    if isHeadActivated:
      head.setAcceleration(20)
      head.enableAutoDisable(0) 
  else:
    MoveHeadTimer.stopClock()
    
def MoveHeadStop():
  
  if RobotCanMoveHeadWhileSpeaking:
    if isHeadActivated:
      head.rothead.enableAutoDisable(rotheadEnableAutoDisable)
      head.neck.enableAutoDisable(neckEnableAutoDisable)
      head.rollNeck.enableAutoDisable(rollneckEnableAutoDisable)
      
      i01.head.rest()
    
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")  
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")