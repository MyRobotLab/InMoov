# -- coding: utf-8 --

def story():
  i01.startedGesture()
  sleep(2)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(79,100)
  i01.moveArm("left",5,119,28,15)
  i01.moveArm("right",5,111,28,15)
  i01.moveHand("left",42,58,87,55,71,35)
  i01.moveHand("right",81,20,82,60,105,113)
  
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(124,90)
  i01.moveArm("left",89,94,91,35)
  i01.moveArm("right",20,67,31,22)
  i01.moveHand("left",106,41,161,147,138,90)
  i01.moveHand("right",0,0,0,54,91,90)
 
  sleep(1)
  i01.setHandSpeed("left", 0.85, 0.85, 1.0, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(105,76);
  i01.moveArm("left",89,106,103,35);
  i01.moveArm("right",35,67,31,22);
  i01.moveHand("left",106,0,0,147,138,7);
  i01.moveHand("right",0,0,0,54,91,90);
  
  sleep(0.2)
  i01.setHandSpeed("left", 0.85, 0.85, 1.0, 1.0, 1.0, 0.85)
  i01.moveHand("left",106,0,0,0,0,7);
  
  sleep(0.5)
  i01.setHandSpeed("left", 0.85, 0.9, 0.9, 0.9, 0.9, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(90,40);
  i01.moveArm("left",89,106,103,35);
  i01.moveArm("right",35,67,31,20);
  i01.moveHand("left",106,140,140,140,140,7);
  i01.moveHand("right",0,0,0,54,91,90);
  
  sleep(0.5)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(105,125);
  i01.setArmSpeed("left", 0.9, 0.9, 0.9, 0.9)
  i01.moveArm("left",60,100,85,30);
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(40,56);
  sleep(0.5)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
  i01.setArmSpeed("right", 0.5, 0.6, 0.5, 0.6);
  i01.moveArm("left",87,41,64,11)
  i01.moveArm("right",5,95,40,11)
  i01.moveHand("left",98,150,160,160,160,104)
  i01.moveHand("right",0,0,50,54,91,90);
  
  i01.moveHead(40,67);
  sleep(2)
  i01.setHandSpeed("left", 0.8, 0.9, 0.8, 0.8, 0.8, 0.8)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.8, 0.8)
  i01.moveHead(43,69)
  i01.moveArm("left",87,41,64,11)
  i01.moveArm("right",5,95,40,42)
  i01.moveHand("left",42,0,100,80,113,35)
  i01.moveHand("left",42,10,160,160,160,35)
  i01.moveHand("right",81,20,82,60,105,113)
  
  sleep(1)
  i01.moveHead(37,60);
  i01.setHandSpeed("left", 1.0, 1.0, 0.9, 0.9, 1.0, 0.8)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.moveArm("right",5,95,67,42)
  i01.moveHand("left",42,10,10,160,160,30)
  
  sleep(1)
  i01.moveHead(43,69);
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.moveArm("right",5,134,67,42)
  i01.moveHand("left",42,10,10,10,160,35)
  
  sleep(1)
  i01.setArmSpeed("right", 0.8, 0.8, 0.8, 0.8)
  i01.moveArm("right",20,90,45,16)
  
  sleep(1)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0);
  i01.moveHead(43,72)
  i01.moveArm("left",90,44,66,11)
  i01.moveArm("right",90,100,67,26)
  i01.moveHand("left",42,80,100,80,113,35)
  i01.moveHand("right",81,0,82,60,105,69)
  
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.8, 0.8)
  i01.moveHead(45,62)
  i01.moveArm("left",72,44,90,11)
  i01.moveArm("right",90,95,68,15)
  i01.moveHand("left",42,0,100,80,113,35)
  i01.moveHand("right",81,0,82,60,105,0)
  
  i01.moveHead(40,60)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
  i01.moveArm("left",72,44,90,9)
  i01.moveArm("right",90,95,68,15)
  i01.moveHand("left",42,0,100,80,113,35)
  i01.moveHand("right", 10, 140,82,60,105,10)
  
  sleep(0.5)
  i01.moveHand("left",42,0,100,80,113,35)
  i01.moveHand("right", 50, 51, 15,23, 30,140);
  
  i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8,0.8, 0.8)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.moveHand("left", 36, 52, 8,22, 20);
  i01.moveHand("right", 120, 147, 130,110, 125);
  removeleftarm()
  sleep(1)
  
  i01.moveHand("right",110,137,120,100,105,130);
  i01.setHeadSpeed(1,1)
  i01.setArmSpeed("right", 1.0,1.0, 1.0, 1.0);
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
  sleep(1)
  i01.finishedGesture()
  relax()
  sleep(2)
