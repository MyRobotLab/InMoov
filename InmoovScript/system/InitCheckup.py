# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

#subconsciousMouth is an always worky english voice used to diagnostic
subconsciousMouth = Runtime.createAndStart("subconsciousMouth", "MarySpeech")
subconsciousMouth.setVoice("cmu-slt-hsmm")

#we import libraries
execfile('InmoovScript/system/Import_Libraries.py')
#we include some error control
execfile('InmoovScript/system/Errors.py')
#this is functions that tweak the mouth
execfile(u'InmoovScript/services/Mouth.py')



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