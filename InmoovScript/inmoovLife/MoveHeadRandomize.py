# ##############################################################################
#						*** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################

	
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

#main function called by the timer
def MoveHeadRandomize():
	MoveHeadTimer.setInterval(random.randint(500,1500))
	if MoveHeadRandom==1 and RobotCanMoveHeadWhileSpeaking:
			
		if isHeadActivated:
			i01.setHeadVelocity(random.randint(20,40),random.randint(20,40))
			if random.randint(0,3)>0:
				i01.head.neck.moveTo(random.uniform(30,140))
			if random.randint(0,3)>0:
				i01.head.rothead.moveTo(random.uniform(60,120))
		if isRollNeckActivated:
			rollneck.setVelocity(random.randint(20,40))
			if random.randint(0,3)>0:
				rollneck.moveTo(random.uniform(20,150))
	


def MoveHead(timedata):
	MoveHeadRandomize()
	
#function called if timer is stopped
def MoveHeadStopped():
	if MoveHeadRandom==1 and RobotCanMoveHeadWhileSpeaking:
		
		if isHeadActivated:
			i01.head.neck.setVelocity(200)
			i01.head.rothead.setVelocity(200)
			i01.moveHead(neckRest, rotheadRest)
			sleep(1)
			i01.head.rothead.detach()
			i01.head.neck.detach()
		if isRollNeckActivated:
			rollneck.setVelocity(200)
			rollneck.moveTo(RollNeckRestPosition)
			sleep(1)
			rollneck.detach()

#initial function
def MoveHeadStart():
	
	if MoveHeadRandom==1 and RobotCanMoveHeadWhileSpeaking:
		if isHeadActivated:
			
			i01.head.neck.attach()
			i01.head.rothead.attach()
			i01.head.neck.setAcceleration(20)
			i01.head.rothead.setAcceleration(20)
		if isRollNeckActivated:
			rollneck.setVelocity(20)
			rollneck.attach()
			rollneck.setAcceleration(20)
		MoveHeadRandomize()
	else:
		MoveHeadTimer.stopClock()
		
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	

#MoveHeadTimer.startClock()
