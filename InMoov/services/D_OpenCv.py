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
except:
  ThisServicePartConfig.set('MAIN','streamerEnabled',False)
  with open(ThisServicePart+'.config', 'wb') as f:
    ThisServicePartConfig.write(f)
  ThisServicePartConfig.read(ThisServicePart+'.config')
  pass
streamerEnabled=ThisServicePartConfig.getboolean('MAIN', 'streamerEnabled')

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
  else:talkEvent(lang_startingOpenCv)
  
  opencv.removeFilters()
  opencv.stopCapture()
  
if isOpenCvActivated:openCvInit()