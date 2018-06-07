def power_down():
  relax()
  inMoov.powerDown()
  ##sleep(2)
  ##relax()
  ##inMoov.mouth.speakBlocking()
  ##sleep(2)
  ##inMoov.moveHead(40, 85);
  ##sleep(4)
  ##rightSerialPort.digitalWrite(53, Arduino.LOW)
  ##leftSerialPort.digitalWrite(53, Arduino.LOW)
  ear.lockOutAllGrammarExcept("power up")
  sleep(2)