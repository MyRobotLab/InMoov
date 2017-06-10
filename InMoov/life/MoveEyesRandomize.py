# ##############################################################################
#            *** ROBOT MOVE THE EYES ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveEyesTimer = Runtime.start("MoveEyesTimer","Clock")

def MoveEyes(timedata):
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    #redefine next loop
    MoveEyesTimer.setInterval(random.randint(200,1000))
    if isHeadActivated:
      head.eyeX.setVelocity(random.randint(10,50))
      head.eyeY.setVelocity(random.randint(10,50))
      #wait servo last move
      if not head.eyeX.isMoving():head.eyeX.moveTo(random.uniform(60,120))
      if not head.eyeY.isMoving():head.eyeY.moveTo(random.uniform(60,120))
    else:
      MoveEyesTimer.stopClock()
  
#initial function
def MoveEyesStart():
  print "MoveEyesStart",i01.RobotIsTrackingSomething()

  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
        #head.setAcceleration(20)
      head.eyeX.enableAutoDisable(0)
      head.eyeY.enableAutoDisable(0)
    else:
      MoveEyesTimer.stopClock()
    
def MoveEyesStop():
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
      head.eyeX.enableAutoDisable(eyeXEnableAutoDisable)
      head.eyeY.enableAutoDisable(eyeYEnableAutoDisable)

      head.eyeX.rest()
      head.eyeY.rest()
      head.eyeX.setVelocity(-1)
      head.eyeY.setVelocity(-1)
    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")