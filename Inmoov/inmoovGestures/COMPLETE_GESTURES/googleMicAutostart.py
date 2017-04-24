#autorestart 15 seconds
def WebkitSpeachReconitionON(timedata):
  agreeanswer()
  try:
    ear.startListening()
  except:
    pass

    #clock declaration
    WebkitSpeachReconitionFix = Runtime.start("WebkitSpeachReconitionFix","Clock")
    WebkitSpeachReconitionFix.setInterval(15000)
    WebkitSpeachReconitionFix.addListener("pulse", python.name, "WebkitSpeachReconitionON")
    WebkitSpeachReconitionFix.startClock()

  