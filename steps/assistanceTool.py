
import serial, time
import codecs

class RelayTool:
    '''
    继电器控制，针对16口继电器读一个口的控制
    '''

    def __init__(self):
        self.com1 = serial.Serial(port='COM1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None)

    def controlPoweron(self):
        poweron1 = codecs.decode('005A560005010000B6',"hex_codec")
        if not self.com1.isOpen():
            self.com1.open()

        self.com1.write(poweron1)
        self.com1.close()


<<<<<<< HEAD
    def controlPoweroff(self):
=======
    def controlPoweroff(self,S):
>>>>>>> 564297e124f74aa7206984deb1f8eca4a7bb997f
        poweroff1 = codecs.decode('005A560006010000B7',"hex_codec")
        if not self.com1.isOpen():
            self.com1.open()
        self.com1.write(poweroff1)
        self.com1.close()


<<<<<<< HEAD
relays = RelayTool()

class PictureCapture:
    pass

relays.controlPoweron()
time.sleep(3)
relays.controlPoweroff()
=======
class PictureCapture:
    pass
>>>>>>> 564297e124f74aa7206984deb1f8eca4a7bb997f
