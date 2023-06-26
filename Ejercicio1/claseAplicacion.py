from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.configure(bg = 'beige')
        self.__ventana.title('Índice de Precios al Consumidor (IPC)')
        self.__ventana.geometry("400x250")
        mainframe = ttk.Frame(self.__ventana, padding= "5 10 5 10")
        mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
                
        self.cantVest = StringVar()
        self.precioBaseVest = StringVar()
        self.precioActualVest = StringVar()
        self.cantAlim = StringVar()
        self.precioBaseAlim = StringVar()
        self.precioActualAlim = StringVar()
        self.cantEdu = StringVar()
        self.precioBaseEdu = StringVar()
        self.precioActualEdu = StringVar()
        self.resultado = StringVar()
        
        self.itemLbl = ttk.Label(mainframe, text = 'Item').grid(column=1,row=1,sticky=(W))
        self.cantidadLbl = ttk.Label(mainframe, text = 'Cantidad').grid(column=2,row=1,sticky=(W))
        self.precioBaseLbl = ttk.Label(mainframe, text = 'Precio Año Base').grid(column=3,row=1,sticky=(W))
        self.precioActualLbl = ttk.Label(mainframe, text = 'Precio Año Actual').grid(column=4,row=1,sticky=(W))
        self.vestimentaLbl = ttk.Label(mainframe, text = 'Vestimenta').grid(column=1,row=2,sticky=(W))
        self.alimentosLbl = ttk.Label(mainframe, text = 'Alimentos').grid(column=1,row=3,sticky=(W))
        self.educacionLbl = ttk.Label(mainframe, text = 'Educacion').grid(column=1,row=4,sticky=(W))
        self.IPCLbl = ttk.Label(mainframe, text = 'IPC % ').grid(column=1,row=7,sticky=(W))
        self.resultadoIPC = ttk.Label (mainframe, text= '%').grid(column=2,row=7,sticky=(W))

        
        
        
        self.ccantV =  ttk.Entry(mainframe,width=12, textvariable=self.cantVest)
        self.ccantV.grid(column=2,row=2,sticky=(W))
        
        self.cprecioBaseV =  ttk.Entry(mainframe,width=12, textvariable=self.precioBaseVest)
        self.cprecioBaseV.grid(column=3,row=2,sticky=(W))
        
        self.cprecioActualV =  ttk.Entry(mainframe,width=12, textvariable=self.precioActualVest)
        self.cprecioActualV.grid(column=4,row=2,sticky=(W))  
        
        self.ccantA =  ttk.Entry(mainframe,width=12, textvariable=self.cantAlim)
        self.ccantA.grid(column=2,row=3,sticky=(W))  
        
        self.cprecioBaseA =  ttk.Entry(mainframe,width=12, textvariable=self.precioBaseAlim)
        self.cprecioBaseA.grid(column=3,row=3,sticky=(W))  
        
        self.cprecioActualA =  ttk.Entry(mainframe,width=12, textvariable=self.precioActualAlim)
        self.cprecioActualA.grid(column=4,row=3,sticky=(W)) 
        
        self.ccantE =  ttk.Entry(mainframe,width=12, textvariable=self.cantEdu)
        self.ccantE.grid(column=2,row=4,sticky=(W))  
        
        self.cprecioBaseE =  ttk.Entry(mainframe,width=12, textvariable=self.precioBaseEdu)
        self.cprecioBaseE.grid(column=3,row=4,sticky=(W))  
        
        self.cprecioActualE =  ttk.Entry(mainframe,width=12, textvariable=self.precioActualEdu)
        self.cprecioActualE.grid(column=4,row=4,sticky=(W))  

        self.boton1 = ttk.Button(mainframe, text = 'Calcular IPC', command=self.calcularIPC).grid(column=2,row=6, sticky=(W)) 
        self.boton2 = ttk.Button(mainframe, text = 'Salir', command=self.__ventana.destroy).grid(column=4,row=6, sticky=(W))
        ttk.Label(mainframe,textvariable=str(self.resultado)).grid(column=1,row=7,sticky=(E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=8, pady=8)
        self.ccantV.focus()
        self.__ventana.mainloop()

    def calcularIPC(self):
        try:
            cantv=int(self.ccantV.get())
            basev=float(self.cprecioBaseV.get())
            actualv=float(self.cprecioActualV.get())


            canta=int(self.ccantA.get())
            basea=float(self.cprecioBaseA.get())
            actuala=float(self.cprecioActualA.get())


            cante=int(self.ccantE.get())
            basee=float(self.cprecioBaseE.get())
            actuale=float(self.cprecioActualE.get())      

        except ValueError:
            messagebox.showerror(title='Error de ingreso.', message='Debe ingresar datos numericos.')

        costoBase = (canta * basea) + (cantv * basev) + (cante * basee)
        costoActual = (canta * actuala) + (cantv * actualv) + (cante * actuale)

        ipc = (costoActual/costoBase)
        ipc = ipc - int(ipc)
        ipc = ipc*100
        self.resultado.set(round(ipc,2))
