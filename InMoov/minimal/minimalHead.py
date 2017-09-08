# ##############################################################################
#            *** FROM InMoov3.minimalHead.py ***
# ##############################################################################

def lookleftside():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,160)
  i01.finishedGesture()
  
def lookrightside():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,20)
  i01.finishedGesture()

def lookinmiddle():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60)
  i01.moveHead(85,90)
  i01.finishedGesture()
  
def lookup():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60)
  i01.moveHead(175,90)
  i01.finishedGesture()

def lookdown():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60)
  i01.moveHead(10,90) 
  i01.finishedGesture()  
  
def tiltHeadLeftSide():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(85,90,0)
  i01.finishedGesture()
  
def tiltHeadRightSide():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(85,90,180)
  i01.finishedGesture()