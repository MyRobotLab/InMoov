def rest():
	if RightPortIsConnected:
		i01.moveHand("right",0,0,0,0,0)
		i01.moveArm("right",5,90,30,10)
	
	
	if LeftPortIsConnected:
		i01.moveHand("left",0,0,0,0,0)
		i01.moveArm("left",5,90,30,10)