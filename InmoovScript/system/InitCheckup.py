# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

#we import libraries
execfile(RuningFolder+'/system/Import_Libraries.py')
RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"

#we load personal parameters
execfile(RuningFolder+'/system/ConfigParser.py')

#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in os.listdir(RuningFolder+'services'):
     execfile(RuningFolder+'services/'+filename)

#we include some error control
execfile(RuningFolder+'system/Errors.py')

#we start raw Inmoov ear and mouth service
i01.startMouth()
i01.startEar()
ear = i01.ear

#set user language
setRobotLanguage()

#check and update marytts voices	
checkAndDownloadVoice()

#set CustomVoice
setCustomVoice()
	
# We do a checkup of arduinos and mrlcomm
CheckArduinos()
	

#todo check mrlcomm version		
print right.getBoardInfo()


