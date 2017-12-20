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
  if DisplayRender=="SarxosFrameGrabber":opencv.setFrameGrabberType("org.myrobotlab.opencv.SarxosFrameGrabber")
  if DisplayRender=="VideoInputFrameGrabber":opencv.setFrameGrabberType("org.bytedeco.javacv.VideoInputFrameGrabber")
  if DisplayRender=="OpenCVFrameGrabber":opencv.setFrameGrabberType("org.bytedeco.javacv.OpenCVFrameGrabber")
  
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