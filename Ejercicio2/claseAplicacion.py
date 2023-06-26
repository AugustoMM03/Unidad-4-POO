from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculo de IVA')
        self.__ventana.geometry("341x341")

        mainframe = ttk.Frame(self.__ventana, padding="5 10 5 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2

        self.precioSinIVA = StringVar()
        self.IVA = StringVar()
        self.precioConIVA = StringVar()
        self.resultadoIVA = StringVar()
        self.resultadoPrecioIVA = StringVar()
        self.tipoIVA = StringVar()

        self.titleLbl = ttk.Label(mainframe,text='Calculo de IVA', background='lightblue')
        self.titleLbl.grid(column=1, row=1, columnspan=3, sticky=(N), pady=10)

        self.precioLbl = ttk.Label(mainframe, text='Precio sin IVA')
        self.precioLbl.grid(column=1, row=2, sticky=(W), pady=10)
        self.ivaLbl = ttk.Label(mainframe, text='IVA')
        self.ivaLbl.grid(column=1, row=5, sticky=(W), pady=10)
        self.precioConIvaLbl = ttk.Label(mainframe, text='Precio Con IVA')
        self.precioConIvaLbl.grid(column=1, row=6, sticky=(W), pady=10)

        self.botonIVA21 = ttk.Radiobutton(mainframe, text='IVA 21%', value='21', variable=self.tipoIVA,
                                          command=self.cambiaTipoIVA)
        self.botonIVA21.grid(column=1, row=3, sticky=(W), pady=10)
        self.botonIVA105 = ttk.Radiobutton(mainframe, text='IVA 10.5%', value='10.5', variable=self.tipoIVA,
                                           command=self.cambiaTipoIVA)
        self.botonIVA105.grid(column=1, row=4, sticky=(W), pady=10)

        self.boton1 = ttk.Button(mainframe, text='Calcular', command=self.calcularIVA)
        self.boton1.grid(column=1, row=7, sticky=(W), pady=10)
        self.boton2 = ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy)
        self.boton2.grid(column=3, row=7, sticky=(W), pady=10)

        self.precioSinIVAE = ttk.Entry(mainframe, textvariable=self.precioSinIVA)
        self.precioSinIVAE.grid(column=2, row=2, sticky=(W), pady=10)

        self.precioIVAE = ttk.Label(mainframe, textvariable=self.resultadoIVA, width=15)
        self.precioIVAE.grid(column=2, row=5, sticky=(W), pady=10)

        self.precioConIVAE = ttk.Label(mainframe, textvariable=self.resultadoPrecioIVA, width=15)
        self.precioConIVAE.grid(column=2, row=6, sticky=(W), pady=10)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=7, pady=3)
        self.precioSinIVAE.focus()
        self.__ventana.mainloop()

    def calcularIVA(self):
        try:
            sinIVA = float(self.precioSinIVAE.get())
        except ValueError:
            messagebox.showerror(title='Error de Ingreso', message='Debe ingresar datos numericos.')

        if self.tipoIVA.get() == '21':
            lIVA = sinIVA * 0.21
        elif self.tipoIVA.get() == '10.5':
            lIVA = sinIVA * 0.105
        else:
            lIVA = 0.0

        precioConIva = sinIVA + lIVA
        self.resultadoIVA.set(round(lIVA, 2))
        self.resultadoPrecioIVA.set(round(precioConIva, 2))

    def cambiaTipoIVA(self):
        pass