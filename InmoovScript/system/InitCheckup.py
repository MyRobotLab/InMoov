# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

################################
# INIT.0
################################

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
#startup sound
AudioPlayer = Runtime.createAndStart("AudioPlayer", "AudioFile")
if StartupSound:AudioPlayer.playFile(RuningFolder+'/system/sounds/startupsound.mp3', False)


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



################################
# INIT.4 - configuration and system health
################################
#mrl version check
if int(runtime.getVersion()[-4:])<int(mrlCompatible):errorSpokenFunc('MrlNeedUpdate')

	
################################
# INIT.5 - skeleton loading
################################
#we launch Inmoov Skeleton
for filename in os.listdir(RuningFolder+'inmoovSkeleton'):		
	if os.path.splitext(filename)[1] == ".py":execfile(RuningFolder+'inmoovSkeleton/'+filename.encode('utf8'))

################################
# INIT.6 - ear.addcmmands
################################
#if chatbot loaded we do not load ear.addcommands
if EarInterpretEngine!="chatbot":
	for root, subdirs, files in os.walk(RuningFolder+'inmoovVocal/ear.addCommand'):
		for name in files:
			if name.split(".")[-1] == "py":
				execfile(os.path.join(root, name).encode('utf8'))
				if DEBUG==1:print "debug  ear.addcmmands : ",os.path.join(root, name)		


################################
# INIT.7- inmoov loading
################################
	
#we launch Inmoov Gestures
for root, subdirs, files in os.walk(RuningFolder+'inmoovGestures'):
	for name in files:
		if name.split(".")[-1] == "py":
			execfile(os.path.join(root, name))
			if DEBUG==1:print "debug inmoovGestures : ",os.path.join(root, name)
		
#we launch Inmoov life
for root, subdirs, files in os.walk(RuningFolder+'inmoovLife'):
	for name in sorted(files):
		if name.split(".")[-1] == "py":
			execfile(os.path.join(root, name))
			if DEBUG==1:print "debug inmoovLife : ",os.path.join(root, name)

#create the custom script, only if not exist
if not os.path.isfile(RuningFolder+'inmoovCustom/Inmoov_custom.py'):shutil.move(RuningFolder+'inmoovCustom/Inmoov_custom.py.default',RuningFolder+'inmoovCustom/Inmoov_custom.py')


################################
# INIT.8 - inmoov APPS - TODO
################################

#we launch Inmoov APPS - GAMES
for root, subdirs, files in os.walk(RuningFolder+'inmoovAPPS'):
	for name in files:
		if name.split(".")[-1] == "py":
			execfile(os.path.join(root, name))
			if DEBUG==1:print "debug inmoovAPPS : ",os.path.join(root, name)

# here we go !
ImageDisplay.exitFS()
ImageDisplay.closeAll()
#sleep(5)
#detachAll()
talkEvent(lang_ready)
WebkitSpeechRecognitionFix.startClock()
RobotIsStarted=1




