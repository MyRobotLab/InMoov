# ##############################################################################
#						*** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
	
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):

	if MoveHeadRandom==1 and RobotCanMoveHeadWhileSpeaking:
		#redefine next loop
		MoveHeadTimer.setInterval(random.randint(200,1000))
		if isHeadActivated:
			i01.setHeadVelocity(random.randint(5,25),random.randint(5,25))
			#wait servo last move
			if not head.rothead.isMoving():head.rothead.moveTo(random.uniform(60,120))
			if not head.neck.isMoving():head.neck.moveTo(random.uniform(60,120))
		if isRollNeckActivated:
			rollneck.setVelocity(random.randint(5,25))
			if not head.neck.isMoving():rollneck.moveTo(random.uniform(60,120))

#initial function
def MoveHeadStart():

	if MoveHeadRandom==1 and RobotCanMoveHeadWhileSpeaking:
		if isHeadActivated:
			head.neck.setAcceleration(20)
			head.rothead.setAcceleration(20)
			head.rothead.enableAutoDetach(0)
			head.neck.enableAutoDetach(0)
		if isRollNeckActivated:
			rollneck.enableAutoDetach(0)
			rollneck.setAcceleration(20)
	else:
		MoveHeadTimer.stopClock()
		
def MoveHeadStop():
	
	if MoveHeadRandom==1 and RobotCanMoveHeadWhileSpeaking:
		if isHeadActivated:
			head.rothead.enableAutoDetach(1)
			head.neck.enableAutoDetach(1)
			i01.setHeadVelocity(200,200)
			i01.head.rest()
		if isRollNeckActivated:
			rollneck.enableAutoDetach(1)
			rollneck.rest()
	else:
		MoveHeadTimer.stopClock()

MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")