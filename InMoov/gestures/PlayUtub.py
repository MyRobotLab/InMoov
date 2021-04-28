
def PlayUtub(q,id):
  subprocess.call("taskkill /IM vlc.exe /F")
  if q=="stop":
    MoveHeadTimer.stopClock()
    subprocess.call("taskkill /IM vlc.exe /F")
  if q=="listen":
    MoveHeadTimer.startClock()
    p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","http://www.myai.cloud/utub/list/tub.php?num=1&q="+str(id).encode('utf-8'),"--no-video","vlc://quit"])
#todo watch  