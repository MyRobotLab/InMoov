def FindImage(image):
  RetourServer=Parse("http://www.myai.cloud/version.html")
  try:
    image = image.decode( "utf8" )
  except: 
    pass
  #mouth.speak(image)
  #PLEASE USE REAL LANGUAGE PARAMETER :
  #lang=XX ( FR/EN/RU/IT etc...)
  #A FAKE LANGUAGE WORKS BUT DATABASE WILL BROKE
  a = Parse(BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20"))
  
  DisplayPic(a)
  print BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20")
#Light(1,1,1)