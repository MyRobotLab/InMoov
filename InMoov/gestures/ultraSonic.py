def ultraSonic(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicSensorDistance()).replace(".0", ""))