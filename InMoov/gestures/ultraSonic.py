
def ultraSonic(returnText):
  inMoov.mouth.speakBlocking(unicode(returnText,'utf-8')+str(inMoov.getUltrasonicSensorDistance()).replace(".0", ""))