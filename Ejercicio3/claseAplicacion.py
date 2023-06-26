from tkinter import *
from tkinter import ttk, messagebox
import requests

class Aplicacion(object):

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Conversor de Moneda')
        self.ventana.geometry("293x149")

        mainframe = ttk.Frame(self.ventana, padding="5 10 5 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        self.cantDolares = StringVar()
        self.resultado = StringVar()
        self.cantDolares.trace_add('write', self.conversionPesos)


        self.dolaresLbl = ttk.Label(mainframe, text= 'dólares').grid(column=3,row=1, pady = 10,sticky=(W))
        self.dolaresEntry = ttk.Entry(mainframe,width=8, textvariable= self.cantDolares).grid(column=2,row=1, pady = 10,sticky=(W))


        self.pesosLbl1 = ttk.Label(mainframe, text= 'es equivalente a ').grid(column=1,row=2, pady = 10,sticky=(W))
        self.resultadoLbl = ttk.Label(mainframe, textvariable=self.resultado).grid(column=2,row=2, pady = 10,sticky=(W))
        self.pesosLbl2 = ttk.Label(mainframe, text= ' pesos').grid(column=3,row=2, pady = 10,sticky=(W))

        self.botonSalida = ttk.Button(mainframe, text='Salir', command= self.ventana.destroy).grid(column=3,row=3, pady = 10)

        self.ventana.mainloop()


    def obtenerCotizacion(self):
        url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        try:
            response = requests.get(url)
            data = response.json()
            cotizacion = float(data[0]['casa']['venta'].replace(',', '.'))
            return cotizacion
        except requests.exceptions.RequestException as e:
            messagebox.showerror(title='Error', message="Error al obtener la cotizacion del dolar")
            return None


    def conversionPesos(self,*args):
        try:
            cantdolares = float(self.cantDolares.get())
        except ValueError:
            messagebox.showerror(title='Error de ingreso.', message='Debe ingresar datos numericos.')
        
        cotizacion = self.obtenerCotizacion()
        if cotizacion:
            cantpesos = cantdolares * cotizacion
            self.resultado.set(round(cantpesos,2))