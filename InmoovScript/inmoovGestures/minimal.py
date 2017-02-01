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