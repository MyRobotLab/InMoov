def PlayUtub(q,num):
  if q=="stop" and num==0:
    subprocess.Popen("taskkill /F /T /PID %i"%proc1.pid , shell=True)
    sleep(2)
    webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
  else:
    webgui.startBrowser("http://www.myai.cloud/utub/?num="+str(num)+"&q="+str(q).encode('utf-8'))
#print "http://www.myai.cloud/utub/?num="+str(num)+"&q="+str(q).encode('utf-8')