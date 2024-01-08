import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from datetime import datetime

fecha_actual = datetime.now()
# Formatear la fecha en el formato de SQLite
fecha_sqlite = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

#fechahoy = fecha_sqlite
class InterfazInsercion(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inserción en Tabla")

        # Crear widgets
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.entry_nombre = tk.Entry(self)

        self.label_descripcion = tk.Label(self, text="Descripción:")
        self.entry_descripcion = tk.Entry(self)

        self.btn_insertar = tk.Button(self, text="Insertar", command=self.insertar_en_tabla)

        # Posicionar widgets
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.label_descripcion.grid(row=1, column=0, padx=10, pady=10)
        self.entry_descripcion.grid(row=1, column=1, padx=10, pady=10)
        self.btn_insertar.grid(row=2, column=0, columnspan=2, pady=10)

        # Conectar a la base de datos
        self.conexion = sqlite3.connect('Test_DB.db')
        self.cursor = self.conexion.cursor()

        # Crear la tabla si no existe
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ejemplo1 (
                ID INTEGER PRIMARY KEY,
                Nombre TEXT,
                Descripcion TEXT,
                fecha_hoy DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conexion.commit()

    def insertar_en_tabla(self):
        # Obtener valores de las entradas
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        #fechahoy =  self.entry_fechahoy.get()
        # Insertar en la tabla
        self.cursor.execute("INSERT INTO Ejemplo1 (Nombre, Descripcion) VALUES (?, ?)", (nombre, descripcion))
        self.conexion.commit()

        # Limpiar entradas después de la inserción
        self.entry_nombre.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

        # Mensaje de éxito
        tk.messagebox.showinfo("Éxito", "Datos insertados correctamente.")

if __name__ == "__main__":
    app = InterfazInsercion()
    app.mainloop()
