# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

GUIService.dockPanel("python")
print "MRL version : ",runtime.getVersion()[-4:]
print "Inmoov version : ",version
print "Starting..."
DEBUG=0

################################
# INIT.1 - system dependencies
################################

# libraries import
execfile(RuningFolder+'/system/Import_Libraries.py')
# common functions
execfile(RuningFolder+'/system/Import_Functions.py')


RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"
# global vars import
execfile(RuningFolder+'/system/Robot_Satus_GlobalsVars.py')



################################
# INIT.2 - low level
################################

# we load personal parameters
execfile(RuningFolder+'/system/ConfigParser.py')

i01.startEar()
ear = i01.ear
ear.pauseListening()

# vocal errors
execfile(RuningFolder+'/system/Errors.py'.encode('utf8'))

# language pack
execfile(RuningFolder+'/system/languagePack.py')





################################
# INIT.3 - services call
################################
#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in sorted(os.listdir(RuningFolder+'services')):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'services/'+filename.encode('utf8'))
		print filename
if boot_green:		
	PlayNeopixelAnimation("Flash Random", 0, 255, 0, 1)


################################
# INIT.4 - configuration and system health
################################
#mrl version check
if int(runtime.getVersion()[-4:])<int(mrlCompatible):
	errorSpokenFunc('MrlNeedUpdate')

	
################################
# INIT.5 - skeleton loading
################################
#we launch Inmoov Skeleton
for filename in os.listdir(RuningFolder+'inmoovSkeleton'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovSkeleton/'+filename.encode('utf8'))



################################
# INIT.6 - inmoov loading
################################
	
#we launch Inmoov Gestures
for filename in os.listdir(RuningFolder+'inmoovGestures'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovGestures/'+filename.encode('utf8'))
		
#we launch Inmoov life
for filename in os.listdir(RuningFolder+'inmoovLife'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovLife/'+filename.encode('utf8'))

#create the custom script, only if not exist
if not os.path.isfile(RuningFolder+'inmoovCustom/Inmoov_custom.py'):
		shutil.move(RuningFolder+'inmoovCustom/Inmoov_custom.py.default',RuningFolder+'inmoovCustom/Inmoov_custom.py')


################################
# INIT.7 - inmoov APPS
################################

#we launch Inmoov APPS - GAMES
for root, subdirs, files in os.walk(RuningFolder+'inmoovAPPS'):
	print files
	for name in files:
		if name.split(".")[-1] == "py":
			execfile(os.path.join(root, name))
			if DEBUG==1:
				print "debug inmoovAPPS : ",os.path.join(root, name)

# here we go !
talkEvent(lang_startingEar)
#ImageDisplay.exitFS()
#ImageDisplay.closeAll()
talkEvent(lang_ready)
WebkitSpeechRecognitionFix.startClock()

RobotIsStarted=1




