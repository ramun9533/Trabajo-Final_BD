import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

fecha_actual = datetime.now()
# Formatear la fecha en el formato de SQLite
fecha_sqlite = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')


class PuntoDeVentaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Punto de Venta")

        # Crear pestañas
        self.tabControl = ttk.Notebook(root)
        self.tab_venta = ttk.Frame(self.tabControl)
        self.tab_inventario = ttk.Frame(self.tabControl)

        # Configurar pestañas
        self.tabControl.add(self.tab_venta, text='Venta')
        self.tabControl.add(self.tab_inventario, text='Inventario')

        # Inicializar la interfaz gráfica de la pestaña de venta
        self.inicializar_interfaz_venta()

        # Inicializar la interfaz gráfica de la pestaña de inventario
        self.inicializar_interfaz_inventario()

        # Mostrar pestañas
        self.tabControl.pack(expand=1, fill="both")

        # Inicializar la base de datos
        self.db_manager = DBManager()

    def inicializar_interfaz_venta(self):
       # TODO: Agregar widgets y lógica para la pestaña de venta
        pass

    def inicializar_interfaz_inventario(self):
        # Etiqueta y cuadro de texto para ingresar el nombre del producto
        lbl_nombre_producto = tk.Label(self.tab_inventario, text="Nombre del Producto:")
        lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre_producto = tk.Entry(self.tab_inventario)
        entry_nombre_producto.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar descripcion del producto
        lbl_decripcion_producto = tk.Label(self.tab_inventario, text="Descripcion del Producto:")
        lbl_decripcion_producto.grid(row=1, column=0, padx=10, pady=10)
        entry_decripcion_producto = tk.Entry(self.tab_inventario)
        entry_decripcion_producto.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el precio del producto
        lbl_precio_producto = tk.Label(self.tab_inventario, text="Precio del Producto:")
        lbl_precio_producto.grid(row=2, column=0, padx=10, pady=10)
        entry_precio_producto = tk.Entry(self.tab_inventario)
        entry_precio_producto.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar la cantidad en stock
        lbl_stock = tk.Label(self.tab_inventario, text="Cantidad en Stock:")
        lbl_stock.grid(row=3, column=0, padx=10, pady=10)
        entry_stock = tk.Entry(self.tab_inventario)
        entry_stock.grid(row=3, column=1, padx=10, pady=10)
        
        # Etiqueta y cuadro de texto para ingresar el statuaus del producto
        lbl_status_producto = tk.Label(self.tab_inventario, text="Status del Producto:")
        lbl_status_producto.grid(row=4, column=0, padx=10, pady=10)
        entry_status_producto = tk.Entry(self.tab_inventario)
        entry_status_producto.grid(row=4, column=1, padx=10, pady=10)

        # Botón para agregar producto al inventario
        btn_agregar_inventario = tk.Button(self.tab_inventario, text="Agregar al Inventario", command=self.agregar_a_inventario)
        btn_agregar_inventario.grid(row=5, column=0, columnspan=5, pady=10)

    def agregar_a_inventario(self):
        # Obtener la información ingresada por el usuario
        nombre_producto = self.entry_nombre_producto.get()
        descripcion_producto = self.entry_descripcion.get()
        precio_producto = self.entry_precio.get()
        cantidad_stock = self.entry_stock.get()
        status_producto = self.entry_status_producto.get()
#        fecha_creacion = self.entry_fecha_creacion.get()
        # Validar que se hayan ingresado valores
        if not nombre_producto or not cantidad_stock:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            # Convertir la cantidad a un entero
            cantidad_stock = int(cantidad_stock)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        # Insertar el nuevo producto en el inventario
        self.db_manager.agregar_producto(nombre_producto, descripcion_producto, precio_producto, cantidad_stock, status_producto)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Producto agregado al inventario con éxito.")

        # Limpiar los campos de entrada después de agregar el producto
        self.entry_nombre_producto = None
        self.entry_descripcion = None
        self.entry_precio = None
        self.entry_stock = None
        self.entry_status_producto = None
#        self.entry_fecha_creacion = None
        # Inicializar la base de datos
        self.db_manager = DBManager()

    # ... (resto del código es igual)

    class DBManager:
    def __init__(self):
        # Conectar a la base de datos
        self.conexion = sqlite3.connect('credenciales_usuarios.db')
        self.cursor = self.conexion.cursor()

        # Crear tablas si no existen
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Producto (
                ID_Producto INTEGER PRIMARY KEY,
                Nombre TEXT,
                Descripcion TEXT,
                Precio REAL,
                Stock INTEGER,
                Status INTEGER,
                CreadoPor INTEGER,
                ModificadoPor INTEGER,
                FechaCreacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conexion.commit()

    def agregar_producto(self, nombre, descripcion, precio, stock, status):
        # Insertar el nuevo producto en la tabla 'Producto'
        creadopor = 1  # Puedes ajustar esto según tus necesidades
        modificado_por = 2  # Puedes ajustar esto según tus necesidades
        #fecha_creacion = fe
        self.cursor.execute("INSERT INTO Producto (Nombre, Descripcion, Precio, Stock, Status, CreadoPor, FechaCreacion, ModificadoPor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nombre, descripcion, precio, stock, status, creadopor, fecha_creacion, modificado_por))
        self.conexion.commit()

    def __del__(self):
        # Cerrar la conexión a la base de datos al destruir el objeto
        self.conexion.close()

# Resto del código...

if __name__ == "__main__":
    root = tk.Tk()
    app = PuntoDeVentaApp(root)
    root.mainloop()