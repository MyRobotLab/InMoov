def MoveHeadRandomize():
	if MoveHeadRandom==1:
		i01.setHeadSpeed(0.5, 0.5)
		rollneck.setSpeed(0.5)
		i01.moveHead(random.randint(70,100), random.randint(60,90))
		rollneck.moveTo(random.randint(50,130))
	

MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(random.randint(600,1200))

def MoveHead(timedata):
   MoveHeadRandomize()
MoveHeadTimer.setInterval(random.randint(5000,20000))

def MoveHeadStopped():
	if MoveHeadRandom==1:
		MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
		MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")

def MoveHeadStart():
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	
