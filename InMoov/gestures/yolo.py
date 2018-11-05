## Yolo filter / 2 samples
# We classify objects per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time
# "collection" is the dictionary for detected objects in given time
# after aquisition, we will read collection content to play with it


# Cumulative frames analysis :
collection=[]
def startYoloInventory(duration):
  talk(chatBot.getPredicate(chatBot.getCurrentUserName(),"startupSentence"))
  startYolo(duration)
  # interpret results ...
  collectionString=""
  for key, value in countYolo().iteritems():
    collectionString=collectionString+str(value)+" "+str(key)+", "
  #check if we have results, return key "none" if no ( aiml will understand the key )
  print collection
  if len(collectionString) == 0:collectionString="none"
  return collectionString

  
# function to get given element (label) position, from all others in the field off view, from left to right
# todo add filter ( like "table" for elements onto )
def getYoloPosition(duration,label):
  talk(chatBot.getPredicate(chatBot.getCurrentUserName(),"startupSentence"))
  startYolo(duration)
  position=0
  for x in sortLeftRightYolo():
    if x[0]==label:position=sortLeftRightYolo().index(x)+1
  return position
  

## OpenCV configuration for yolo publisher
  
python.subscribe("i01.opencv", "publishYoloClassification")  
# TODO classify while head moves ! ( count )
# TODO what do you see in front of you ( few centimeters -> use gael mods )
# TODO tranlate coco
# TODO ...

#main function to read yolo filter output
def onYoloClassification(data):
  global collection
  label=[]
  
  # iterate over the frame and clean up previous results based on actual detection ( update positions + count elements )
  # todo cleaner method to extract data...
  for x in data:
    object=str(x).split(",")[3].replace("label=","").strip()
    for y in collection:
      if object in y:
        collection.remove(y)
        break

  # iterate over the frame and extract classified objects ( TODO this inside java land to publish it ? )
  for x in data:
    object=str(x).split(",")[3].replace("label=","").strip()
    xPos=str(x).split(",")[0].replace("YoloDetectedObject [boundingBox=X:","") 
    collection.append([object,xPos])      

#shared function to count classified elements
def countYolo():
  yoloDic={}
  for yoloLabel in collection:
    if yoloLabel[0] in yoloDic:
      yoloDic[yoloLabel[0]]=yoloDic[yoloLabel[0]]+1
    else:
      yoloDic[yoloLabel[0]]=1
  return yoloDic
  
#shared function to start & stop yolo filter
def startYolo(duration):
  global collection
  collection=[]
  #start opencv + yolo filter
  i01.opencv.capture()
  i01.opencv.removeFilters()
  i01.opencv.addFilter("PyramidDown")
  i01.opencv.addFilter("Yolo")
  # wait for X ( todo unlimited, until STOP vocal command ? )
  sleep(duration)
  i01.opencv.removeFilters()
  i01.opencv.stopCapture()
  print collection
  
#shared function to sort elements from left to right
def sortLeftRightYolo():
  sortedObject = sorted(collection, key=lambda k: int(k[1]))
  return sortedObject