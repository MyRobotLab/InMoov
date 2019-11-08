# -- coding: utf-8 --
# ##############################################################################
#                 finger Sensor FILE
# ##############################################################################
# This a work in progress

#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

#Right Hand sensors
right_thumbPin=ThisServicePartConfig.getint('MAIN', 'right_thumbPin')
right_indexPin=ThisServicePartConfig.getint('MAIN', 'right_indexPin')
right_majeurePin=ThisServicePartConfig.getint('MAIN', 'right_majeurePin')
right_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'right_ringFingerPin')
right_pinkyPin=ThisServicePartConfig.getint('MAIN', 'right_pinkyPin')
right_extraPin=ThisServicePartConfig.getint('MAIN', 'right_extraPin')
rightHandSensorArduino=ThisServicePartConfig.get('MAIN', 'rightHandSensorArduino')
rightHandSensorActivated=ThisServicePartConfig.getboolean('MAIN', 'rightHandSensorActivated')

right_thumb_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_min')
right_thumb_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_low')
right_thumb_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_mid')
right_thumb_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_max')

right_index_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_min')
right_index_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_low')
right_index_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_mid')
right_index_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_max')

right_majeure_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_min')
right_majeure_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_low')
right_majeure_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_mid')
right_majeure_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_max')

right_ringFinger_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_min')
right_ringFinger_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_low')
right_ringFinger_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_mid')
right_ringFinger_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_max')

right_pinky_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_min')
right_pinky_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_low')
right_pinky_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_mid')
right_pinky_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_max')

right_extra_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_extra_Psi_min')
right_extra_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_extra_Psi_low')
right_extra_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_extra_Psi_mid')
right_extra_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_extra_Psi_max')


#Left Hand sensors
left_thumbPin=ThisServicePartConfig.getint('MAIN', 'left_thumbPin')
left_indexPin=ThisServicePartConfig.getint('MAIN', 'left_indexPin')
left_majeurePin=ThisServicePartConfig.getint('MAIN', 'left_majeurePin')
left_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'left_ringFingerPin')
left_pinkyPin=ThisServicePartConfig.getint('MAIN', 'left_pinkyPin')
left_extraPin=ThisServicePartConfig.getint('MAIN', 'left_extraPin')
leftHandSensorArduino=ThisServicePartConfig.get('MAIN', 'leftHandSensorArduino')
leftHandSensorActivated=ThisServicePartConfig.getboolean('MAIN', 'leftHandSensorActivated')

left_thumb_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_min')
left_thumb_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_low')
left_thumb_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_mid')
left_thumb_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_max')

left_index_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_min')
left_index_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_low')
left_index_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_mid')
left_index_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_max')

left_majeure_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_min')
left_majeure_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_low')
left_majeure_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_mid')
left_majeure_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_max')

left_ringFinger_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_min')
left_ringFinger_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_low')
left_ringFinger_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_mid')
left_ringFinger_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_max')

left_pinky_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_min')
left_pinky_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_low')
left_pinky_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_mid')
left_pinky_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_max')

left_extra_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_extra_Psi_min')
left_extra_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_extra_Psi_low')
left_extra_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_extra_Psi_mid')
left_extra_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_extra_Psi_max')


if rightHandSensorActivated:
  
  try:
    # common right pin listener function
    def publishRightSensor(pinsRight):
          print ""
                
          global rightThumbPressure
          global rightIndexPressure
          global rightMajeurePressure
          global rightRingFingerPressure
          global rightPinkyPressure
          global rightExtraPressure
          

          
          for pin in range(0, len(pinsRight)):
            if pinsRight[pin].address==(right_thumbPin):
              if pinsRight[pin].value<=(right_thumb_Psi_min) and pinsRight[pin].value<(right_thumb_Psi_low):rightThumbPressure = 0 
              if pinsRight[pin].value>=(right_thumb_Psi_low)and pinsRight[pin].value<(right_thumb_Psi_mid):
                if rightThumbPressure == 1:
                  i01.rightHand.thumb.stop()
                  i01.rightHand.thumb.disable()
              if pinsRight[pin].value>=(right_thumb_Psi_mid)and pinsRight[pin].value<(right_thumb_Psi_max):
                if rightThumbPressure <= 2:
                  i01.rightHand.thumb.stop()
                  i01.rightHand.thumb.disable()
              if pinsRight[pin].value>=(right_thumb_Psi_max):
                if rightThumbPressure <= 3:
                  i01.rightHand.thumb.stop()
                  i01.rightHand.thumb.disable()
              print "rightThumbSensorPin:",right_thumbPin,"Value:",pinsRight[pin].value

            if pinsRight[pin].address==(right_indexPin):
              if pinsRight[pin].value<=(right_index_Psi_min) and pinsRight[pin].value<(right_index_Psi_low):rightIndexPressure = 0
              if pinsRight[pin].value>=(right_index_Psi_low)and pinsRight[pin].value<(right_index_Psi_mid):
                if rightIndexPressure == 1:
                  i01.rightHand.index.stop()
                  i01.rightHand.index.disable()
              if pinsRight[pin].value>=(right_index_Psi_mid)and pinsRight[pin].value<(right_index_Psi_max):
                if rightIndexPressure <= 2:
                  i01.rightHand.index.stop()
                  i01.rightHand.index.disable()
              if pinsRight[pin].value>=(right_index_Psi_max):
                if rightIndexPressure <= 3:
                  i01.rightHand.index.stop()
                  i01.rightHand.index.disable()
              print "rightIndexSensorPin:",right_indexPin,"Value:",pinsRight[pin].value

            if pinsRight[pin].address==(right_majeurePin):
              if pinsRight[pin].value<=(right_majeure_Psi_min) and pinsRight[pin].value<(right_majeure_Psi_low):rightMajeurePressure = 0
              if pinsRight[pin].value>=(right_majeure_Psi_low)and pinsRight[pin].value<(right_majeure_Psi_mid):
                if rightMajeurePressure == 1:
                  i01.rightHand.majeure.stop()
                  i01.rightHand.majeure.disable()                  
              if pinsRight[pin].value>=(right_majeure_Psi_mid)and pinsRight[pin].value<(right_majeure_Psi_max):
                if rightMajeurePressure <= 2:
                  i01.rightHand.majeure.stop()
                  i01.rightHand.majeure.disable()
              if pinsRight[pin].value>=(right_majeure_Psi_max):
                if rightMajeurePressure <= 3:
                  i01.rightHand.majeure.stop()
                  i01.rightHand.majeure.disable()
              print "rightMajeureSensorPin:",right_majeurePin,"Value:",pinsRight[pin].value

            if pinsRight[pin].address==(right_ringFingerPin):
              if pinsRight[pin].value<=(right_ringFinger_Psi_min) and pinsRight[pin].value<(right_ringFinger_Psi_low):rightRingFingerPressure = 0
              if pinsRight[pin].value>=(right_ringFinger_Psi_low)and pinsRight[pin].value<(right_ringFinger_Psi_mid):
                if rightRingFingerPressure == 1:
                  i01.rightHand.ringFinger.stop()
                  i01.rightHand.ringFinger.disable()
              if pinsRight[pin].value>=(right_ringFinger_Psi_mid)and pinsRight[pin].value<(right_ringFinger_Psi_max):
                if rightRingFingerPressure <= 2:
                  i01.rightHand.ringFinger.stop()
                  i01.rightHand.ringFinger.disable()
              if pinsRight[pin].value>=(right_ringFinger_Psi_max):
                if rightRingFingerPressure <= 3:
                  i01.rightHand.ringFinger.stop()
                  i01.rightHand.ringFinger.disable()
              print "rightRingFingerSensorPin:",right_ringFingerPin,"Value:",pinsRight[pin].value

            if pinsRight[pin].address==(right_pinkyPin):
              if pinsRight[pin].value<=(right_pinky_Psi_min) and pinsRight[pin].value<(right_pinky_Psi_low):rightPinkyPressure = 0
              if pinsRight[pin].value>=(right_pinky_Psi_low)and pinsRight[pin].value<(right_pinky_Psi_mid):
                if rightPinkyPressure == 1:
                  i01.rightHand.pinky.stop()
                  i01.rightHand.pinky.disable()
              if pinsRight[pin].value>=(right_pinky_Psi_mid)and pinsRight[pin].value<(right_pinky_Psi_max):
                if rightPinkyPressure <= 2:
                  i01.rightHand.pinky.stop()
                  i01.rightHand.pinky.disable()
              if pinsRight[pin].value>=(right_pinky_Psi_max):
                if rightPinkyPressure <= 3:
                  i01.rightHand.pinky.stop()
                  i01.rightHand.pinky.disable()
              print "rightPinkySensorPin:",right_pinkyPin,"Value:",pinsRight[pin].value
              print "-----------Right-Finger-Sensors-----------"

            if pinsRight[pin].address==(right_extraPin):
              if pinsRight[pin].value<=(right_extra_Psi_min) and pinsRight[pin].value<(right_extra_Psi_low):rightExtraPressure = 0
              if pinsRight[pin].value>=(right_extra_Psi_low)and pinsRight[pin].value<(right_extra_Psi_mid):rightExtraPressure = 1
              if pinsRight[pin].value>=(right_extra_Psi_mid)and pinsRight[pin].value<(right_extra_Psi_max):rightExtraPressure = 2
              if pinsRight[pin].value>=(right_extra_Psi_max):rightExtraPressure = 3
              print "rightExtraSensorPin:",right_extraPin,"Value:",pinsRight[pin].value

    rightHandSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'rightHandSensorArduino'))
    rightHandSensorArduino.addListener("publishPinArray","python","publishRightSensor")
    talkEvent(lang_startingRightHandSensor)
    
    def rightHandSensorON():
      if rightHandSensorActivated:
        print "=========RightSensorON========" 
        rightHandSensorArduino.enablePin(right_thumbPin,2) #2 is the number of polls per seconds
        rightHandSensorArduino.enablePin(right_indexPin,2)
        rightHandSensorArduino.enablePin(right_majeurePin,2)
        rightHandSensorArduino.enablePin(right_ringFingerPin,2)
        rightHandSensorArduino.enablePin(right_pinkyPin,2)
        #rightHandSensorArduino.enablePin(right_extraPin,1)
      else:
        pass

    def rightHandSensorOFF():
      #sleep(5)
      if rightHandSensorActivated:
        rightHandSensorArduino.disablePin(right_thumbPin)
        rightHandSensorArduino.disablePin(right_indexPin)
        rightHandSensorArduino.disablePin(right_majeurePin)
        rightHandSensorArduino.disablePin(right_ringFingerPin)
        rightHandSensorArduino.disablePin(right_pinkyPin)
        rightHandSensorArduino.disablePin(right_extraPin)
        print "=========RightSensorOFF======="
      else:
        pass
    
  except:
    errorSpokenFunc('BAdrduinoChoosen','right Hand Sensor')
    rightHandSensorActivated=False
    pass

if leftHandSensorActivated:
  
  try:
    # common left pin listener function
    def publishLeftSensor(pinsLeft):
          print ""
                
          global leftThumbPressure
          global leftIndexPressure
          global leftMajeurePressure
          global leftRingFingerPressure
          global leftPinkyPressure
          global leftExtraPressure
          

          
          for pin in range(0, len(pinsLeft)):
            if pinsLeft[pin].address==(left_thumbPin):
              if pinsLeft[pin].value<=(left_thumb_Psi_min) and pinsLeft[pin].value<(left_thumb_Psi_low):leftThumbPressure = 0 
              if pinsLeft[pin].value>=(left_thumb_Psi_low)and pinsLeft[pin].value<(left_thumb_Psi_mid):
                if leftThumbPressure == 1:
                  i01.leftHand.thumb.stop()
                  i01.leftHand.thumb.disable()
              if pinsLeft[pin].value>=(left_thumb_Psi_mid)and pinsLeft[pin].value<(left_thumb_Psi_max):
                if leftThumbPressure <= 2:
                  i01.leftHand.thumb.stop()
                  i01.leftHand.thumb.disable()
              if pinsLeft[pin].value>=(left_thumb_Psi_max):
                if leftThumbPressure <= 3:
                  i01.leftHand.thumb.stop()
                  i01.leftHand.thumb.disable()
              print "leftThumbSensorPin:",left_thumbPin,"Value:",pinsLeft[pin].value

            if pinsLeft[pin].address==(left_indexPin):
              if pinsLeft[pin].value<=(left_index_Psi_min) and pinsLeft[pin].value<(left_index_Psi_low):leftIndexPressure = 0
              if pinsLeft[pin].value>=(left_index_Psi_low)and pinsLeft[pin].value<(left_index_Psi_mid):
                if leftIndexPressure == 1:
                  i01.leftHand.index.stop()
                  i01.leftHand.index.disable()
              if pinsLeft[pin].value>=(left_index_Psi_mid)and pinsLeft[pin].value<(left_index_Psi_max):
                if leftIndexPressure <= 2:
                  i01.leftHand.index.stop()
                  i01.leftHand.index.disable()
              if pinsLeft[pin].value>=(left_index_Psi_max):
                if leftIndexPressure <= 3:
                  i01.leftHand.index.stop()
                  i01.leftHand.index.disable()
              print "leftIndexSensorPin:",left_indexPin,"Value:",pinsLeft[pin].value

            if pinsLeft[pin].address==(left_majeurePin):
              if pinsLeft[pin].value<=(left_majeure_Psi_min) and pinsLeft[pin].value<(left_majeure_Psi_low):leftMajeurePressure = 0
              if pinsLeft[pin].value>=(left_majeure_Psi_low)and pinsLeft[pin].value<(left_majeure_Psi_mid):
                if leftMajeurePressure == 1:
                  i01.leftHand.majeure.stop()
                  i01.leftHand.majeure.disable()
              if pinsLeft[pin].value>=(left_majeure_Psi_mid)and pinsLeft[pin].value<(left_majeure_Psi_max):
                if leftMajeurePressure <= 2:
                  i01.leftHand.majeure.stop()
                  i01.leftHand.majeure.disable()
              if pinsLeft[pin].value>=(left_majeure_Psi_max):
                if leftMajeurePressure <= 3:
                  i01.leftHand.majeure.stop()
                  i01.leftHand.majeure.disable()
              print "leftMajeureSensorPin:",left_majeurePin,"Value:",pinsLeft[pin].value

            if pinsLeft[pin].address==(left_ringFingerPin):
              if pinsLeft[pin].value<=(left_ringFinger_Psi_min) and pinsLeft[pin].value<(left_ringFinger_Psi_low):leftRingFingerPressure = 0
              if pinsLeft[pin].value>=(left_ringFinger_Psi_low)and pinsLeft[pin].value<(left_ringFinger_Psi_mid):
                if leftRingFingerPressure == 1:
                  i01.leftHand.ringFinger.stop()
                  i01.leftHand.ringFinger.disable()
              if pinsLeft[pin].value>=(left_ringFinger_Psi_mid)and pinsLeft[pin].value<(left_ringFinger_Psi_max):
                if leftRingFingerPressure <= 2:
                  i01.leftHand.ringFinger.stop()
                  i01.leftHand.ringFinger.disable()
              if pinsLeft[pin].value>=(left_ringFinger_Psi_max):
                if leftRingFingerPressure <= 3:
                  i01.leftHand.ringFinger.stop()
                  i01.leftHand.ringFinger.disable()
              print "leftRingFingerSensorPin:",left_ringFingerPin,"Value:",pinsLeft[pin].value

            if pinsLeft[pin].address==(left_pinkyPin):
              if pinsLeft[pin].value<=(left_pinky_Psi_min) and pinsLeft[pin].value<(left_pinky_Psi_low):leftPinkyPressure = 0
              if pinsLeft[pin].value>=(left_pinky_Psi_low)and pinsLeft[pin].value<(left_pinky_Psi_mid):
                if leftPinkyPressure == 1:
                  i01.leftHand.pinky.stop()
                  i01.leftHand.pinky.disable()
              if pinsLeft[pin].value>=(left_pinky_Psi_mid)and pinsLeft[pin].value<(left_pinky_Psi_max):
                if leftPinkyPressure <= 2:
                  i01.leftHand.pinky.stop()
                  i01.leftHand.pinky.disable()
              if pinsLeft[pin].value>=(left_pinky_Psi_max):
                if leftPinkyPressure <= 3:
                  i01.leftHand.pinky.stop()
                  i01.leftHand.pinky.disable()
              print "leftPinkySensorPin:",left_pinkyPin,"Value:",pinsLeft[pin].value
              print "-----------Left-Finger-Sensors-----------"
              
            if pinsLeft[pin].address==(left_extraPin):
              if pinsLeft[pin].value<=(left_extra_Psi_min) and pinsLeft[pin].value<(left_extra_Psi_low):leftExtraPressure = 0
              if pinsLeft[pin].value>=(left_extra_Psi_low)and pinsLeft[pin].value<(left_extra_Psi_mid):leftExtraPressure = 1
              if pinsLeft[pin].value>=(left_extra_Psi_mid)and pinsLeft[pin].value<(left_extra_Psi_max):leftExtraPressure = 2
              if pinsLeft[pin].value>=(left_extra_Psi_max):leftExtraPressure = 3
              print "leftExtraSensorPin:",left_extraPin,"Value:",pinsLeft[pin].value  

    leftHandSensorArduino=eval(ThisServicePartConfig.get('MAIN', 'leftHandSensorArduino'))
    leftHandSensorArduino.addListener("publishPinArray","python","publishLeftSensor")
    talkEvent(lang_startingLeftHandSensor)
    
    def leftHandSensorON():
      if leftHandSensorActivated:
        print "=========LeftSensorON========" 
        leftHandSensorArduino.enablePin(left_thumbPin,2) #1 is the number of polls per seconds
        leftHandSensorArduino.enablePin(left_indexPin,2)
        leftHandSensorArduino.enablePin(left_majeurePin,2)
        leftHandSensorArduino.enablePin(left_ringFingerPin,2)
        leftHandSensorArduino.enablePin(left_pinkyPin,2)
        #leftHandSensorArduino.enablePin(left_extraPin,1)

    def leftHandSensorOFF():
      #sleep(5)
      if leftHandSensorActivated:
        leftHandSensorArduino.disablePin(left_thumbPin)
        leftHandSensorArduino.disablePin(left_indexPin)
        leftHandSensorArduino.disablePin(left_majeurePin)
        leftHandSensorArduino.disablePin(left_ringFingerPin)
        leftHandSensorArduino.disablePin(left_pinkyPin)
        leftHandSensorArduino.disablePin(left_extraPin)
        print "=========LeftSensorOFF======="
    
  except:
    errorSpokenFunc('BAdrduinoChoosen','left Hand Sensor')
    leftHandSensorActivated=False
    pass
