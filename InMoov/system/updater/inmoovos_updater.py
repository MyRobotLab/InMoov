#inmoov os check if there is a new version ( stable or beta )
def CheckVersion():
  global RobotneedUpdate
  global target
  global branch
  
  branch="master"
  if BetaVersion:branch="develop"
  
  #download remote information
  remoteVersion=""
  try:
    urlretrieve("https://raw.githubusercontent.com/MyRobotLab/inmoov/"+branch+"/InMoov/system/updater/updater.ini", RuningFolder+'system/updater/updater.ini')
    #read downloaded file
    BasicConfig = ConfigParser.ConfigParser(allow_no_value = True)
    BasicConfig.read(RuningFolder+'system/updater/updater.ini')
    remoteVersion=BasicConfig.get('updater', 'version')
    targetstable=BasicConfig.get('updater', 'targetstable')
    targetbeta=BasicConfig.get('updater', 'targetbeta')
    #read myrobotlab.jar url
    target=targetstable
    if BetaVersion:target=targetbeta
  except:
    pass
  
  
  if str(remoteVersion) == str(version) or str(remoteVersion)=='':
    return False
  else:
    print "need update"
    RobotneedUpdate=1
    i01.RobotIsStarted=1
    return True
    

talkDownloadPercent = Runtime.start("talkDownloadPercent","Clock")
talkDownloadPercent.setInterval(5000)
global percentDownload
percentDownload=0

def talkDownloadPercentFunc(timedata):
  chatBot.getResponse(str(percentDownload) + " SYSTEM_PERCENT")
  
  
talkDownloadPercent.addListener("pulse", python.name, "talkDownloadPercentFunc")




def dlProgress(count, blockSize, totalSize):
    global percentDownload
    percentDownload=(int(count * blockSize * 100 / totalSize))
  
def updateMe():
  
  
  global RobotneedUpdate
  if RobotneedUpdate:
    RobotneedUpdate=0
    print "start"
    PlayNeopixelAnimation("Theater Chase", 0, 0, 255, 5)
    displayPic(RuningFolder+'system/pictures/update_1024-600.jpg')
    sleep(2)
    talkDownloadPercent.startClock()
    urlretrieve(target, RuningFolder+'myrobotlab-'+branch+".jar",reporthook=dlProgress)
    sleep(2)
    talkDownloadPercent.stopClock()
    chatBot.getResponse("SYSTEM_DOWNLOAD_OK")
    sleep(3)
    open("mrlNeedReinstall", 'a').close()
    RemoveFile(RuningFolder+'system/updater/currentMrlVersion.ini')
    shutdown()

def dontUpdateMe():
  
  global RobotneedUpdate
  if RobotneedUpdate:
    RobotneedUpdate=0
    sleep(2)
    sleepModeWakeUp()
  
  
#hard coded forced patch v 0.3.5

def RemoveFile(file):
  try:
    os.remove(file)
  except:
    pass
  

RemoveFile(RuningFolder+"gestures/translateText.py")
RemoveFile(RuningFolder+"gestures/translateTextFR.py")
RemoveFile(RuningFolder+"gestures/rockpaperscissors.py")
RemoveFile(RuningFolder+"gestures/rockpaperscissors2.py")
RemoveFile(RuningFolder+"gestures/stoprockpaperscissors.py")
RemoveFile(RuningFolder+"life/AutoListen.py")

  #clean up .default.config
for root, subdirs, files in os.walk(RuningFolder):
  for name in files:
    if name.split(".")[-1] == "default":
      os.remove(os.path.join(root, name))
      if DEBUG==1:print "removed .default : ",os.path.join(root, name)