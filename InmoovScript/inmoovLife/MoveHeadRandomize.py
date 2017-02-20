# ##############################################################################
#						*** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################

#main function called by the timer
def MoveHeadRandomize():
	MoveHeadTimer.setInterval(random.randint(600,1500))
	if MoveHeadRandom==1:
			
		if isHeadActivated:
			i01.setHeadVelocity(random.randint(10,50),random.randint(10,50))
			if random.randint(0,2)>0:
				i01.head.neck.moveTo(random.uniform(30,160))
			if random.randint(0,2)>0:
				i01.head.rothead.moveTo(random.uniform(30,150))
		if isRollNeckActivated:
			rollneck.setVelocity(random.randint(10,50))
			if random.randint(0,2)>0:
				rollneck.moveTo(random.uniform(20,150))
	
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):
	MoveHeadRandomize()
	
#function called if timer is stopped
def MoveHeadStopped():
	if MoveHeadRandom==1:
		if isHeadActivated:
			i01.moveHead(neckRest, rotheadRest)
			sleep(1)
			i01.head.rothead.detach()
			i01.head.neck.detach()
		if isRollNeckActivated:
			rollneck.moveTo(RollNeckRestPosition)
			sleep(1)
			rollneck.detach()

#initial function
def MoveHeadStart():
	if isHeadActivated:
		i01.setHeadVelocity(20,20)
		i01.head.rothead.setAcceleration(10)
		i01.head.neck.setAcceleration(10)
		i01.head.neck.attach()
		i01.head.rothead.attach()
	if isRollNeckActivated:
		rollneck.setAcceleration(15)
		rollneck.attach(RollNeckArduino, RollNeckPin, RollNeckRestPosition, 10)
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	

#MoveHeadTimer.startClock()
