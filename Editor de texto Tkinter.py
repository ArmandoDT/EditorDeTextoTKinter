import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename


class Editor(tk.Tk):
    def __init__(self):
        super(Editor, self).__init__()
        self.title('Editor de Texto')
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuracion minima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)

        # Atributo de campo de texto
        self.campoTexto = tk.Text(self, wrap=tk.WORD)

        # Atributo de archivo
        self.archivo = None

        # Atributo abierto
        self.archivoAbierto = False

        # Creacion de componentes

        self._crear_componentes()
        self._crear_menu()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        tk.Button(frame_botones, text='Abrir', command=self._abrir_archivo).grid(row=0, column=0, sticky='we', padx=5,
                                                                                 pady=5)
        tk.Button(frame_botones, text='Guardar', command=self._guardar).grid(row=1, column=0, sticky='we', padx=5,
                                                                             pady=5)
        tk.Button(frame_botones, text='Guardar como...', command=self._guardar_como).grid(row=2, column=0, sticky='we',
                                                                                          padx=5, pady=5)

        # Se coloca el frame
        frame_botones.grid(row=0, column=0, sticky='ns')

        self.campoTexto.grid(row=0, column=1, sticky='nswe')

    def _crear_menu(self):
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        # Agregamos las opciones a nuestro menu
        # Agregamos menu archivo
        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)
        # Agregamos las opciones del menu de archivo
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar como...', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='salir', command=self.quit)

    def _abrir_archivo(self):
        # Abrimos el archivo para edicion
        self.archivoAbierto = askopenfile(mode='r+')
        # Eliminamos el texto anterior
        self.campoTexto.delete(1.0, tk.END)

        # Revisamos si hay un archivo
        if not self.archivoAbierto:
            return
        # Abrimos el archivo en modo lectura/escritura como un recurso
        with open(self.archivoAbierto.name, 'r+') as self.archivo:
            # leemos el contenido
            texto = self.archivo.read()
            # insertamos eñ contenido del archivo
            self.campoTexto.insert(1.0, texto)
            # modificamos el título de la aplicacion
            self.title(f'*Editor de Texto - {self.archivo.name}')

    def _guardar(self):
        if self.archivoAbierto:
            # salvamos el archivo
            with open(self.archivoAbierto.name, 'w') as self.archivo:
                # Leemos el conetiddo de la caja de texto
                texto = self.campoTexto.get(1.0, tk.END)
                self.archivo .write(texto)
                self.title(f'Editor texto - {self.archivo.name}')
        else:
            self._guardar_como()

    def _guardar_como(self):
        # Salvamos el archivo actual
        self.archivo = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if not self.archivo:
            return

        with open(self.archivo, 'w') as self.archivo:
            # leemos el contenido de la caja de texto
            texto = self.campoTexto.get(1.0, tk.END)
            # Escribimos el contenido al nuevo archivo
            self.archivo.write(texto)
            self.title(f'Editor texto - {self.archivo.name}')
            # Indicamos que hemos abierto un archivo
            self.archivoAbierto = self.archivo

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()
