# ##############################################################################
#            *** ROBOT MOVE THE EYES ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveEyesTimer = Runtime.start("MoveEyesTimer","Clock")

def MoveEyes(timedata):
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    #redefine next loop
    MoveEyesTimer.setInterval(random.randint(600,2000))
    if isHeadActivated:
      head.eyeX.setVelocity(random.randint(10,90))
      head.eyeY.setVelocity(random.randint(10,90))
      #wait servo last move
      if not head.eyeX.isMoving():head.eyeX.moveTo(random.uniform(20,160))
      if not head.eyeY.isMoving():head.eyeY.moveTo(random.uniform(20,160))
    else:
      MoveEyesTimer.stopClock()
  
#initial function
def MoveEyesStart():
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    if not isHeadActivated:MoveEyesTimer.stopClock()
    
def MoveEyesStop():
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
      head.eyeX.rest()
      head.eyeY.rest()
      head.eyeX.setVelocity(-1)
      head.eyeY.setVelocity(-1)
    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")