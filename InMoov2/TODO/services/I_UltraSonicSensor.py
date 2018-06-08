# -- coding: utf-8 --
# ##############################################################################
#                 ultra Sonic Sensor FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
trigPin=ThisServicePartConfig.getint('MAIN', 'trigPin')
echoPin=ThisServicePartConfig.getint('MAIN', 'echoPin')
ultraSonicSensorArduino=ThisServicePartConfig.get('MAIN', 'ultraSonicSensorArduino')
ultraSonicSensorActivated=ThisServicePartConfig.getboolean('MAIN', 'ultraSonicSensorActivated')

if ultraSonicSensorActivated:
  ultrasonicSensor = Runtime.start("ultrasonicSensor", "UltrasonicSensor")
  
  try:
    ultraSonicSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'ultraSonicSensorArduino'))
    ultrasonicSensor.attach(ultraSonicSensorArduino, trigPin, echoPin)
    i01.ultrasonicSensor=ultrasonicSensor
    talkEvent(lang_startingUltraSonic)
    # range can also be retreieved in a blocking call
    print "ultrasonicSensor test is ", i01.getUltrasonicSensorDistance()
  except:
    errorSpokenFunc('BAdrduinoChoosen','ultra Sonic Sensor')
    ultraSonicSensorActivated=False
    pass
  