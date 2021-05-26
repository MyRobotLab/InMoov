def ultraSonicRight(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicRightDistance()).replace(".0", ""))