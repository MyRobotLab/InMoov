# 10/05/2015
# Load a mp3 sound from the Web URL and save it localy (by default the  directory from where you start MRL
# test on Pc-win7 only...

from org.myrobotlab.service import Speech

import urllib2
import os

# The directory where the file will be saved default = current directory
#currentdir=os.getcwd()
# To set a directory
# os.chdir("h:/mrl/sound")
os.chdir("C:/myrobotlab/myrobotlab.1.0.1920/audioFile")

# the name of the local file
# remove the file if it already exist in the Audiofile directory
#soundfilename="startupsound.mp3";

try:
	mp3file = urllib2.urlopen('https://github.com/MyRobotLab/pyrobotlab/blob/master/home/hairygael/MP3/startupsound.mp3')
	output = open(soundfilename,'wb')
	output.write(mp3file.read())
	output.close()
except IOError:
	print "Check access right on the directory"
except Exception:
	print "Can't get the sound File ! Check internet Connexion"

# Start the sound...
mouth = Runtime.createAndStart("mouth","Speech")
mouth.audioFile.playFile(currentdir+"/"+soundfilename, False)
