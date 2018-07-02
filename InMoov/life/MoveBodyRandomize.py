# ##############################################################################
#            *** ROBOT MOVE THE BODY ***
# ##############################################################################
  
MoveBodyTimer = Runtime.start("MoveBodyTimer","Clock")

def MoveBody(timedata):

  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping:
  
    if (ScriptType=="Full" or ScriptType=="Virtual"):
      #redefine next loop
      MoveBodyTimer.setInterval(random.randint(1000,5000))
   
      if isLeftHandActivated:
        i01.setHandVelocity("left", random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25))
        if not leftHand.thumb.isMoving():leftHand.thumb.moveTo(random.uniform(10,160))
        if not leftHand.index.isMoving():leftHand.index.moveTo(random.uniform(10,60))
        if not leftHand.majeure.isMoving():leftHand.majeure.moveTo(random.uniform(10,60))
        if not leftHand.ringFinger.isMoving():leftHand.ringFinger.moveTo(random.uniform(10,60))
        if not leftHand.pinky.isMoving():leftHand.pinky.moveTo(random.uniform(10,60))
        if not leftHand.wrist.isMoving():leftHand.wrist.moveTo(random.uniform(10,80))
      if isRightHandActivated:
        i01.setHandVelocity("right", random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25))
        if not rightHand.thumb.isMoving():rightHand.thumb.moveTo(random.uniform(10,160))
        if not rightHand.index.isMoving():rightHand.index.moveTo(random.uniform(10,60))
        if not rightHand.majeure.isMoving():rightHand.majeure.moveTo(random.uniform(10,90))
        if not rightHand.ringFinger.isMoving():rightHand.ringFinger.moveTo(random.uniform(10,60))
        if not rightHand.pinky.isMoving():rightHand.pinky.moveTo(random.uniform(10,60))
        if not rightHand.wrist.isMoving():rightHand.wrist.moveTo(random.uniform(100,170))
      if isLeftArmActivated:
        i01.setArmVelocity("left", random.randint(2,5), random.randint(2,5), random.randint(2,5), random.randint(2,5))
        if not leftArm.bicep.isMoving():leftArm.bicep.moveTo(random.uniform(0,10))
        if not leftArm.shoulder.isMoving():leftArm.shoulder.moveTo(random.uniform(15,35))
        if not leftArm.rotate.isMoving():leftArm.rotate.moveTo(random.uniform(85,95))
        if not leftArm.omoplate.isMoving():leftArm.omoplate.moveTo(random.uniform(10,20))
      if isRightArmActivated:
        i01.setArmVelocity("right", random.randint(2,5), random.randint(2,5), random.randint(2,5), random.randint(2,5))
        if not rightArm.bicep.isMoving():rightArm.bicep.moveTo(random.uniform(0,10))
        if not rightArm.shoulder.isMoving():rightArm.shoulder.moveTo(random.uniform(15,35))
        if not rightArm.rotate.isMoving():rightArm.rotate.moveTo(random.uniform(85,95))
        if not rightArm.omoplate.isMoving():rightArm.omoplate.moveTo(random.uniform(10,20))
      if isTorsoActivated:
        i01.setTorsoVelocity(random.randint(2,5), random.randint(2,5), random.randint(2,5))
        if not torso.topStom.isMoving():torso.topStom.moveTo(random.uniform(85,95))
        if not torso.midStom.isMoving():torso.midStom.moveTo(random.uniform(88,93))

    else:
      MoveBodyTimer.stopClock()
  
#initial function
def MoveBodyStart():
  
  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping:
  
    if (ScriptType=="Full" or ScriptType=="Virtual"):
      print "MoveBodyStart"
        #head.setAcceleration(20)
        #head.enableAutoDisable(0) 
    else:
      MoveBodyTimer.stopClock()
    
def MoveBodyStopped():
  
  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping:
  
    if (ScriptType=="Full" or ScriptType=="Virtual"):
      print "MoveBodyStopped"
      i01.halfSpeed()
      i01.rest()

MoveBodyTimer.addListener("pulse", python.name, "MoveBody")
MoveBodyTimer.addListener("clockStarted", python.name, "MoveBodyStart")  
MoveBodyTimer.addListener("clockStopped", python.name, "MoveBodyStopped")
