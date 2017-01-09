
# inmoov
inmoov repo

Copy all to mrl root

bugs : https://github.com/MyRobotLab/inmoov/issues

topic : http://myrobotlab.org/content/inmoov-script-merge-them-all

[DOCUMENTATION]

Main Folder
Inmoov.py > the main script ( very tiny, also called Fingerstarter )
Inmoov.config > Basic user configuration inside ( arduino com, language, voice/ear engine ... )

inmoovVocal

Inmoov can listen with the help of service ear "webkitspeechrecognition"
To interpret the recognized text you have the choice of 2 engines :
ear.addCommand > it's is hardcoded text, very EASY to use ear.commands and script actions
chatbot > Very powefull AIML engine ( not yet implemented ) . This is the engine of "Full Inmoov"
So, every ear.commands from Gael minimal script will be inside languagePack\ear.addCommand
It is very easy to translate minimal scripts, all is in one place
TODO : need to carefully work about chatbot/ear.commands conflicts

inmoovGestures

Inside this folder you can find all preprogammed gestures of inmoov, like "Open the right hand" "Da Vinci"...
Those gesture are often associate with a ear.command from the previous folder. But not necessarie ( exemple if those gesture are called by a timer or a chatbot action )

inmoovSkeleton

You will find every Inmoov official skeleton parts ( leftHand, RightArm etc... ) .
Every part is optional and we can chose to launch one part or the whole robot
Every skeleton parts is associated with a .config file : to put individual parameters inside ( min/max servo value, default speed ... )
This is the folder you can put optional mods and extra servos inside, like bob's neck and many others

inmoovLife

WIP idea about timers and automations

inmoovCustom

Never deleted file when script update. You can script your own inmoov inside it and take advantages of the basics already loaded.

Services

We load inside this folder every optional (or not) MRL services used by the script ( exemple arduino/neopixel )

system

Core and init levels
