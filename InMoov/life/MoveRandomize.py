# ##############################################################################
#            *** WHOLE ROBOT MOVE RANDOM ***
# ##############################################################################
  
MoveRandomTimer = Runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):

  MoveRandomTimer.setInterval(random.randint(10000,30000))
  
  if random.randint(0,1)==1:
    if i01.RobotCanMoveEyesRandom:
      i01.RobotCanMoveEyesRandom=False
    else:
      i01.RobotCanMoveEyesRandom=True
      if not MoveEyesTimer.isClockRunning:MoveEyesTimer.startClock()
    
  if random.randint(0,1)==1:
    if i01.RobotCanMoveBodyRandom:
      i01.RobotCanMoveBodyRandom=False
    else:
      i01.RobotCanMoveBodyRandom=True
    
  if random.randint(0,1)==1:
    if i01.RobotCanMoveHeadRandom:
      i01.RobotCanMoveHeadRandom=False
    else:
      i01.RobotCanMoveHeadRandom=True
      if not MoveHeadTimer.isClockRunning:MoveHeadTimer.startClock()
      
  if random.randint(0,3)==3:
    i01.disableRobotRandom(20)
    chatBot.getResponse("RANDOM")

def MoveRandomStart():
  MoveBodyTimer.startClock()
  MoveEyesTimer.startClock()
  MoveHeadTimer.startClock()
    
def MoveRandomStop():
  MoveBodyTimer.stopClock()
  MoveEyesTimer.stopClock()
  MoveHeadTimer.stopClock()
      
    
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.addListener("clockStopped", python.name, "MoveRandomStop")
MoveRandomTimer.addListener("clockStarted", python.name, "MoveRandomStart")