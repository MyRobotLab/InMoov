## Yolo filter / 2 samples
## WARNING, memory overflow if yolo filter executed multiple times...
# We classify objects per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time
# "collection" is the dictionary for detected objects in given time
# after aquisition, we will read collection content to play with it


# Cumulative frames analysis :
# Also get given element (label) position if set, from all others in the field off view, from left to right
# todo add filter ( like "table" for elements onto )
collection=[]
def startYoloInventory(duration):
  talk(chatBot.getPredicate("startupSentence"))
  startYolo(duration)
  # interpret results ...
  collectionString=""
  for key, value in countYolo().iteritems():
    collectionString=collectionString+str(value)+" "+key+", "
  #check if we have results, return key "none" if no ( aiml will understand the key )
  print collection
  if len(collectionString) == 0:collectionString="none"
  # return results
  chatBot.setPredicate("yoloTotalDetected",str(len(collection)))
  return collectionString

def getYoloPosition(label):
  position=0
  for x in collection:
    if x[0]==label:position=collection.index(x)+1
  # return results
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
    x=unicode(repr(x),'utf-8')
    object=x.split(",")[3].replace("label=","").strip()
    for y in collection:
      if object in y:
        collection.remove(y)
        break

  # iterate over the frame and extract classified objects ( TODO this inside java land to publish it ? )
  for x in data:
    x=unicode(repr(x),'utf-8')
    object=x.split(",")[3].replace("label=","").strip()
    xPos=x.split(",")[0].replace("YoloDetectedObject [boundingBox=X:","") 
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
  if flipPicture:i01.opencv.addFilter("Flip")
  i01.opencv.addFilter("PyramidDown")
  i01.opencv.addFilter("Yolo")
  # wait for X ( todo unlimited, until STOP vocal command ? )
  sleep(duration)
  i01.opencv.removeFilters()
  i01.opencv.stopCapture()
  #sort results
  collection = sorted(collection, key=lambda k: int(k[1]))
  print collection