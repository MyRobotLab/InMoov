# ##############################################################################
#            *** FROM InMoov3.minimalHead.py ***
# ##############################################################################

def lookleftside():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,160)

def lookrightside():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,20)

def lookinmiddle():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,90)
  
def lookup():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60)
  i01.moveHead(175,90)

def lookdown():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60)
  i01.moveHead(10,90)  
  
def tiltHeadLeftSide():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(85,90,0)
  
def tiltHeadRightSide():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(85,90,180)
