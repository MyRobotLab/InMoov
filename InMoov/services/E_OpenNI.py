# ##############################################################################
#            *** KINECT *** >> TODO MIGRATE TO INMOOV SERVICE
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isKinectActivated=0
global KinectStarted  
KinectStarted=0
isKinectActivated=ThisServicePartConfig.getboolean('MAIN', 'isKinectActivated')
  
openNiShouldersOffset=float(ThisServicePartConfig.get('MAIN', 'openNiShouldersOffset'))
openNiLeftShoulderInverted=ThisServicePartConfig.getboolean('MAIN', 'openNiLeftShoulderInverted')
openNiRightShoulderInverted=ThisServicePartConfig.getboolean('MAIN', 'openNiRightShoulderInverted')

# ##############################################################################
#                 SERVICE START
# ##############################################################################


def openNIInit():
  if isKinectActivated:
    i01.openNiShouldersOffset=openNiShouldersOffset
    i01.openNiLeftShoulderInverted=openNiLeftShoulderInverted
    i01.openNiRightShoulderInverted=openNiRightShoulderInverted
    try:
      openni.capture()
      #worky open ni kinect detection
      timeout=0
      while not i01.RobotIsOpenNiCapturing:
        sleep(1)
        timeout+=1
        if timeout>7:break
    except:
      pass

if isKinectActivated:
  try:
    openni = Runtime.createAndStart("i01.openni", "OpenNi")
  except:
    isKinectActivated=0
    pass
  openNIInit()
  
  if not i01.RobotIsOpenNiCapturing:
    if ScriptType!="RightSide":errorSpokenFunc('OpenNiNoWorky')
    isKinectActivated=0
    
  else:
    try:
      i01.startOpenNI()
      openni.stopCapture()
    except:
      pass
