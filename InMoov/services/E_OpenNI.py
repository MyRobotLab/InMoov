# ##############################################################################
#            *** KINECT *** >> TODO MIGRATE TO INMOOV SERVICE
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
  if isKinectActivated:
    python.subscribe(openni.getName(),"publishOpenNIData")
    openni.capture()
    #worky open ni kinect detection
    timeout=0
    while not KinectStarted:
      sleep(1)
      timeout+=1
      if timeout>7:break

def onOpenNIData(data):
#####################################################
# This is openni functions that do jobs
#####################################################
  global KinectStarted
  if data and not KinectStarted:
    KinectStarted=1
    
  if data:
    skeleton = data.skeleton

    leftBicep = round(skeleton.leftBicep.getAngleXY())
    leftOmoplate = round(skeleton.leftShoulder.getAngleXY())
    leftShoulder = round(skeleton.leftShoulder.getAngleYZ())

    rightBicep = round(skeleton.rightBicep.getAngleXY())
    rightOmoplate = round(skeleton.rightShoulder.getAngleXY())
    rightShoulder = round(skeleton.rightShoulder.getAngleYZ())

  try:
    leftBicep = int(leftBicep)
    leftOmoplate = int(leftOmoplate)
    leftShoulder = int(leftShoulder) - 50

    rightBicep = int(rightBicep)
    rightOmoplate = int(rightOmoplate)
    rightShoulder = int(rightShoulder) - 50
  except ValueError:
    print "Value error: ", ValueError

  if leftBicep>0 and leftOmoplate>0 and leftShoulder>0:
    if DEBUG_KINECT==1:
      print "Left Bicep : ", leftBicep
      print "Left Omoplate : ", leftOmoplate
      print "Left Shoulder : ", leftShoulder

      moveArm("left", leftBicep, 90, leftShoulder, leftOmoplate)

  if rightBicep>0 and rightOmoplate>0 and rightShoulder>0:
    if DEBUG_KINECT==1:
      print "Right Bicep : ", rightBicep
      print "Right Omoplate: ", rightOmoplate
      print "Right Shoulder : ", rightShoulder

      moveArm("right", rightBicep, 90, rightShoulder, rightOmoplate)  

if isKinectActivated:
  try:
    openni = Runtime.createAndStart("i01.openni", "OpenNi")
  except:
    isKinectActivated=0
    pass
  openNIInit()
  
  if not KinectStarted:
    if ScriptType!="RightSide":errorSpokenFunc('OpenNiNoWorky')
    isKinectActivated=0
    
  else:
    talkEvent(lang_startingOpenNi)
    i01.startOpenNI()
    openni.stopCapture()