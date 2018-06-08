# ##############################################################################
#                 INITIAL CHECKUP
# ##############################################################################

################################
# INIT.1 - system dependencies & language pack
################################
#subconscious for diagnose
subconsciousMouth = Runtime.createAndStart("subconsciousMouth", "MarySpeech")
subconsciousMouth.setVoice("cmu-slt-hsmm")
log = Runtime.createAndStart("log", "Log")
runtime.setLogLevel("INFO")
# libraries import
execfile(RuningFolder+'/system/Import_Libraries.py')
# common functions
execfile(RuningFolder+'/system/Import_Functions.py')


RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"
# global vars import
execfile(RuningFolder+'/system/Robot_Satus_GlobalsVars.py')

#inmoov.fr webgui
execfile(RuningFolder+'/system/inmoovGui.py')

# we load personal parameters
execfile(RuningFolder+'/system/ConfigParser.py')

# language pack
execfile(RuningFolder+'/system/languagePack.py')

# vocal errors
execfile(RuningFolder+'/system/Errors.py'.encode('utf8'))


################################
# INIT.2 - mrl core updater
################################

execfile(RuningFolder+'/system/updater/mrl_updater.py')

################################
# INIT.3 - services call
################################
#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in sorted(os.listdir(RuningFolder+'services')):    
  if os.path.splitext(filename)[1] == ".py":
    execfile(RuningFolder+'services/'+filename.encode('utf8'))
    if DEBUG==1:print filename
if LoadingPicture:displayPic(RuningFolder+'/system/pictures/loading_1024-600.jpg')
#mrl too old dude, update it !
#if actualVersion<int(mrlCompatible):errorSpokenFunc('MrlNeedUpdate')   
 
################################
# INIT.4 - skeleton loading & virtual skeleton
################################
#we launch Inmoov Skeleton at half speed
i01.halfSpeed()

for filename in os.listdir(RuningFolder+'skeleton'):    
  if os.path.splitext(filename)[1] == ".py":execfile(RuningFolder+'skeleton/'+filename.encode('utf8'))

if virtualInmoovActivated:
  talkEvent(lang_startingVirtual)
  i01.startVinMoov()
  
if ((not isEyeLidsActivated and not isHeadActivated and not isLeftArmActivated and not isLeftHandActivated and not isRightArmActivated and not isRightHandActivated and not isTorsoActivated) and (ScriptType!="Virtual" and ScriptType!="NoArduino")):
  talkEvent(lang_noSkeleton)
  
################################
# INIT.5 - ear.addcmmands
################################
#if chatbot loaded we do not load ear.addcommands
for root, subdirs, files in os.walk(RuningFolder+'minimal'):
  for name in files:
    if name.split(".")[-1] == "py":
      if (isChatbotActivated and name.split(".")[0][:11] == "earCommands"):
        print name.split(".")[0]," not loaded because chatbot is activated"
      else:  
        execfile(os.path.join(root, name).encode('utf8'))
        if DEBUG==1:print "debug  ear.addcmmands : ",os.path.join(root, name)    


################################
# INIT.6- inmoov loading
################################
  
#we launch Inmoov Gestures
for root, subdirs, files in os.walk(RuningFolder+'gestures'):
  for name in files:
    if name.split(".")[-1] == "py":
      execfile(os.path.join(root, name))
      if DEBUG==1:print "debug inmoovGestures : ",os.path.join(root, name)
    
#we launch Inmoov life
for root, subdirs, files in os.walk(RuningFolder+'life'):
  for name in sorted(files):
    if name.split(".")[-1] == "py":
      execfile(os.path.join(root, name))
      if DEBUG==1:print "debug inmoovLife : ",os.path.join(root, name)

#create the custom script, only if not exist
if not os.path.isfile(RuningFolder+'custom/InMoov_custom.py'):shutil.move(RuningFolder+'custom/InMoov_custom.py.default',RuningFolder+'custom/InMoov_custom.py')

      
################################
# INIT.8 - yes there is no 7 :) great, inmoov is alive
################################
if DEBUG==1:runtime.setLogLevel("INFO")
else:runtime.setLogLevel("ERROR")

#wip updater
execfile(RuningFolder+'/system/updater/inmoovos_updater.py')


if boot_green and isNeopixelActivated:    
  i01.setNeopixelAnimation("Flash Random", 0, 255, 0, 1)
  sleep(2)
  i01.stopNeopixelAnimation()
  sleep(1)
  i01.setNeopixelAnimation("Flash Random", 0, 255, 50, 10)
sleep(1)
sleepModeWakeUp()