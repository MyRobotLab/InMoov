def CheckVersion():
	global RobotneedUpdate
	remoteVersion=Parse("https://raw.githubusercontent.com/MyRobotLab/inmoov/master/InmoovScript/system/updater/inmoovOsVersion.ini")
	print version,remoteVersion
	if str(remoteVersion) == str(version) or str(remoteVersion)=='':
		return False
	else:
		print "need update"
		RobotneedUpdate=1
		return True
		
def updateMe():
	if RobotneedUpdate:
		#not implemented yet
		#talkBlocking(lang_newVersionDownloadStart)
		sleepModeWakeUp()

def dontUpdateMe():
	
	if RobotneedUpdate:
		talkBlocking(lang_newVersionNoUpdate)
		sleepModeWakeUp()
		
		



		
ear.addCommand(lang_newVersionYes, "python", "updateMe")
ear.addCommand(lang_newVersionNo, "python", "dontUpdateMe")
	
	
	
	
#hard coded forced patch v 0.3.5
try:
	os.remove(RuningFolder+"inmoovGestures/COMPLETE_GESTURES/lookinmiddle.py")
	os.remove(RuningFolder+"inmoovGestures/COMPLETE_GESTURES/lookleftside.py")
	os.remove(RuningFolder+"inmoovGestures/COMPLETE_GESTURES/lookrightside.py")
except:
	pass
	#clean up .default.config
for root, subdirs, files in os.walk(RuningFolder):
	for name in files:
		if name.split(".")[-1] == "default":
			os.remove(os.path.join(root, name))
			if DEBUG==1:print "removed .default : ",os.path.join(root, name)

	