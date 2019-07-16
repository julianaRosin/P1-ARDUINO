from tkinter import *
from Comunicacao import *

class Application:
    def __init__(self, janela_pai):
        self.cl_janela_pai = janela_pai
        self.flag_sinal = 0
        self.flag_conn = False
        self.cl_conn = Comm()
        self.carrega_imagens()
        self.mostra_layout_janela()
        self.atualiza_sinal()
    
    def mostra_layout_janela(self):
        
        self.lb_logo = Label(self.cl_janela_pai,image=self.ph_logo,borderwidth=0)
        self.lb_logo.imagem = self.ph_logo 
        self.lb_logo.place(x=0,y=0)

        self.lb_distancia = Label(self.cl_janela_pai, text='Distância: XX cm')
        self.lb_distancia.configure(bg='white',font=('arial','14','bold'))
        self.lb_distancia.place(x=30,y=150)

        self.lb_sinal = Label(self.cl_janela_pai,image=self.ph_sinal_off)
        self.lb_sinal.configure(borderwidth=0,bg='white')
        self.lb_sinal.imagem = self.ph_sinal_off 
        self.lb_sinal.place(x=200,y=200)

        self.bt_conn = Button(self.cl_janela_pai,text='Conectar',command=self.command_conecta_porta)
        self.bt_conn.configure(bg='#1B6DC1',fg='white')
        self.bt_conn.place(x=30,y=350)

    def carrega_imagens(self):
        self.ph_logo = PhotoImage(file='img/logo.png')
        self.ph_sinal_off = PhotoImage(file='img/off.png')
        self.ph_sinal_red = PhotoImage(file='img/red.png')
        self.ph_sinal_green = PhotoImage(file='img/green.png')
        self.ph_sinal_yellow = PhotoImage(file='img/yellow.png')

    def atualiza_sinal(self):
        if self.flag_conn:
            valor = self.cl_conn.rotina()
            if valor !='':
                distancia = valor[1:]
                self.flag_sinal = valor[0]
                self.lb_distancia['text'] = 'Distância: ' + distancia + 'cm'
                if self.flag_sinal == 'g':
                    self.lb_sinal['image'] = self.ph_sinal_green
                    self.lb_sinal.imagem = self.ph_sinal_green
                elif self.flag_sinal == 'y':
                    self.lb_sinal['image'] = self.ph_sinal_yellow
                    self.lb_sinal.imagem = self.ph_sinal_yellow
                elif self.flag_sinal == 'r':
                    self.lb_sinal['image'] = self.ph_sinal_red
                    self.lb_sinal.imagem = self.ph_sinal_red
        else:
            self.lb_sinal['image'] = self.ph_sinal_off
            self.lb_sinal.imagem = self.ph_sinal_off
        self.lb_sinal.after(500,lambda: self.atualiza_sinal())
        
    def command_conecta_porta(self):
        if self.bt_conn['text'] == 'Conectar':
            self.bt_conn['text'] = 'Desconectar'
            self.cl_conn.connecta_porta()
            self.flag_conn = True
        elif self.bt_conn['text'] == 'Desconectar':
            self.bt_conn['text'] = 'Conectar'
            self.command_desconecta_porta()
            
    def command_desconecta_porta(self):
        self.cl_conn.desconecta_porta()
        self.flag_conn = False    


if __name__ == "__main__":
    janela= Tk()
    janela.geometry('%dx%d+%d+%d' % (400,400,50,50))
    janela.configure(bg='white')
    janela.title('app distancia')
    janela.resizable(False, False)
    app = Application(janela)
    janela.mainloop()
    app.command_desconecta_porta()
    