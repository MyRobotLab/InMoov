import subprocess

def shutdownComplete():
  subprocess.call([r'E:/Documents/Myrobotlab/myrobotlab.1.0.2693.7/InMoov/custom/SHUTDOWN_pc_inmoov.bat'])
  sleep(1)
  shutdown()
  
##TODO Change the call to automatic filepath positionning  
  
