## Yolo filter / 2 samples : what do you see / LOOKING FOR THE *
## WARNING, memory overflow if yolo filter executed multiple times...
## as a temporary workarround for the demo, yolo filter + camera capture is not disabled after inventory, so you can execute it multiple times
# We classify objects per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time
# Also get given element (label) position if set, from all others in the field off view, from left to right

# "collection" is the dictionary for detected objects in given time
# after aquisition, we will read collection content to play with it
collection=[]
# filter, maybe we don't want to inventory every objects, like the table ['table','cow','chair'...]
filteredObjects=['sample1','sample2']

def startYoloInventory(duration):
  talk(chatBot.getPredicate("startupSentence"))
  startYolo(duration)
  # interpret results ...
  collectionString=""
  for key, value in countYolo().iteritems():
    collectionString=collectionString+str(value)+" "+key+", "
  #check if we have results, return key "none" if no ( aiml will understand the key 'none' )
  print collection
  if len(collectionString) == 0:collectionString="none"
  # return results
  chatBot.setPredicate("yoloTotalDetected",str(len(collection)))
  return collectionString

def getYoloPosition(label):
  position=0
  for x in collection:
    if x[0]==label:position=collection.index(x)+1
  # to not launch gesture, comment showObject :
  print "Position of : ",label,position
  showObject(position)
  return position  

## i01.opencv configuration for yolo publisher
  
# TODO classify while head moves ! ( count )
# TODO what do you see in front of you ( few centimeters -> use gael mods )
# TODO tranlate coco
# TODO ...

#main function to read yolo filter output
def onClassification(classifications):
  print classifications
  global collection
  label=[]
  
  # iterate over the frame and clean up previous results based on actual detection ( update positions + count elements )
  # todo cleaner method to extract data...
  for id, documents in classifications.items():
    for document in documents:
      object=document.getLabel()
      for y in collection:
        if object in y:
          collection.remove(y)
          break

  # iterate over the frame and extract classified objects ( TODO this inside java land to publish it ? )
  for id, documents in classifications.items():
    for document in documents:
      object=document.getLabel()
      xPos=document.getBoundingBox().x
      if not object in filteredObjects:collection.append([object,xPos])      

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
  #start i01.opencv + yolo filter
  i01.cameraOn()
  i01.vision.setActiveFilter("Yolo")
  # wait for X ( todo unlimited, until STOP vocal command ? )
  sleep(duration)
  i01.cameraOff()
  
  #sort results
  collection = sorted(collection, key=lambda k: int(k[1]))
  print collection
