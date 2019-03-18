from tkinter import *
from tkinter import ttk 
from functools import partial

class Programa(object):
    def __init__(self, janela):
        
            self.tab_control = ttk.Notebook(janela)
            self.aba1 = ttk.Frame(self.tab_control) 
            self.aba2 = ttk.Frame(self.tab_control)
            self.aba3 = ttk.Frame(self.tab_control)
            self.tab_control.add(self.aba1, text='Adesivos') 
            self.tab_control.add(self.aba2, text='Banner')
            self.tab_control.add(self.aba3, text='Informações')
            
            self.tab_control.grid(row=0)
            
            #
            #
            #
            ##################  Informações
            #
            #
            #
            
            self.inf1 = Label (self.aba3, text="Valor do Metro: ")
            self.inf1.grid(row=1, column=0)
            
            self.inf8 = Entry(self.aba3, width="5")
            self.inf8.grid(row=1, column=1)
            self.inf8.insert(0, 50)
            
            self.inf2 = Label (self.aba3, text="Tamanho da Tabela: ")
            self.inf2.grid(row=2, column=0)
            
            self.inf3 = Entry(self.aba3, width="5")
            self.inf3.grid(row=2, column=1)
            self.inf3.insert(0, 20)
            
            self.inf4 = Label(self.aba3, text="x")
            self.inf4.grid(row=2, column=2)
            
            self.inf5 = Entry(self.aba3, width="5")
            self.inf5.grid(row=2, column=3)
            self.inf5.insert(0, 30)
            
            self.inf6 = Label (self.aba3, text="Acabamento: ")
            self.inf6.grid(row=3, column=0)
            
            self.inf7 = Entry(self.aba3, width="5")
            self.inf7.grid(row=3, column=1)
            self.inf7.insert(0, 5)
        
            
            #
            #
            #
            ##################  Adesivos
            #
            #
            #
            
            self.lb1 = Label (self.aba1, text="Q/Adesivos: ")
            self.lb1.grid(row=1, column=1)
            
            self.ed1 = Entry(self.aba1, width="5")
            self.ed1.grid(row=1, column=2)
            
            self.lb2 = Label (self.aba1, text="Tamanho: ")
            self.lb2.grid(row=2, column=1)
            
            self.ed2 = Entry(self.aba1, width="5")
            self.ed2.grid(row=2, column=2)
            ed3 = Entry(self.aba1, width="5")
            ed3.grid(row=2, column=4)
            
            self.lb21 = Label(self.aba1, text="x")
            self.lb21.grid(row=2, column=3)
        
            self.lb4 = Label(self.aba1, text="Resultado")
            self.lb4.grid(row=4, column=0, columnspan = 5)
            
            self.bt = Button(self.aba1, text="Calcular", width="15")
            self.bt["command"] = partial(self.calM, self.ed1, self.ed2, ed3)
            self.bt.grid(row=3, column=1, columnspan = 10)
            
            #self.bt1 = Button(self.aba1, width="5", text="Add")
            #self.bt1["command"] = print ("atette")
            #self.bt1.grid(row=3, column=1)
            
            #
            #
            #
            ##################  Banner
            #
            #
            #
            
            self.ban1 = Label (self.aba2, text="Valor do Metro: ")
            self.ban1.grid(row=1, column=0)
            
            self.ban2 = Label(self.aba2, text= self.inf8.get())
            self.ban2.grid(row=1, column=1)
            
            self.ban3 = Label (self.aba2, text="Tamanho: ")
            self.ban3.grid(row=2, column=0)
            
            self.ban4 = Entry(self.aba2, width="5")
            self.ban4.grid(row=2, column=1)
            
            self.ban6 = Label(self.aba2, text="x")
            self.ban6.grid(row=2, column=2)
            
            self.ban5 = Entry(self.aba2, width="5")
            self.ban5.grid(row=2, column=3)
            
            self.ban8 = Label (self.aba2, text="Acabamento: ")
            self.ban8.grid(row=3, column=0)

            
            self.ban9 = Label (self.aba2, text= self.inf7.get())
            self.ban9.grid(row=3, column=1)
            
            self.ban7 = Button(self.aba2, text="Calcular")
            self.ban7["command"] = partial(self.calMB, self.inf8, self.ban4, self.ban5, self.inf7)
            self.ban7.grid(row=4, column=0, columnspan = 4)
            
            self.ban10 = Label(self.aba2, text="Resultado")
            self.ban10.grid(row=5, column=0, columnspan = 4)
            
            self.inf9 = Button(self.aba3,width="15" ,text="Ok")
            self.inf9["command"] = self.prit
            self.inf9.grid(row=4, column=0, columnspan = 4)
            
    def calMB (self, inf8, ban4, ban5, inf7):
        try:
            num1 = int(inf8.get())
            num2 = (float(ban4.get()))/100
            num3 = (float(ban5.get()))/100
            num4 = int(inf7.get())
            self.ban10["text"] = "R$ "+("%.2f" % ((num2*num3*num1)+num4))
        except:
            self.ban10["text"]= "Comando Inválido"
        
        
    def calM (self, ed1, ed2, ed3):
        
        try:
            x = self.vall(self.inf3, self.inf5)
            num1 = int(ed1.get())
            num2 = (float(ed2.get()))/100
            num3 = (float(ed3.get()))/100
            t = (num1/(int(x/(num2*num3)+0.00000000001)))
            if((num1%(int(x/(num2*num3))))!=0):
                t += 1
            self.lb4["text"]= (str(int(t)))+" T.Adesivos\n"+(str(int(x/(num2*num3))*int(t)))+" Adesivos\n"+str(int(x/(num2*num3)+0.00000000001))+" Adesivos/T"
        except:
            self.lb4["text"]= "Comando Inválido"
    def vall (self, inf3, inf5):
        try:
            num1 = (float(inf3.get())/100)
            num2 = (float(inf5.get())/100)
            return (num1*num2)
        except:
            self.lb4["text"]= "Comando Inválido"
    def prit(self):
        self.ban2["text"] = self.inf8.get()
        self.ban9["text"] = self.inf7.get()
        
janela = Tk()
Programa(janela)
janela.title("ArtCores")
janela.geometry("230x180")
janela.mainloop()
