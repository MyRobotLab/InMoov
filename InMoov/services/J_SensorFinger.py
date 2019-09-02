# -- coding: utf-8 --
# ##############################################################################
#                 finger Sensor FILE
# ##############################################################################

#TODO Create a auto calibrating file for each sensor when the robot initialize which sends the data here

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

right_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_Psi_min')
right_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_Psi_low')
right_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_Psi_mid')
right_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_Psi_max')

left_thumbPin=ThisServicePartConfig.getint('MAIN', 'left_thumbPin')
left_indexPin=ThisServicePartConfig.getint('MAIN', 'left_indexPin')
left_majeurePin=ThisServicePartConfig.getint('MAIN', 'left_majeurePin')
left_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'left_ringFingerPin')
left_pinkyPin=ThisServicePartConfig.getint('MAIN', 'left_pinkyPin')
left_extraPin=ThisServicePartConfig.getint('MAIN', 'left_extraPin')
leftHandSensorArduino=ThisServicePartConfig.get('MAIN', 'leftHandSensorArduino')
leftHandSensorActivated=ThisServicePartConfig.getboolean('MAIN', 'leftHandSensorActivated')

left_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_Psi_min')
left_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_Psi_low')
left_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_Psi_mid')
left_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_Psi_max')

if rightHandSensorActivated:
  
  try:
    def publishRightSensor(pins):
      for pin in range(0, len(pins)):
          print pins[pin].address, pins[pin].value  #these values are between 0-1024
          if pins[pin].value<=(right_Psi_min)and pins[pin].value<(right_Psi_low):
            print "No right pressure"
          if pins[pin].value>=(right_Psi_low)and pins[pin].value<(right_Psi_mid):
            print "Low right pressure"
          if pins[pin].value>=(right_Psi_mid)and pins[pin].value<(right_Psi_max):
            print "Mid right pressure"
          if pins[pin].value>=(right_Psi_max):
            print "High right pressure"
    rightHandSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'rightHandSensorArduino'))
    rightHandSensorArduino.addListener("publishPinArray","python","publishRightSensor")
    rightHandSensorArduino.enablePin(right_thumbPin,1)
    rightHandSensorArduino.enablePin(right_indexPin,1)
    rightHandSensorArduino.enablePin(right_majeurePin,1)
    rightHandSensorArduino.enablePin(right_ringFingerPin,1)
    rightHandSensorArduino.enablePin(right_pinkyPin,1)
    rightHandSensorArduino.enablePin(right_extraPin,1)
    talkEvent(lang_startingRightHandSensor)
    
  except:
    errorSpokenFunc('BAdrduinoChoosen','right Hand Sensor')
    rightHandSensorActivated=False
    pass

if leftHandSensorActivated:
  leftHandSensor = Runtime.start("leftHandSensor", "SensorMonitor")
  
  try:
    def publishLeftSensor(pins):
      for pin in range(0, len(pins)):
          print pins[pin].address, pins[pin].value  #these values are between 0-1024
          if pins[pin].value<=(left_Psi_min)and pins[pin].value<(left_Psi_low):
            print "No left pressure"
          if pins[pin].value>=(left_Psi_low)and pins[pin].value<(left_Psi_mid):
            print "Low left pressure"
          if pins[pin].value>=(left_Psi_mid)and pins[pin].value<(left_Psi_max):
            print "Mid left pressure"
          if pins[pin].value>=(left_Psi_max):
            print "High left pressure"
    leftHandSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'leftHandSensorArduino'))
    leftHandSensorArduino.addListener("publishPinArray","python","publishLeftSensor")
    leftHandSensorArduino.enablePin(left_thumbPin,1)
    leftHandSensorArduino.enablePin(left_indexPin,1)
    leftHandSensorArduino.enablePin(left_majeurePin,1)
    leftHandSensorArduino.enablePin(left_ringFingerPin,1)
    leftHandSensorArduino.enablePin(left_pinkyPin,1)
    leftHandSensorArduino.enablePin(left_extraPin,1)
    talkEvent(lang_startingLeftHandSensor)
   
  except:
    errorSpokenFunc('BAdrduinoChoosen','left Hand Sensor')
    leftHandSensorActivated=False
    pass
