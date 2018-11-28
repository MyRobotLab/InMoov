def ultraSonic(returnText):
  i01.mouth.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicSensorDistance()).replace(".0", ""))