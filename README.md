# InMooV - Service launcher v 1.0.0   

This is the full configurable internationnal launcher script for Inmoov service.  
Worky out of the box with standardized InMoov hardware configuration.  


![virtual inmoov screenshot](https://inmoov.fr/wp-content/uploads/2020/04/webgui49.png)

## Getting Started
MORE informations here : http://myrobotlab.org/service/InMoov  
  
At this time ( v 1.0.0 ) , configurable things are inside the config folder.   
By default virtual environment is started, so you can test things with no risk !  

![virtual inmoov screenshot](http://myrobotlab.org/sites/default/files/users/user3images/dual5.gif)
  
To start using the Finger Starter with real hardware, set :  
 ( The Finger Starter is considered here to be right index, so make sure your servo is connected to pin3 of you Arduino )  

```
ScriptType=RightSide | inside config/_InMoov.config  
MyRightPort=COMx | inside config/_service_6_Arduino.config  
isRightHandActivated=True | inside config/skeleton_rightHand.config  
voice command sample : OPEN HAND  
```

Check your configuration inside Inmoov.config ( exemple to change english to french )  
If you setup 2 arduino + configs in skeleton folder, it can run full Inmoov or separated parts ( right hand / head ... )  

  
### DOCUMENTATION & HELP  
http://myrobotlab.org/service/InMoov  
  
bugs report : https://github.com/MyRobotLab/inmoov/issues  

### CONTRIBUTION  
Is welcome :)  
( On the develop branch )  
  
### CHANGELOG  
   
0.9.9  
/ Testing...  
0.7.0  
/ Chatbots enhancements & fixes...  
0.6.1  
/ add AndroidSpeechRecognizer   
