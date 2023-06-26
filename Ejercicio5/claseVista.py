import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from claseModelo import Pelicula
from claseModelo import RepositorioPeliculas
from claseModelo import ManejadorPeliculas




class ListaPeliculas(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill= tk.Y)
        self.lb.pack(side=tk.LEFT, fill= tk.BOTH, expand=1)
    
    def insertar(self, pelicula, index=tk.END):
        text = "{}".format(pelicula.getTitle())
        self.lb.insert(index,text)

    def bindDobleClick(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class contenidoPeliculas(tk.LabelFrame):
    fields = ('Titulo', 'Resumen', 'Lenguaje Original', 'Fecha de Lanzamiento', 'Generos')
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Pelicula", padx= 10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.info = list(map(self.mostrarInfo, enumerate(self.fields)))
        self.frame.pack()

    def mostrarInfo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        labelcontent = tk.Label(self.frame)
        label.grid(row=position, column=0, pady=5)
        labelcontent.grid(row=position,column=1,pady=5)
        return labelcontent

    def actualizarDatos(self, pelicula):
        self.info[0]['text'] = ' {}'.format(pelicula.getTitle())
        self.info[1].destroy()  # Eliminar el widget anterior
        self.info[1] = tk.Text(self.frame, height=5, wrap='word')
        self.info[1].insert(tk.END, pelicula.getOverView())
        self.info[1].config(state='disabled')
        self.info[1].grid(row=1, column=1, pady=5)
        #self.info[1]['text'] = 'Resumen: {}'.format(pelicula.getOverView())
        self.info[2]['text'] = '{}'.format(pelicula.getLanguage())
        self.info[3]['text'] = '{}'.format(pelicula.getDate())
        self.info[4]['text'] = '{}'.format(pelicula.getGenres())


class peliculasView(object):
    __ventana = None
    __repositorio = RepositorioPeliculas()
    __manejador = __repositorio.crearPeliculas(__repositorio.obtenerPeliculas())

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Cinéfilos Argentinos APP')
        self.list = ListaPeliculas(self.__ventana,height=15)
        self.list.pack(side=tk.LEFT, padx=10,pady=10)
        self.form = contenidoPeliculas(self.__ventana)
        self.form.pack(padx=10, pady=10)

        for pelicula in self.__manejador.getListaPeliculas():
            self.list.insertar(pelicula)
        
        self.list.bindDobleClick(self.mostrarDatosPelicula)

        self.__ventana.mainloop()

    def mostrarDatosPelicula(self, index):
        peliculas = self.__manejador.getListaPeliculas()
        pelicula = peliculas[index]
        self.form.actualizarDatos(pelicula)

app = peliculasView()



