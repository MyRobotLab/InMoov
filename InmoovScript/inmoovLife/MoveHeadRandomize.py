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
      head.neck.setAcceleration(20)
      head.rothead.setAcceleration(20)
      head.rothead.enableAutoDisable(0)
      head.neck.enableAutoDisable(0)
      head.rollNeck.enableAutoDisable(0)
      head.rollNeck.setAcceleration(20)
  else:
    MoveHeadTimer.stopClock()
    
def MoveHeadStop():
  
  if RobotCanMoveHeadWhileSpeaking:
    if isHeadActivated:
      head.rothead.enableAutoDisable(1)
      head.neck.enableAutoDisable(1)
      head.rollNeck.enableAutoDisable(1)
      i01.head.rest()
    
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")  
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")