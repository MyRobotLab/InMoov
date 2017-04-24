def onEndSpeaking(text):
	global IcanStartToEar
	global IcanEarOnlyKnowsWords
	print "End speaking debug"
	global MoveHeadRandom
	MoveHeadTimer.stopClock()
	global Ispeak
	Ispeak=0
	global TimeNoSpeak
	VieAleatoire.startClock()
	TimeNoSpeak="OFF"
	#Light(0,0,0)
	if IsInmoovArduino==1:
		i01.moveHead(90,90,90,90,90)
	MoveHeadRandom=1
	
	if IcanStartToEar==1:
		try:
			ear.startListening()
		except: 
			pass
	WebkitSpeechRecognitionFix.startClock()
	IcanStartToEar=1
	StopListenTimer.stopClock()
	IcanEarOnlyKnowsWords=-1
	StopListenTimer.startClock()
    #sleep(0.2)