# ##############################################################################
#         ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest(optionalDetach=0):
  #fullspeed()
  if isRightHandActivated:
    i01.rightHand.attach()
    i01.rightHand.rest()
  
  if isLeftHandActivated:
    i01.leftHand.attach()
    i01.leftHand.rest()
  
  if isRightArmActivated:
    i01.rightArm.attach()
    i01.rightArm.rest()
  
  if isLeftArmActivated:
    i01.leftArm.attach()
    i01.leftArm.rest()
    
# ##############################################################################
#         ROBOT REST POSITIONS ( full )
# ##############################################################################    
  
  if isHeadActivated:
    i01.head.attach()
    i01.head.rest()
  
  if isTorsoActivated:
    i01.torso.attach()
    i01.torso.rest()
  
  if isRollNeckActivated:
    rollneck.attach()
    rollneck.rest()