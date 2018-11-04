python.subscribe(runtime,"shutdown")

def shutdownComplete():
  runtime.execute("cmd.exe","/c","shutdown.exe /s /t 30 /f")
  shutdown()
  
