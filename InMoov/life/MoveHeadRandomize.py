# ##############################################################################
#            *** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):

  if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    #redefine next loop
    MoveHeadTimer.setInterval(random.randint(200,1000))
    if isHeadActivated:
      i01.setHeadVelocity(random.randint(8,25),random.randint(8,25),random.randint(8,25))
      #wait servo last move
      if not head.rothead.isMoving():head.rothead.moveTo(random.uniform(60,120))
      if not head.neck.isMoving():head.neck.moveTo(random.uniform(60,120))
      if not head.rollNeck.isMoving():head.rollNeck.moveTo(random.uniform(60,120))
    else:
      MoveHeadTimer.stopClock()
  
#initial function
def MoveHeadStart():
  
  print "moveheadstart"
  if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
      #head.setAcceleration(20)
      head.enableAutoDisable(0) 
    else:
      MoveHeadTimer.stopClock()
    
def MoveHeadStop():
  
  if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
      head.rothead.enableAutoDisable(rotheadEnableAutoDisable)
      head.neck.enableAutoDisable(neckEnableAutoDisable)
      head.rollNeck.enableAutoDisable(rollneckEnableAutoDisable)
      i01.setHeadVelocity(25,25,25)
      i01.head.rest()
      i01.setHeadVelocity(40,40,40)
      
    
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")  
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")