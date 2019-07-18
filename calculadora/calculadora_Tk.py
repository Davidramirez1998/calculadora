from Tkinter import *
from calculadora import *
from threading import *

class InterfazCalculadora(Thread):

    def __init__(self):
        self.root = Tk()
        self.calculadora = Calculadora()
        self.frame = Frame(self.root)
        self.frame.pack()
       
        foreground = "red"
        foreground2 = "blue"
        background = "blue"
        activeforeground = "white"
        disabledforeground = "white"
   
       
        

        #Etiqueta display de calculadora
        self.inicio = StringVar()
        self.inicio.set ("0" )
        self.display = Label(self.frame, textvariable = self.inicio, font=("arial", 30))
        self.display.grid(row=0, column=0, columnspan=4)

        self.boton_CE = Button(self.frame, text=" CE ", font=("arial", 20), height=1 , width=3, foreground =foreground)    
        self.boton_CE.bind("<Button-1>")
        self.boton_CE.grid(row=5, column=0)
         


        self.boton_div = Button(self.frame, text=" / ", font=("arial", 20), height=1 , width=3, foreground =foreground2)
        self.boton_div.bind("<Button-1>")
        self.boton_div.grid(row=5, column=3)


        self.boton_7 = Button(self.frame, text=" 7 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("7"))
        self.boton_7.bind("<Button-1>")
        self.boton_7.grid(row=2, column=0)

        self.boton_8 = Button(self.frame, text=" 8 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("8"))
        self.boton_8.bind("<Button-1>")
        self.boton_8.grid(row=2, column=1)

        self.boton_9 = Button(self.frame, text=" 9 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("9"))
        self.boton_9.bind("<Button-1>")
        self.boton_9.grid(row=2, column=2)

        self.boton_por = Button(self.frame, text=" x ", font=("arial", 20),  height=1 , width=3, foreground =foreground2)
        self.boton_por.bind("<Button-1>")
        self.boton_por.grid(row=2, column=3)

        self.boton_4 = Button(self.frame, text=" 4 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("4"))
        self.boton_4.bind("<Button-1>")
        self.boton_4.grid(row=3, column=0)

        self.boton_5 = Button(self.frame, text=" 5 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("5"))
        self.boton_5.bind("<Button-1>")
        self.boton_5.grid(row=3, column=1)

        self.boton_6 = Button(self.frame, text=" 6 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("6"))
        self.boton_6.bind("<Button-1>")
        self.boton_6.grid(row=3, column=2)

        self.boton_men = Button(self.frame, text=" - ", font=("arial", 20),  height=1 , width=3, foreground =foreground2)
        self.boton_men.bind("<Button-1>")
        self.boton_men.grid(row=3, column=3)

        self.boton_1 = Button(self.frame, text=" 1 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("1"))
        self.boton_1.bind("<Button-1>")
        self.boton_1.grid(row=4, column=0)

        self.boton_2 = Button(self.frame, text=" 2 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("2"))
        self.boton_2.bind("<Button-1>")
        self.boton_2.grid(row=4, column=1)

        self.boton_3 = Button(self.frame, text=" 3 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("3"))
        self.boton_3.bind("<Button-1>")
        self.boton_3.grid(row=4, column=2)

        self.boton_mas = Button(self.frame, text=" + ", font=("arial", 20),  height=1 , width=3, foreground =foreground2)
        self.boton_mas.bind("<Button-1>")
        self.boton_mas.grid(row=4, column=3)

        self.boton_cero = Button(self.frame, text=" 0 ", font=("arial", 20),  height=1 , width=3, command = lambda: self.manejar_numeros ("0"))
        self.boton_cero.bind("<Button-1>")
        self.boton_cero.grid(row=5, column=1, )

        
        self.boton_igual = Button(self.frame, text=" = ", font=("arial", 20),  height=1 , width=3, foreground =foreground)
        self.boton_igual.bind("<Button-1>", )
        self.boton_igual.grid(row=5, column=2)

       

        Thread.__init__(self)
        self.start()
        self.root.geometry('250x350')
        self.root.mainloop()





    def manejar_numeros(self, valor):
        if self.inicio.get () == "0" :
            self.inicio.set (valor)

        else:

            self.inicio.set (self.inicio.get() + valor)


 
        

        
        

    
    








app = InterfazCalculadora()
