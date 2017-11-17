# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('opencv',ThisServicePart+'.config')
###############################################################################

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
global isOpenCvActivated
isOpenCvActivated=0

isOpenCvActivated=ThisServicePartConfig.getboolean('MAIN', 'isOpenCvActivated')
CameraIndex=ThisServicePartConfig.getint('MAIN', 'CameraIndex') 
DisplayRender=ThisServicePartConfig.get('MAIN', 'DisplayRender')

try:
  streamerEnabled=ThisServicePartConfig.getboolean('MAIN', 'streamerEnabled')
  eyeXPidKp=ThisServicePartConfig.get('TRACKING', 'eyeXPidKp')
except:
  ThisServicePartConfig.set('MAIN','streamerEnabled',False)
  ThisServicePartConfig.add_section('TRACKING')
  ThisServicePartConfig.set('TRACKING','eyeXPidKp',12.0)
  ThisServicePartConfig.set('TRACKING','eyeXPidKi',1.0)
  ThisServicePartConfig.set('TRACKING','eyeXPidKd',0.1)
  ThisServicePartConfig.set('TRACKING','eyeYPidKp',12.0)
  ThisServicePartConfig.set('TRACKING','eyeYPidKi',1.0)
  ThisServicePartConfig.set('TRACKING','eyeYPidKd',0.1)
  ThisServicePartConfig.set('TRACKING','rotheadPidKp',5.0)
  ThisServicePartConfig.set('TRACKING','rotheadPidKi',1.0)
  ThisServicePartConfig.set('TRACKING','rotheadPidKd',0.1)
  ThisServicePartConfig.set('TRACKING','neckPidKp',5.0)
  ThisServicePartConfig.set('TRACKING','neckPidKi',1.0)
  ThisServicePartConfig.set('TRACKING','neckPidKd',0.1)

  with open(ThisServicePart+'.config', 'wb') as f:
    ThisServicePartConfig.write(f)
  ThisServicePartConfig.read(ThisServicePart+'.config')
  pass
  
faceRecognizerActivated=True
try:
  faceRecognizerActivated=ThisServicePartConfig.getboolean('MAIN', 'faceRecognizerActivated')
except:
  pass

streamerEnabled=ThisServicePartConfig.getboolean('MAIN', 'streamerEnabled')
eyeXPidKp=ThisServicePartConfig.getfloat('TRACKING', 'eyeXPidKp')
eyeXPidKi=ThisServicePartConfig.getfloat('TRACKING', 'eyeXPidKi')
eyeXPidKd=ThisServicePartConfig.getfloat('TRACKING', 'eyeXPidKd')
eyeYPidKp=ThisServicePartConfig.getfloat('TRACKING', 'eyeYPidKp')
eyeYPidKi=ThisServicePartConfig.getfloat('TRACKING', 'eyeYPidKi')
eyeYPidKd=ThisServicePartConfig.getfloat('TRACKING', 'eyeYPidKd')
rotheadPidKp=ThisServicePartConfig.getfloat('TRACKING', 'rotheadPidKp')
rotheadPidKi=ThisServicePartConfig.getfloat('TRACKING', 'rotheadPidKi')
rotheadPidKd=ThisServicePartConfig.getfloat('TRACKING', 'rotheadPidKd')
neckPidKp=ThisServicePartConfig.getfloat('TRACKING', 'neckPidKp')
neckPidKi=ThisServicePartConfig.getfloat('TRACKING', 'neckPidKi')
neckPidKd=ThisServicePartConfig.getfloat('TRACKING', 'neckPidKd')

#for noworky
log.info("D_OpenCv.config")
log.info("isOpenCvActivated : "+str(isOpenCvActivated))
log.info("DisplayRender : "+str(DisplayRender))
log.info("streamerEnabled : "+str(streamerEnabled))

# ##############################################################################
#                 SERVICE START
# ##############################################################################


i01.opencv = Runtime.create("i01.opencv", "OpenCV")
opencv=i01.opencv
opencv.streamerEnabled=streamerEnabled
i01.opencv = Runtime.start("i01.opencv", "OpenCV")

def openCvInit():
  global isOpenCvActivated
  if DisplayRender=="SarxosFrameGrabber":opencv.setFrameGrabberType("org.myrobotlab.opencv."+DisplayRender)
  opencv.setCameraIndex(CameraIndex)
  opencv.removeFilters()
  opencv.capture()
  #worky open cv camera detection
  timeout=0
  while not i01.RobotIsOpenCvCapturing():
    sleep(1)
    timeout+=1
    if timeout>7:break
  
  if not i01.RobotIsOpenCvCapturing():
    if ScriptType!="RightSide":
      errorSpokenFunc('OpenCvNoWorky','camera '+str(CameraIndex))
    isOpenCvActivated=0
  else:
    talkEvent(lang_startingOpenCv)
    python.subscribe("i01.opencv", "publishRecognizedFace")
  
  opencv.removeFilters()
  opencv.stopCapture()
  
if isOpenCvActivated:openCvInit()

def onRecognizedFace(name):
  print name
  # robot reaction if recognized face ( todo beter reaction... )
  if isChatbotActivated:
    chatBot.setUsername(unicode(name,'utf-8'))
    chatBot.getResponse("SYSTEM_SAY_HELLO")