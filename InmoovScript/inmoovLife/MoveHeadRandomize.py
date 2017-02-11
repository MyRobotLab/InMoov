# ##############################################################################
#						*** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################

def MoveHeadRandomize():
	MoveHeadTimer.setInterval(random.randint(1000,2000))
	if MoveHeadRandom==1:
			
		if isHeadActivated:
			i01.moveHead(random.randint(50,130), random.randint(70,110))
		if isRollNeckActivated:
			rollneck.moveTo(random.randint(20,150))
	
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):
	MoveHeadRandomize()
	

def MoveHeadStopped():
	if MoveHeadRandom==1:
		if isHeadActivated:
			i01.moveHead(90, 90)
		if isRollNeckActivated:
			rollneck.moveTo(90)

def MoveHeadStart():
	if isHeadActivated:
		i01.setHeadVelocity(20,20)
		head.rothead.setAcceleration(20)
		head.neck.setAcceleration(20)
		i01.head.attach()
	if isRollNeckActivated:
		rollneck.setVelocity(15)
		rollneck.setAcceleration(20)
		rollneck.attach()
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	

#MoveHeadTimer.startClock()
