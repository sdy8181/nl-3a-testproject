
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


    def controlPoweroff(self,S):
        poweroff1 = codecs.decode('005A560006010000B7',"hex_codec")
        if not self.com1.isOpen():
            self.com1.open()
        self.com1.write(poweroff1)
        self.com1.close()


class PictureCapture:
    pass