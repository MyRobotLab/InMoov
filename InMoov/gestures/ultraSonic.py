def ultraSonic(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicRightDistance()).replace(".0", "")+str(i01.getUltrasonicLeftDistance()).replace(".0", ""))
