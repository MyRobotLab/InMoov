# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
global isOpenCvActivated
i01.vision.setOpenCVenabled(ThisServicePartConfig.getboolean('MAIN', 'isOpenCvActivated'))
isOpenCvActivated=i01.vision.openCVenabled
CameraIndex=ThisServicePartConfig.getint('MAIN', 'CameraIndex') 
DisplayRender=ThisServicePartConfig.get('MAIN', 'DisplayRender')

flipPicture=False
faceRecognizerActivated=True
try:
  flipPicture=ThisServicePartConfig.getboolean('MAIN', 'flipPicture')
  faceRecognizerActivated=ThisServicePartConfig.getboolean('MAIN', 'faceRecognizerActivated')
except:pass

streamerEnabled=ThisServicePartConfig.getboolean('MAIN', 'streamerEnabled')

#for noworky
log.info("D_OpenCv.config")
log.info("isOpenCvActivated : "+str(isOpenCvActivated))
log.info("DisplayRender : "+str(DisplayRender))
log.info("streamerEnabled : "+str(streamerEnabled))

#i01.vision.setOpenCVenabled(True)
#i01.vision.addPreFilter("Flip")
#i01.opencv.setCameraIndex(1)
#i01.opencv.setGrabberType("Sarxos")

if flipPicture:i01.vision.addPreFilter("Flip")

# ##############################################################################
#                 SERVICE START
# ##############################################################################

if i01.vision.openCVenabled:
  i01.opencv = Runtime.create("i01.opencv", "OpenCV")
  i01.opencv.setCameraIndex(CameraIndex)
  i01.opencv.setGrabberType(DisplayRender)
  i01.opencv = Runtime.start("i01.opencv", "OpenCV")
  i01.vision.setOpenCVenabled(i01.startOpenCV())
  if not i01.vision.openCVenabled:
    errorSpokenFunc('OpenCvNoWorky','camera '+str(i01.opencv.getCameraIndex()))
  else:
    python.subscribe("i01.opencv", "publishRecognizedFace")
  

def onRecognizedFace(name):
  print name
  # robot reaction if recognized face ( todo beter reaction... )
  if isChatbotActivated:
    i01.chatBot.startSession(unicode(name,'utf-8'))
    i01.opencv.disableFilter("FaceRecognizer")
    i01.chatBot.getResponse("SYSTEM_SAY_HELLO")
