def DisplayPic(pic):
  r=0
  try:
    r=image.displayFullScreen(pic,1)
  except: 
    inmoovWebKit.getResponse("PICTUREPROBLEM")
    pass
  time.sleep(0.1)
  try:
    r=image.displayFullScreen(pic,1)
  except:
      pass