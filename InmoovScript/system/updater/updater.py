def CheckVersion():
	RetourServer=Parse("https://raw.githubusercontent.com/MyRobotLab/inmoov/master/InmoovScript/system/updater/inmoovOsVersion.ini")
	#print str(RetourServer)+' '+str(version)
	if str(RetourServer)==str(version):
		print "software is OK"
		#chatBot.getResponse("IAMUPDATED")
	else:
		chatBot.getResponse("INEEDUPDATE")
		sleep(3)
		
def updateMe():
	if IneedUpdate:
		talkBlocking(lang_newVersionDownloadStart)

def dontUpdateMe():
	if IneedUpdate:
		IneedUpdate=0
		talkBlocking(lang_newVersionNoUpdate)
		

IneedUpdate=0

if IneedUpdate:

		
	ear.addCommand(lang_newVersionYes, "python", "updateMe")
	ear.addCommand(lang_newVersionNo, "python", "dontUpdateMe")
	talkBlocking(lang_newVersion)
	
	
#hard coded forced patch v 0.3.5
	try:
		os.remove(RuningFolder+"inmoovGestures/COMPLETE_GESTURES/lookinmiddle.py")
		os.remove(RuningFolder+"inmoovGestures/COMPLETE_GESTURES/lookleftside.py")
		os.remove(RuningFolder+"inmoovGestures/COMPLETE_GESTURES/lookrightside.py")
	except:
		pass
	