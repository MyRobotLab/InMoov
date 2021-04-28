def power_down():
  relax()
  i01.powerDown()
  ##sleep(2)
  ##relax()
  ##i01.mouth.speakBlocking()
  ##sleep(2)
  ##i01.moveHead(40, 85);
  ##sleep(4)
  ##rightSerialPort.digitalWrite(53, Arduino.LOW)
  ##leftSerialPort.digitalWrite(53, Arduino.LOW)
  ear.lockOutAllGrammarExcept("power up")
  sleep(2)