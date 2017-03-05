# ##############################################################################
# 								ROBOT SLEEP MODE
# ##############################################################################

###############################################################################
# check if robot can sleep or wakeup
# only based on pir at this time
###############################################################################


def sleepModeWakeUp():
	global RobotIsSleeping
	
	if RobotIsStarted:
		
		ImageDisplay.exitFS()
		ImageDisplay.closeAll()
		if LoadingPicture:r=ImageDisplay.displayFullScreen(RuningFolder+'/system/pictures/loading_1024-600.jpg',1)
		
		if PlayCurstomSoundIfDetection:AudioPlayer.playFile(RuningFolder+'/system/sounds/Notifications/'+random.choice(os.listdir(RuningFolder+'/system/sounds/Notifications')),False)
		#optional switchon nervoboard
		switchOnAllNervo()
		#head up
		if isHeadActivated:
			head.neck.setVelocity(50)
			head.neck.rest()
	else:
		
		if EarInterpretEngine=="chatbot":
			
			if str(chatBot.getPredicate("default","firstinit"))=="unknown" or str(chatBot.getPredicate("default","firstinit"))=="started":
				chatBot.setPredicate("default","topic","default")
				chatBot.getResponse("FIRST_INIT")
			else:
				chatBot.getResponse("WAKE_UP")
		else:
			talkEvent(lang_ready)
	#ear activation

	
	RobotIsSleeping=0
	#restart pir poling
	if isPirActivated:
		PirControlerArduino.enablePin(PirPin,1)
	

def sleepModeSleep():
	
	global RobotIsSleeping
	ImageDisplay.exitFS()
	ImageDisplay.closeAll()
		
	#display sleeping robot on screen
	r=ImageDisplay.displayFullScreen(RuningFolder+'/system/pictures/sleeping_1024-600.jpg',1)
	#head down
	if isHeadActivated:
		head.neck.setVelocity(50)
		head.neck.moveTo(180)
	#stop ear service
	
	sleep(5)
	#optional switchoff nervoboard
	switchOffAllNervo()
	sleep(10)
	RobotIsSleeping=1
	#restart pir poling
	if isPirActivated:
		PirControlerArduino.enablePin(PirPin,1)




