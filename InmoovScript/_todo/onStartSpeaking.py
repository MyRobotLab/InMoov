def onStartSpeaking(text):

	#sleep(0.2)
	print "Start speaking debug"
	global Ispeak
	Ispeak=1
	WebkitSpeechRecognitionFix.stopClock()
	global MoveHeadRandom
	if 'non' in text or 'no' in text:
		No('no')
		MoveHeadRandom=0
		#print("no detected")
	if 'oui' in text or 'yes' in text:
		Yes('yes')
		#print("yes detected")
		MoveHeadRandom=0
	if MoveHeadRandom==1:
		MoveHeadTimer.startClock()
	try:
		ear.stopListening()
	except: 
		pass
	global TimeNoSpeak
	TimeNoSpeak="OFF"
	VieAleatoire.stopClock()