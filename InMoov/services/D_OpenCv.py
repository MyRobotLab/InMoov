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
isOpenCvActivated=0
global opencvStarted  
opencvStarted=0
isOpenCvActivated=ThisServicePartConfig.getboolean('MAIN', 'isOpenCvActivated')
CameraIndex=ThisServicePartConfig.getint('MAIN', 'CameraIndex') 
DisplayRender=ThisServicePartConfig.get('MAIN', 'DisplayRender')

# ##############################################################################
#                 SERVICE START
# ##############################################################################


i01.opencv = Runtime.createAndStart("i01.opencv", "OpenCV")
opencv=i01.opencv
python.subscribe(opencv.getName(),"publishOpenCVData")


def openCvInit():
  global opencvStarted  
  opencvStarted=0
  if DisplayRender=="SarxosFrameGrabber":opencv.setFrameGrabberType("org.myrobotlab.opencv."+DisplayRender)
  opencv.setCameraIndex(CameraIndex)
  opencv.removeFilters()
  opencv.addFilter("PyramidDown")
  opencv.addFilter("Gray")
  opencv.addFilter("FaceDetect")
  opencv.setDisplayFilter("FaceDetect")
  opencv.capture()
  #worky open cv camera detection
  timeout=0
  while not opencvStarted:
    sleep(1)
    timeout+=1
    if timeout>7:break
  
  if not opencvStarted:
    if ScriptType!="RightSide":
      errorSpokenFunc('OpenCvNoWorky','camera '+str(CameraIndex))
    isOpenCvActivated=0
  else:talkEvent(lang_startingOpenCv)
  
  opencv.removeFilters()


def onOpenCVData(data):
#####################################################
# This is opencv functions that do jobs
#####################################################
  global opencvStarted
  if data and not opencvStarted:
    opencvStarted=1
  global FaceDetected
  

if isOpenCvActivated:openCvInit()
  