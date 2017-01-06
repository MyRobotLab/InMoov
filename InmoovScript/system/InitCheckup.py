# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################


GUIService.dockPanel("python")
print "MRL version : ",runtime.getVersion()[-4:]
print "Inmoov version : ",version
print "Starting..."
DEBUG=0


#we import libraries
execfile(RuningFolder+'/system/Import_Libraries.py')
RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"

#we import global vars
execfile(RuningFolder+'/system/Robot_Satus_GlobalsVars.py')

#we load personal parameters
execfile(RuningFolder+'/system/ConfigParser.py')

#we load personal parameters
execfile(RuningFolder+'/system/Errors.py')

#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in os.listdir(RuningFolder+'services'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'services/'+filename)

		
if boot_green:		
	PlayNeopixelAnimation("Flash Random", 0, 255, 0, 1)


#we launch Inmoov Skeleton
for filename in os.listdir(RuningFolder+'inmoovSkeleton'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovSkeleton/'+filename)
		


				
#mrl version check
if int(runtime.getVersion()[-4:])<int(mrlCompatible):
	errorSpokenFunc('MrlNeedUpdate',0)

#we start raw Inmoov ear and mouth service
i01.startMouth()

#set user language
setRobotLanguage()

#check and update marytts voices	
checkAndDownloadVoice()

#set CustomVoice
setCustomVoice()
	
#we launch Inmoov Gestures
for filename in os.listdir(RuningFolder+'inmoovGestures'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovGestures/'+filename)
		print filename
		
#we launch Inmoov inmoovVocal commands
for filename in os.listdir(RuningFolder+'inmoovVocal/ear.addCommand'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovVocal/ear.addCommand/'+filename)
		print filename
		
#we launch Inmoov life
for filename in os.listdir(RuningFolder+'inmoovLife'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovLife/'+filename)
		
ear.startListening()

#create the custom script, only if not exist
if not os.path.isfile(RuningFolder+'inmoovCustom/Inmoov_custom.py'):
		shutil.move(RuningFolder+'inmoovCustom/Inmoov_custom.py.default',RuningFolder+'inmoovCustom/Inmoov_custom.py')




