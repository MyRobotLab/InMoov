#this is a test file about gestures integration
# THIS IS A CLONE OF DAVINCI

def gestureTEST():
	
	inMoov.leftHand.attach()
	inMoov.rightHand.attach()
	inMoov.leftArm.attach()
	inMoov.rightArm.attach()
	inMoov.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
	inMoov.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
	inMoov.setArmSpeed("left", 0.75, 0.75, 0.75, 0.75)
	inMoov.setArmSpeed("right", 0.75, 0.75, 0.75, 0.75)
	inMoov.setHeadSpeed( 0.75, 0.75)
	inMoov.moveHead(80,90)
	inMoov.moveArm("left",0,118,13,74)
	inMoov.moveArm("right",0,118,29,74)
	inMoov.moveHand("left",50,28,30,10,10,47)
	inMoov.moveHand("right",10,10,10,10,10,137)
