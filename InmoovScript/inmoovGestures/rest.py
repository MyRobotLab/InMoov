# ##############################################################################
# 				ROBOT REST POSITIONS ( minimal )
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
# 				ROBOT REST POSITIONS ( full )
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

		
		
# ##############################################################################
# 				full speed
# ##############################################################################
		
def fullspeed():
	if isRightHandActivated:
		i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
			
	if isLeftHandActivated:
		i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
			
	if isRightArmActivated:
		i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
		
	if isLeftArmActivated:
		i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
	
	if isHeadActivated:
		i01.setHeadSpeed(1.0, 1.0)
	
	if isTorsoActivated:
		i01.setTorsoSpeed(1.0, 1.0, 1.0)
			
	if isRollNeckActivated:
		rollneck.setSpeed(1.0)
		
def detachAll():
	i01.detach()
	if isRollNeckActivated:
		rollneck.detach()
		
   #TODO RANDOM GESTURE
   #global MoveBodyRandom
   #MoveBodyRandom=0
   #global MoveHeadRandom
   #MoveHeadRandom=0