## Yolo filter / 2 samples : what do you see / WHERE IS THE *

# We classify objects per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time
# Also get given element (label) position if set, from all others in the field off view, from left to right

# "i01.vision.collectionCount" is the dictionary for detected objects in given time
# after aquisition & position sort, we will read collection content to play with it

## warning : yolo publisher is now inside java land to avoid threading issues because of python sleep

# filter, maybe we don't want to inventory every objects, like the table : i01.vision.filteredLabel.add("table");
i01.vision.filteredLabel.add("sample");

def startYoloInventory(duration):
  i01.speak(i01.chatBot.getPredicate("startupSentence"))
  sleep(5)
  if isNeopixelActivated==1:
    i01.setNeopixelAnimation("Color Wipe", 25, 5, 10, 15)
  enableYoloFor(duration)
  # interpret results ...
  collectionString=""
  for key, value in i01.vision.collectionCount.iteritems():
    collectionString=collectionString+str(value)+" "+key+", "
  #check if we have results, return key "none" if no ( aiml will understand the key 'none' )
  if len(collectionString) == 0:collectionString="none"
  # return results
  i01.chatBot.setPredicate("yoloTotalDetected",str(len(i01.vision.collectionCount)))
  return collectionString

def getYoloPosition(label):
  position=i01.vision.getPosition(label)
  # to not launch gesture, comment showObject :
  print "Position of : ",label,position
  showObject(position)
  return position  

# TODO classify while head moves ! ( count )
# TODO what do you see in front of you ( few centimeters -> use gael mods )

global lastPhotoFileName
#shared function to start & stop yolo filter
def enableYoloFor(duration):
  global lastPhotoFileName
  i01.vision.collectionCount.clear()
  i01.vision.collectionPositions.clear()
  #start i01.opencv
  i01.cameraOn()
  # yolo filter in the pipeline ( add if no exist + enable + setActive )
  i01.vision.setActiveFilter("Yolo")
  try:
    gui.setActiveTab("i01.opencv")
    #os.remove(lastPhotoFileName)
    imagedisplay.closeAll()
  except:
    pass
  # wait for X
  sleep(duration)
  lastPhotoFileName = i01.opencv.recordFrame()
  #print lastPhotoFileName
  imagedisplay.display(lastPhotoFileName)
  i01.opencv.disableFilter("Yolo")
  print i01.vision.collectionCount
