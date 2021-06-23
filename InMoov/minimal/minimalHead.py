# ##############################################################################
#            *** FROM InMoov3.minimalHead.py ***
# ##############################################################################

def lookleftside():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60)
  i01.moveHeadBlocking(85,160)
  i01.finishedGesture()
  
def lookrightside():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60)
  i01.moveHeadBlocking(85,20)
  i01.finishedGesture()

def lookinmiddle():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60)
  i01.moveHeadBlocking(85,90)
  i01.finishedGesture()
  
def lookup():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60)
  i01.moveHeadBlocking(175,90)
  i01.finishedGesture()

def lookdown():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60)
  i01.moveHeadBlocking(10,90) 
  i01.finishedGesture()  
  
def tiltHeadLeftSide():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60, 60)
  i01.moveHeadBlocking(85,90,0)
  i01.finishedGesture()
  
def tiltHeadRightSide():
  i01.startedGesture()
  i01.setHeadSpeed(60, 60, 60)
  i01.moveHeadBlocking(85,90,180)
  i01.finishedGesture()