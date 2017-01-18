def thatwasfun():
  i01.mouth.speak("that was fun")
  i01.moveHead(90,90)
  i01.moveArm("left",85,106,25,18)
  i01.moveArm("right",87,107,32,18)
  i01.moveHand("left",110,62,56,88,81,145)
  i01.moveHand("right",78,88,101,95,81,27)
  i01.moveTorso(90,90,90)
  relax()

########################################
# The Walking Thread
# This is a thread that you can pass
# an inmoov and a servo to.  It will
# start walking forward and animating in a loop
########################################
class WalkingThread(threading.Thread):
  # constructor for the thread, takes i01 and forwardServo
  def __init__(self,i01,forwardServo):
    super(WalkingThread, self).__init__()
    print "Here we are"
    self.forwardServo = forwardServo
    self.i01 = i01
    # initially the thread is not running.
    self.running = False
  # The thread is started this method runs
  def run(self):
    # flip the state to running
    self.running = True
    # move the servo to go forward
    self.forwardServo.moveTo(60)
    # while we are running, animate
    while self.running:
      try:
        print "walking"
        fullspeed()
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.95, 0.95, 0.95, 0.85)
        i01.setArmSpeed("left", 0.95, 0.95, 0.95, 0.85)
        i01.setHeadSpeed(0.75, 0.75)
        i01.moveHead(70,79,85,85,65)
        i01.moveArm("left",5,90,10,10)
        i01.moveArm("right",15,90,40,10)
        i01.moveHand("left",92,33,37,71,66,10)
        i01.moveHand("right",81,66,82,60,105,100)
        i01.moveTorso(75,97,90)
      except:
        print "Unexpected error(1):", sys.exc_info()[0]
      sleep(1)
      try:
        print "thread..."
        i01.moveHead(79,100,85,85,65)
        i01.moveArm("left",15,84,43,15)
        i01.moveArm("right",5,82,10,20)
        i01.moveHand("left",92,33,37,71,66,50)
        i01.moveHand("right",81,66,82,60,105,150)
        i01.moveTorso(124,83,90)
      except:
        print "Unexpected error(2):", sys.exc_info()[0]
      sleep(1)
        # self.running = False
    # we are no longer running, move servo and relax.
    print "Stopped"
    forwardServo.moveTo(93)

#########################################################################

# Create a thread object that can be global ?
walkingThread = WalkingThread(i01,forwardServo)

