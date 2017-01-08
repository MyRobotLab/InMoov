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


RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"
# global vars import
execfile(RuningFolder+'/system/Robot_Satus_GlobalsVars.py')



################################
# INIT.2 - low level
################################

# we load personal parameters
execfile(RuningFolder+'/system/ConfigParser.py')

# language pack

languagePack=MyLanguage
languagePackLoaded=1

# we load default english language pack
for filename in os.listdir(RuningFolder+'languagePack/en'):		
		if os.path.splitext(filename)[1] == ".lang":
			execfile(RuningFolder+'languagePack/en/'+filename)

# we try to load user language pack		
try:
	
	for filename in os.listdir(RuningFolder+'languagePack/'+languagePack):		
		if os.path.splitext(filename)[1] == ".lang":
			execfile(RuningFolder+'languagePack/'+languagePack+'/'+filename)
	languagePackLoaded=1
except:
	languagePackLoaded=0
	pass		


# vocal errors
execfile(RuningFolder+'/system/Errors.py')



################################
# INIT.3 - services call
################################
#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in os.listdir(RuningFolder+'services'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'services/'+filename)
if boot_green:		
	PlayNeopixelAnimation("Flash Random", 0, 255, 0, 1)


################################
# INIT.4 - configuration and system health
################################
#mrl version check
if int(runtime.getVersion()[-4:])<int(mrlCompatible):
	errorSpokenFunc('MrlNeedUpdate')
#we start raw Inmoov ear and mouth service
i01.startMouth()
#set user language
setRobotLanguage()

#check and update marytts voices	
checkAndDownloadVoice()
#set CustomVoice
setCustomVoice()
#set english subconsious mouth to user globalised mouth now ( only if we found a language pack )


if languagePackLoaded==1 and LanguageError==0 and VoiceError==0:
	subconsciousMouth=mouth
if languagePackLoaded==0:
	errorSpokenFunc('BadLanguagePack')
	
#init confirmation	
talkEvent(lang_startingMouth)
talkEvent(lang_whatIsThisLanguage)
	
################################
# INIT.5 - skeleton loading
################################
#we launch Inmoov Skeleton
for filename in os.listdir(RuningFolder+'inmoovSkeleton'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovSkeleton/'+filename)




################################
# INIT.6 - inmoov loading
################################
	
#we launch Inmoov Gestures
for filename in os.listdir(RuningFolder+'inmoovGestures'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovGestures/'+filename)
		print filename
		
#we launch Inmoov inmoovVocal commands
for filename in os.listdir(RuningFolder+'inmoovVocal/ear.addCommand'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovVocal/ear.addCommand/'+filename.encode('utf8'))
		print filename
		
#we launch Inmoov life
for filename in os.listdir(RuningFolder+'inmoovLife'):		
	if os.path.splitext(filename)[1] == ".py":
		execfile(RuningFolder+'inmoovLife/'+filename)
		


#create the custom script, only if not exist
if not os.path.isfile(RuningFolder+'inmoovCustom/Inmoov_custom.py'):
		shutil.move(RuningFolder+'inmoovCustom/Inmoov_custom.py.default',RuningFolder+'inmoovCustom/Inmoov_custom.py')
print " INIT.6 ...all is ok !"	
talkEvent(lang_startingEar)
talkEvent(lang_ready)
WebkitSpeechRecognitionFix.startClock()




