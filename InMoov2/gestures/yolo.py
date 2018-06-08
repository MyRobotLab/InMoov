# BROKEN
# todo use opencv filter
#from java.lang import String
#from org.myrobotlab.service import Runtime
#from org.myrobotlab.service import OpenCV
#from time import sleep
#from shutil import copyfile
#import os, sys

#list=[]
#list2=[]
#cpt=0

#We need to start the camera before launching yolo
#yolo = Runtime.createAndStart("yolo","Yolo")

# ##############################################################################

# ##############################################################################
def takeFotoForYolo():
  print "Photo..."
  os.chdir("c:\yolo")

  photoFileName = opencv.recordSingleFrame()
  print photoFileName
  
  os.remove("image.jpg")
  os.rename(photoFileName,"image.jpg")
  copyfile("image.jpg", "c:\yolo\yolo\image.jpg")
  sleep(0.1)

  yolo.execYolo()

# ##############################################################################
def statisticResult():
  global list
  NbElement=0
  
  print "statistique..."
  res = yolo.StatisticResult()

  if res == True:
    # Ici il y a obligatoirement des objects
    list=[]
    file = open("statistics.txt","r")
	
    imagedisplay.display("c:\yolo\yolo\predictions.jpg")
	
    for ligne in file:
      list.append(ligne)
    file.close()
    
    NbElement=len(list)
    print "Number of recognized elements:", NbElement

    #inMoov.mouth.speak("I see")

    for val in list:
      print val
      #inMoov.mouth.speak(unicode(val, 'utf-8'))
      #sleep(2)
  else:
    print "Nothing found !!"
    #inMoov.mouth.speak("I see nothing")
  
# ##############################################################################
def analyseResult():
  global list
  NbElement=0
  #displayPic("c:\yolo\yolo\predictions.jpg")
  print "analyse..."
  res = yolo.AnalyseResult()

  if res == True:
    # Ici il y a obligatoirement des objects
    list=[]
    file = open("finalresult.txt","r")

    for ligne in file:
      list.append(ligne)
    file.close()
    
    NbElement=len(list)
	
    print "Number of recognized elements:", NbElement

    inMoov.mouth.speak("I see")
  
    for val in list:
      print val
      inMoov.mouth.speak(unicode(val, 'utf-8'))
      sleep(2)
  else:
    print "Nothing found !!"
    inMoov.mouth.speak("I see nothing")

##################################################################################
# Timer ...
##################################################################################
