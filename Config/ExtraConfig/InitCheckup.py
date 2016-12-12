# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

#we import libraries
execfile('Config/ExtraConfig/Import_Libraries.py')
#we include some error control
execfile(u'Config/ExtraConfig/Errors.py')
execfile(u'Config/ExtraConfig/MouthFunctions.py')



try:
	mouth.setVoice(voiceType)
except:
	errorSpokenFunc('VoiceError')
	pass



# We do a checkup of arduinos and mrlcomm
if ScriptType=="FingerStarter":
	right = Runtime.createAndStart("i01.right", "Arduino")
	RightPortIsConencted=right.connect(MyRightPort)
	RightPortIsConencted=right.isConnected()
		
	if not RightPortIsConencted:
		errorSpokenFunc('RightPortIsConencted')