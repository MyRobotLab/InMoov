# ##############################################################################
#            *** WHOLE ROBOT MOVE RANDOM ***
# ##############################################################################
  
MoveRandomTimer = Runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):

  MoveRandomTimer.setInterval(random.randint(10000,30000))

  if random.randint(0,1)==1:
    if i01.RobotCanMoveEyesRandom:i01.RobotCanMoveEyesRandom=False
    else:
      i01.RobotCanMoveEyesRandom=True
      if not MoveEyesTimer.isClockRunning:MoveEyesTimer.startClock()
    
  if random.randint(0,1)==1:
    if i01.RobotCanMoveBodyRandom:
      i01.RobotCanMoveBodyRandom=False
      i01.RobotCanMoveHeadRandom=False
    else:
      i01.RobotCanMoveBodyRandom=True
      i01.RobotCanMoveHeadRandom=True
      if not MoveBodyTimer.isClockRunning:MoveBodyTimer.startClock()
      if not MoveHeadTimer.isClockRunning:MoveHeadTimer.startClock()

      
  #little pause
  if random.randint(0,4)==4:
    if i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
      i01.RobotCanMoveHeadRandom=False
      i01.RobotCanMoveBodyRandom=False
      relax()
      i01.waitTargetPos()
      #chatBot.getResponse("RANDOM")
  if random.randint(0,3)==3:i01.RobotCanMoveEyesRandom=False

def MoveRandomStart():
  MoveBodyTimer.startClock()
  MoveEyesTimer.startClock()
  MoveHeadTimer.startClock()
    
def MoveRandomStop():
  MoveBodyTimer.stopClock()
  MoveEyesTimer.stopClock()
  MoveHeadTimer.stopClock()
  i01.RobotCanMoveHeadRandom=True
  i01.RobotCanMoveBodyRandom=True
  i01.RobotCanMoveEyesRandom=True
  relax()
  i01.waitTargetPos()    
    
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.addListener("clockStopped", python.name, "MoveRandomStop")
MoveRandomTimer.addListener("clockStarted", python.name, "MoveRandomStart")
