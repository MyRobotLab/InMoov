def MoveBodyRandomize():
	if MoveBodyRandom==1:
		i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
		i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
		i01.setArmSpeed("right", 0.5, 0.5, 0.5, 0.5)
		i01.setArmSpeed("left", 0.5, 0.5, 0.5, 0.5)
		i01.setHeadSpeed(0.5, 0.5)
		rollneck.setSpeed(0.5)
		i01.setTorsoSpeed(0.5, 0.35, 0.5)
		i01.moveHead(random.randint(70,100), random.randint(60,90))
		rollneck.moveTo(random.randint(50,130))
		i01.moveArm("left",random.randint(0,6),random.randint(78,90),random.randint(20,28),random.randint(12,17))
		i01.moveArm("right",random.randint(0,6),random.randint(78,90),random.randint(20,28),random.randint(12,17))
		i01.moveHand("left",random.randint(50,92),random.randint(28,130),random.randint(28,100),random.randint(28,110),random.randint(28,110),random.randint(20,40))
		i01.moveHand("right",random.randint(50,92),random.randint(28,130),random.randint(28,110),random.randint(28,110),random.randint(28,110),random.randint(140,175))
		i01.moveTorso(random.randint(85,95),random.randint(85,95),random.randint(85,95))
	

MoveBodyTimer = Runtime.start("MoveBodyTimer","Clock")
MoveBodyTimer.setInterval(random.randint(600,1200))

def MoveBody(timedata):
   MoveBodyRandomize()
MoveBodyTimer.setInterval(random.randint(5000,20000))

def MoveBodyStopped():
	if MoveBodyRandom==1:
		MoveBodyTimer.addListener("pulse", python.name, "MoveBody")
		MoveBodyTimer.addListener("clockStopped", python.name, "MoveBodyStopped")

def MoveBodyStart():
	MoveBodyRandomize()
	
MoveBodyTimer.addListener("pulse", python.name, "MoveBody")
MoveBodyTimer.addListener("clockStopped", python.name, "MoveBodyStopped")		
MoveBodyTimer.addListener("clockStarted", python.name, "MoveBodyStart")	
