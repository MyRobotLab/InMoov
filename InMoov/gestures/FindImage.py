def FindImage(image):
  RetourServer=Parse("http://www.myai.cloud/version.html")
  try:
    image = image.decode( "utf8" )
  except: 
    pass
  a = Parse("http://www.myai.cloud/bot1.php?type=pic&pic="+urllib2.quote(image).replace(" ", "%20"))
  
  displayPic(a)
  print "http://www.myai.cloud/bot1.php?type=pic&pic="+urllib2.quote(image).replace(" ", "%20")
#Light(1,1,1)
