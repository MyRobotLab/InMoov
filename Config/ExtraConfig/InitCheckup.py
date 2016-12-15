# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

	
#we import libraries
execfile('Config/ExtraConfig/Import_Libraries.py')
#we include some error control
execfile(u'Config/ExtraConfig/Errors.py')
execfile(u'Config/ExtraConfig/MouthFunctions.py')

defaultSystemVoiceAndLanguage()
MyLanguage=MyLanguage.lower()

ear.setLanguage(MyLanguage)

if MyLanguage!="en":
	try:
		mouth.setLanguage(MyLanguage)
	except:
		errorSpokenFunc('MyLanguage')
		pass

try:
	mouth.setVoice(voiceType)
except:
	mouth.setVoice("cmu-slt-hsmm")
	errorSpokenFunc('voiceType')
	pass
	
ear.setLanguage


	

# We do a checkup of arduinos and mrlcomm
if ScriptType=="FingerStarter":
	right = Runtime.createAndStart("i01.right", "Arduino")
	RightPortIsConnected=right.connect(MyRightPort)
	RightPortIsConnected=right.isConnected()
		
	if not RightPortIsConnected:
		errorSpokenFunc('RightPortIsConnected')