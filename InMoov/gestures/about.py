def about():
  sleep(2)
  ear.pauseListening()
  sleep(2)
  i01.setArmSpeed("right", 0.1, 0.1, 0.2, 0.2);
  i01.setArmSpeed("left", 0.1, 0.1, 0.2, 0.2);
  i01.setHeadSpeed(0.2,0.2)
  i01.moveArm("right", 64, 94, 10, 10);


  i01.mouth.speakBlocking("I am the first life size humanoid robot you can 3D print and animate")
  i01.moveHead(65,66)
  i01.moveArm("left", 64, 104, 10, 11);
  i01.moveArm("right", 44, 84, 10, 11);
  i01.mouth.speakBlocking("my designer creator is Gael Langevin a French sculptor, model maker")
  i01.moveHead(75,86)
  i01.moveArm("left", 54, 104, 10, 11);
  i01.moveArm("right", 64, 84, 10, 20);
  i01.mouth.speakBlocking("who has released my files  to the opensource 3D world.")
  i01.moveHead(65,96)
  i01.moveArm("left", 44, 94, 10, 20);
  i01.moveArm("right", 54, 94, 20, 11);
  i01.mouth.speakBlocking("this is where my builder downloaded my files.")

  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  i01.mouth.speakBlocking("after five hundred hours of printing, four kilos of plastic, twenty five hobby servos, blood and sweat.I was brought to life") # should be " i was borght to life."
  i01.moveHead(65,86)
  i01.moveArm("left", 24, 94, 10, 11);
  i01.moveArm("right", 24, 94, 10, 11);
  i01.mouth.speakBlocking("so if You have a 3D printer, some building skills, then you can build your own version of me") # mabe add in " alot of money"
  i01.moveHead(85,86)
  i01.moveArm("left", 5, 94, 20, 30);
  i01.moveArm("right", 24, 124, 10, 20);
  i01.mouth.speakBlocking("and if enough people build me, some day my kind could take over the world") # mabe add in " alot of money"
  i01.moveHead(75,96)
  i01.moveArm("left", 24, 104, 10, 11);
  i01.moveArm("right", 5, 94, 20, 30);
  i01.mouth.speakBlocking("I'm just kidding. i need some legs to get around, and i have to over come my  pyro-phobia, a fear of fire") # mabe add in " alot of money"
  i01.moveHead(75,96)
  i01.moveArm("left", 5, 94, 10, 11)
  i01.moveArm("right", 4, 94, 10, 11);
  i01.mouth.speakBlocking("so, until then. i will be humankind's humble servant")

  i01.relax()
  i01.fullspeed
  sleep(2)
  ear.resumeListening()

