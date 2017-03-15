IneedUpdate=0
def CheckVersion():
	remoteVersion=Parse("https://raw.githubusercontent.com/MyRobotLab/inmoov/master/InmoovScript/system/updater/inmoovOsVersion.ini")
	
	if str(remoteVersion) == str(version) or str(remoteVersion)=='':
		return False
	else:
		print "need update"
		return True
		
def updateMe():
	if IneedUpdate:
		talkBlocking(lang_newVersionDownloadStart)

def dontUpdateMe():
	if IneedUpdate:
		IneedUpdate=0
		talkBlocking(lang_newVersionNoUpdate)
		
		

if CheckVersion():

		
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
	