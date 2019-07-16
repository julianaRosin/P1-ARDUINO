import serial
import time

class Comm:
    def __init__(self):
        self.rcb = ''
        self.rcb_final = ''
        self.tam_rcb = 6

    def connecta_porta(self):
        self.port = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=1)

    def ler_porta(self):
        self.rcb = self.port.read(self.tam_rcb).decode('ascii','ignore')
        print('rcb: ',self.rcb)
        self.port.flushInput()

    def escreve_porta(self,frame):
        x = bytearray(frame,'utf-8')
        self.port.write(x)

    def trata_valor_recebido(self):
        self.rcb_final = ''
        if self.rcb !='':
            if self.rcb[0]=='*' and self.rcb[-1] == '#':
                self.rcb_final+=self.rcb[-2]+ self.rcb[1:4]
            elif self.rcb[0]=='*' and self.rcb[-2] == '#':
                self.rcb_final+=self.rcb[3]+ self.rcb[1:3]
            elif self.rcb[0]=='*' and self.rcb[3] == '#':
                self.rcb_final+=self.rcb[2]+ self.rcb[1]
        self.port.flushInput()

    def get_valor_porta(self):
        return self.rcb_final
    
    def desconecta_porta(self):
        self.port.close()

    def rotina(self):
        self.ler_porta()
        self.trata_valor_recebido()
        return self.get_valor_porta()


