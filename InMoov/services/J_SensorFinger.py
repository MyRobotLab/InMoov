# -- coding: utf-8 --
# ##############################################################################
#                 finger Sensor FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
right_thumbPin=ThisServicePartConfig.getint('MAIN', 'right_thumbPin')
right_indexPin=ThisServicePartConfig.getint('MAIN', 'right_indexPin')
right_majeurePin=ThisServicePartConfig.getint('MAIN', 'right_majeurePin')
right_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'right_ringFingerPin')
right_pinkyPin=ThisServicePartConfig.getint('MAIN', 'right_pinkyPin')
right_extraPin=ThisServicePartConfig.getint('MAIN', 'right_extraPin')
rightHandSensorArduino=ThisServicePartConfig.get('MAIN', 'rightHandSensorArduino')
rightHandSensorActivated=ThisServicePartConfig.getboolean('MAIN', 'rightHandSensorActivated')

left_thumbPin=ThisServicePartConfig.getint('MAIN', 'left_thumbPin')
left_indexPin=ThisServicePartConfig.getint('MAIN', 'left_indexPin')
left_majeurePin=ThisServicePartConfig.getint('MAIN', 'left_majeurePin')
left_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'left_ringFingerPin')
left_pinkyPin=ThisServicePartConfig.getint('MAIN', 'left_pinkyPin')
left_extraPin=ThisServicePartConfig.getint('MAIN', 'left_extraPin')
leftHandSensorArduino=ThisServicePartConfig.get('MAIN', 'leftHandSensorArduino')
leftHandSensorActivated=ThisServicePartConfig.getboolean('MAIN', 'leftHandSensorActivated')

if rightHandSensorActivated:
  rightHandSensor = Runtime.start("SensorMonitor", "rightHandSensor")
  
  try:
    rightHandSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'rightHandSensorArduino'))
    rightHandSensor.attach(rightHandSensorArduino, right_thumbPin, right_indexPin, right_majeurePin, right_ringFingerPin, right_pinkyPin, right_extraPin)
    i01.rightHandSensor=rightHandSensor
    i01.speakBlocking(i01.languagePack.get("startingRightHandSensor"))
    # range can also be retreieved in a blocking call
    print "rightHandSensor test is ", i01.getRightHandSensorAccuracy()
  except:
    errorSpokenFunc('BAdrduinoChoosen','right Hand Sensor')
    rightHandSensorActivated=False
    pass

if leftHandSensorActivated:
  leftHandSensor = Runtime.start("SensorMonitor", "leftHandSensor")
  
  try:
    leftHandSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'leftHandSensorArduino'))
    leftHandSensor.attach(leftHandSensorArduino, left_thumbPin, left_indexPin, left_majeurePin, left_ringFingerPin, left_pinkyPin, left_extraPin)
    i01.leftHandSensor=leftHandSensor
    i01.speakBlocking(i01.languagePack.get("startingLeftHandSensor"))
    # range can also be retreieved in a blocking call
    print "leftHandSensor test is ", i01.getLeftHandSensorAccuracy()
  except:
    errorSpokenFunc('BAdrduinoChoosen','left Hand Sensor')
    leftHandSensorActivated=False
    pass    
  