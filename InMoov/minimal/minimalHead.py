# ##############################################################################
#            *** FROM InMoov3.minimalHead.py ***
# ##############################################################################

def lookleftside():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,160)

def lookrightside():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,20)

def lookinmiddle():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,90)
  
def tiltHeadLeftSide():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(85,90,0)
  
def tiltHeadRightSide():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(85,90,180)