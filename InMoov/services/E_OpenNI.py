# ##############################################################################
#            *** KINECT ***
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('openni',ThisServicePart+'.config')
###############################################################################

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isKinectActivated=0
global KinectStarted  
KinectStarted=0
isKinectActivated=ThisServicePartConfig.getboolean('MAIN', 'isKinectActivated')


# ##############################################################################
#                 SERVICE START
# ##############################################################################


def openNIInit():
  global KinectStarted  
  KinectStarted=0
  openni.capture()
  #worky open ni kinect detection
  timeout=0
  while not KinectStarted:
    sleep(1)
    timeout+=1
    if timeout>7:break
  
  if not KinectStarted:
    if ScriptType!="RightSide":
      errorSpokenFunc('OpenNiNoWorky')
    isKinectActivated=0
  else:
    talkEvent(lang_startingOpenNi)
    i01.startOpenNI()
    openni.stopCapture()
    
  
 

def onOpenNIData(data):
#####################################################
# This is openni functions that do jobs
#####################################################
  global KinectStarted
  if data and not KinectStarted:
    KinectStarted=1

if isKinectActivated:
  i01.openni = Runtime.createAndStart("i01.openni", "OpenNi")
  openni=i01.openni
  python.subscribe(openni.getName(),"publishOpenNIData")
  openNIInit()