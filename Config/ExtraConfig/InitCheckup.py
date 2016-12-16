# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

#subconsciousMouth is an always worky english voice used to diagnostic
subconsciousMouth = Runtime.createAndStart("subconsciousMouth", "MarySpeech")
subconsciousMouth.setVoice("cmu-slt-hsmm")

#we import libraries
execfile('Config/ExtraConfig/Import_Libraries.py')
#we include some error control
execfile(u'Config/ExtraConfig/Errors.py')
#this is functions that tweak the mouth
execfile(u'Config/ExtraConfig/MouthFunctions.py')



MyLanguage=MyLanguage.lower()
ear = i01.ear








	
if MyLanguage!="en":
	try:
		mouth.setLanguage(MyLanguage)
		
		ear.setLanguage(MyLanguage)
	except:
		errorSpokenFunc('MyLanguage')
		pass



try:
	mouth.setVoice(voiceType)
except:
	errorSpokenFunc('voiceType')
	pass
	

# We do a checkup of arduinos and mrlcomm
if ScriptType=="FingerStarter":
	right = Runtime.createAndStart("i01.right", "Arduino")
	RightPortIsConnected=right.connect(MyRightPort)
	RightPortIsConnected=right.isConnected()
		
	if not RightPortIsConnected:
		errorSpokenFunc('RightPortIsConnected')