def ultraSonicLeft(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicLeftDistance()).replace(".0", ""))