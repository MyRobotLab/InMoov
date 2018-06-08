# ##############################################################################
#         ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest():
  fullspeed()
  if isRightHandActivated:
    inMoov.rightHand.rest()
  
  if isLeftHandActivated:
    inMoov.leftHand.rest()
  
  if isRightArmActivated:
    inMoov.rightArm.rest()
  
  if isLeftArmActivated:
    inMoov.leftArm.rest()
    
# ##############################################################################
#         ROBOT REST POSITIONS ( full )
# ##############################################################################    
  
  if isHeadActivated:
    inMoov.head.rest()
  
  if isTorsoActivated:
    inMoov.torso.rest()
    
  if isEyeLidsActivated:
    inMoov.eyelids.rest()