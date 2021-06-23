# ##############################################################################
#            *** FROM InMoov3.minimalTorso.py ***
# ##############################################################################

def teststomach():
  sleep(1)
  i01.setNeopixelAnimation("Flash Random", 255, 255, 255, 1)
  i01.setTorsoSpeed(20,20,20)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.moveTorso(45,90,90)
  sleep(4)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.moveTorso(135,90,90)
  sleep(4)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.setNeopixelAnimation("Flash Random", 255, 0, 255, 1)
  i01.moveTorso(90,45,90)
  sleep(3)
  i01.moveTorso(90,135,90)
  sleep(3)
  i01.moveTorso(90,90,45)
  sleep(3)
  i01.moveTorso(90,90,135)
  i01.stopNeopixelAnimation()