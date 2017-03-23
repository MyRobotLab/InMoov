# ##############################################################################
#						*** FROM InMoov3.minimalHead.py ***
# ##############################################################################

def lookleftside():
	global RobotCanMoveHeadWhileSpeaking
	RobotCanMoveHeadWhileSpeaking=0
	i01.setHeadVelocity(60, 60)
	i01.moveHead(85,160)

def lookrightside():
	global RobotCanMoveHeadWhileSpeaking
	RobotCanMoveHeadWhileSpeaking=0
	i01.setHeadVelocity(60, 60)
	i01.moveHead(85,20)

def lookinmiddle():
	global RobotCanMoveHeadWhileSpeaking
	RobotCanMoveHeadWhileSpeaking=0
	i01.setHeadVelocity(60, 60)
	i01.moveHead(85,90)
	
#opencv

def trackPoint():
	global RobotCanMoveHeadWhileSpeaking
	RobotCanMoveHeadWhileSpeaking=0
	i01.headTracking.startLKTracking()
	i01.eyesTracking.startLKTracking()
	i01.setHeadVelocity(-1, -1)
	 
def trackHumans():
	global RobotCanMoveHeadWhileSpeaking
	RobotCanMoveHeadWhileSpeaking=0
	i01.headTracking.faceDetect()
	#i01.eyesTracking.faceDetect()
	i01.setHeadVelocity(-1, -1)