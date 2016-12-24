# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################


GUIService.dockPanel("python")
python.attachPythonConsole()
print "MRL version : ",runtime.getVersion()[-4:]
print "Inmoov version : ",version
print "Starting..."
DEBUG=0
#we import libraries
execfile(RuningFolder+'/system/Import_Libraries.py')

#we import global vars
execfile(RuningFolder+'/system/Import_Vars.py')


RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"

#we load personal parameters
execfile(RuningFolder+'/system/ConfigParser.py')





#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in os.listdir(RuningFolder+'services'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'services/'+filename)

#we include some error control
execfile(RuningFolder+'system/Errors.py')

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
	
# We do a checkup of arduinos and mrlcomm
if 'right' in globals():
	RightPortIsConnected=CheckArduinos(right,MyRightPort)
	
if 'left' in globals():
	LeftPortIsConnected=CheckArduinos(left,MyLeftPort)	


#we launch Inmoov Skeleton
for filename in os.listdir(RuningFolder+'inmoovSkeleton'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovSkeleton/'+filename)


ear.startListening()
#we detach whole i01 servos after 2 seconds
attachDetachThread(i01,2)

#we start some timers
WebkitSpeachReconitionFix.startClock()

#debug
