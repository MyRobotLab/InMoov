## Yolo gesture poc
# Cumulative frames analysis :
# We count objetcs per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time

# collection is the dictionary for detected objects in given time
# after aquisition, we will read collection content
collection={}
def startYoloInventory(duration):
  talk(chatBot.getPredicate(chatBot.getCurrentUserName(),"startupSentence"))
  global collection
  collection={}
  #start opencv + yolo filter
  i01.opencv.capture()
  i01.opencv.removeFilters()
  i01.opencv.addFilter("PyramidDown")
  i01.opencv.addFilter("Yolo")
  # wait for X ( todo unlimited, until STOP vocal command ? )
  sleep(duration)
  i01.opencv.removeFilters()
  i01.opencv.stopCapture()
  # class results ...
  collectionString=""
  for key, value in collection.iteritems():
    collectionString=collectionString+str(value)+" "+str(key)+", "
  #check if we have results, return key "none" if no ( aiml will understand the key )
  print collectionString
  if len(collectionString) == 0:collectionString="none"
  return collectionString
  

## OpenCV configuration for yolo publisher
  
python.subscribe("i01.opencv", "publishYoloClassification")  
# TODO classify while head moves ! ( count )
# TODO what do you see in front of you ( few centimeters -> use gael mods )
# TODO tranlate coco
# TODO ...

def onYoloClassification(data):
  global collection

  label=[]
  # iterate over the frame and extract classified objects ( TODO this inside java land to publish it ? )
  for x in data:
    object=str(x).split(",")[3].replace("label=","")
    label.append(object)
  # count objects detected
  for key, group in itertools.groupby(label):
    if key in collection:
      #we append exiting object only if we found a greater value ( by exemple there is 3 persons in the room and the 3rd was hidden from now )
      if int(collection[key]) <= label.count(key):
      	collection[key]=label.count(key)
    else:
      # object never detected
      collection[key]=label.count(key)