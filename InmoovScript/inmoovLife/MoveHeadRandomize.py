def MoveHeadRandomize():
	if MoveHeadRandom==1:
		if isHeadActivated:
			i01.head.attach()
			i01.setHeadVelocity(11,11)
			i01.moveHead(random.randint(70,100), random.randint(60,90))
		if isRollNeckActivated:
			rollneck.attach()
			rollneck.setVelocity(11)
			rollneck.moveTo(random.randint(50,130))
	

MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(random.randint(600,1200))

def MoveHead(timedata):
	MoveHeadRandomize()
	MoveHeadTimer.setInterval(random.randint(5000,20000))

def MoveHeadStopped():
	if MoveHeadRandom==1:
		if isHeadActivated:
			i01.moveHead(90, 90)
		if isRollNeckActivated:
			rollneck.moveTo(90)

def MoveHeadStart():
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	
