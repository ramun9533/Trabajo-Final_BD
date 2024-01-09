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
        self.root.title("Menu Administrador")

        # Crear pestañas
        self.tabControl = ttk.Notebook(root)
        self.tab_detalle_venta = ttk.Frame(self.tabControl)
        self.tab_producto = ttk.Frame(self.tabControl)
        self.tab_proveedor = ttk.Frame(self.tabControl)
        self.tab_cliente = ttk.Frame(self.tabControl)
        self.tab_reparacion = ttk.Frame(self.tabControl)
        self.tab_detalle_reparacion = ttk.Frame(self.tabControl)
        self.tab_empleados = ttk.Frame(self.tabControl)
        self.tab_usuarios = ttk.Frame(self.tabControl)
        

        # Configurar pestañas
        
        self.tabControl.add(self.tab_producto, text='Producto')
        self.tabControl.add(self.tab_detalle_venta, text='Detalle de Venta')
        self.tabControl.add(self.tab_proveedor, text='Proveedor')
        self.tabControl.add(self.tab_cliente, text='Cliente')
        self.tabControl.add(self.tab_detalle_reparacion, text='Detalle de reparacion')
        self.tabControl.add(self.tab_empleados, text='Empleados')
        self.tabControl.add(self.tab_usuarios, text='Usuarios')
        self.tabControl.add(self.tab_reparacion, text='Reparacion')
        
        # Inicializar la interfaz gráfica de la pestaña de venta
        
        self.inicializar_interfaz_producto()
        
        self.inicializar_interfaz_detalle_venta()
        
        self.inicializar_interfaz_proveedor()
        
        self.inicializar_interfaz_cliente()
#Pendiente porque no funcionan esas pestañas        
        self.inicializar_interfaz_reparacion()
        
        self.inicializar_interfaz_detalle_reparacion()
        
        self.inicializar_interfaz_empleados()
        
        self.inicializar_interfaz_usuarios()
        # Inicializar la interfaz gráfica de la pestaña de inventario
        

        # Mostrar pestañas
        self.tabControl.pack(expand=1, fill="both")

        # Inicializar la base de datos
        self.db_manager = DBManager()

    def inicializar_interfaz_producto(self):
        # Etiqueta y cuadro de texto para ingresar el nombre del producto
        lbl_nombre_producto = tk.Label(self.tab_producto, text="Nombre del Producto:")
        lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_producto = tk.Entry(self.tab_producto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar descripcion del producto
        lbl_descripcion_producto = tk.Label(self.tab_producto, text="Descripción del Producto:")
        lbl_descripcion_producto.grid(row=1, column=0, padx=10, pady=10)
        self.entry_descripcion = tk.Entry(self.tab_producto)
        self.entry_descripcion.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el precio del producto
        lbl_precio_producto = tk.Label(self.tab_producto, text="Precio del Producto:")
        lbl_precio_producto.grid(row=2, column=0, padx=10, pady=10)
        self.entry_precio_producto = tk.Entry(self.tab_producto)
        self.entry_precio_producto.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar la cantidad en stock
        lbl_stock = tk.Label(self.tab_producto, text="Cantidad en Stock:")
        lbl_stock.grid(row=3, column=0, padx=10, pady=10)
        self.entry_stock = tk.Entry(self.tab_producto)
        self.entry_stock.grid(row=3, column=1, padx=10, pady=10)
        
        # Etiqueta y cuadro de texto para ingresar el statuaus del producto
        lbl_status_producto = tk.Label(self.tab_producto, text="Status del Producto:")
        lbl_status_producto.grid(row=4, column=0, padx=10, pady=10)
        self.entry_status_producto = tk.Entry(self.tab_producto)
        self.entry_status_producto.grid(row=4, column=1, padx=10, pady=10)

        # Botón para agregar producto al inventario
        btn_agregar_producto = tk.Button(self.tab_producto, text="Agregar al Inventario", command=self.agregar_producto)
        btn_agregar_producto.grid(row=5, column=0, columnspan=5, pady=10)
    
    def inicializar_interfaz_detalle_venta(self):
        lbl_cantidad = tk.Label(self.tab_detalle_venta, text="Cantidad:")
        lbl_cantidad.grid(row=0, column=0, padx=10, pady=10)
        self.entry_cantidad = tk.Entry(self.tab_detalle_venta)
        self.entry_cantidad.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar descripcion del producto
        lbl_precio_del_producto = tk.Label(self.tab_detalle_venta, text="Precio del Producto:")
        lbl_precio_del_producto.grid(row=1, column=0, padx=10, pady=10)
        self.entry_precio_del_producto = tk.Entry(self.tab_detalle_venta)
        self.entry_precio_del_producto.grid(row=1, column=1, padx=10, pady=10)
        
        # Falta crear la funcion para el Botón (revisar la funcion agregar_producto)
        btn_detalle_venta = tk.Button(self.tab_detalle_venta, text="Capturar detalle de venta", command=self.detalle_venta)
        btn_detalle_venta.grid(row=5, column=0, columnspan=5, pady=10)
    
    def inicializar_interfaz_detalle_reparacion(self):
        # Etiqueta y cuadro de texto para ingresar cantidad de la reparacion
        lbl_detalle_cantidad = tk.Label(self.tab_detalle_reparacion, text="Cantidad:")
        lbl_detalle_cantidad.grid(row=0, column=0, padx=10, pady=10)
        self.entry_detalle_cantidad = tk.Entry(self.tab_detalle_reparacion)
        self.entry_detalle_cantidad.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar costo de la reparacion
        lbl_detalle_costo = tk.Label(self.tab_detalle_reparacion, text="Costo:")
        lbl_detalle_costo.grid(row=1, column=0, padx=10, pady=10)
        self.entry_detalle_costo = tk.Entry(self.tab_detalle_reparacion)
        self.entry_detalle_costo.grid(row=1, column=1, padx=10, pady=10)

        # Botón para agregar a detalles reparacion
        btn_agregar_detalle_reparacion = tk.Button(self.tab_detalle_reparacion, text="Capturar detalle de reparacion", command=self.agregar_reparacion)
        btn_agregar_detalle_reparacion.grid(row=2, column=0, columnspan=5, pady=10)

    def inicializar_interfaz_cliente(self):
        # Etiqueta y cuadro de texto para ingresar el nombre del cliente
        lbl_nombre_cliente = tk.Label(self.tab_cliente, text="Nombre:")
        lbl_nombre_cliente.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_cliente = tk.Entry(self.tab_cliente)
        self.entry_nombre_cliente.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar la direccion del cliente
        lbl_direccion = tk.Label(self.tab_cliente, text="Direccion:")
        lbl_direccion.grid(row=1, column=0, padx=10, pady=10)
        self.entry_direccion = tk.Entry(self.tab_cliente)
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el telefono del cliente
        lbl_telefono_cliente = tk.Label(self.tab_cliente, text="Telefono:")
        lbl_telefono_cliente.grid(row=2, column=0, padx=10, pady=10)
        self.entry_telefono_cliente = tk.Entry(self.tab_cliente)
        self.entry_telefono_cliente.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el correo del cliente
        lbl_correo_cliente = tk.Label(self.tab_cliente, text="Correo:")
        lbl_correo_cliente.grid(row=3, column=0, padx=10, pady=10)
        self.entry_correo_cliente = tk.Entry(self.tab_cliente)
        self.entry_correo_cliente.grid(row=3, column=1, padx=10, pady=10)  
        # Botón para agregar cliente 
        #no jala la seccion btn
        btn_agregar_cliente = tk.Button(self.tab_cliente, text="Agregar cliente", command=self.detalle_venta)
        btn_agregar_cliente.grid(row=4, column=0, columnspan=5, pady=10)      
    
    def inicializar_interfaz_proveedor(self):
        # Etiqueta y cuadro de texto para ingresar el nombre del proveedor
        lbl_proveedor = tk.Label(self.tab_proveedor, text="Nombre:")
        lbl_proveedor.grid(row=0, column=0, padx=10, pady=10)
        self.entry_proveedor = tk.Entry(self.tab_proveedor)
        self.entry_proveedor.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el status del proveedor
        lbl_status = tk.Label(self.tab_proveedor, text="Status:")
        lbl_status.grid(row=2, column=0, padx=10, pady=10)
        self.entry_status = tk.Entry(self.tab_proveedor)
        self.entry_status.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el telefono del proveedor
        lbl_telefono = tk.Label(self.tab_proveedor, text="Telefono:")
        lbl_telefono.grid(row=3, column=0, padx=10, pady=10)
        self.entry_telefono = tk.Entry(self.tab_proveedor)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el correo del proveedor
        lbl_correo = tk.Label(self.tab_proveedor, text="Correo:")
        lbl_correo.grid(row=4, column=0, padx=10, pady=10)
        self.entry_correo = tk.Entry(self.tab_proveedor)
        self.entry_correo.grid(row=4, column=1, padx=10, pady=10)
        # Botón para agregar proveedor
        #no jala la seccion btn
        btn_agregar_proveedor = tk.Button(self.tab_proveedor, text="Agregar proveedor", command=self.detalle_venta)
        btn_agregar_proveedor.grid(row=5, column=0, columnspan=5, pady=10)

    def inicializar_interfaz_reparacion(self):
        # Etiqueta y cuadro de texto para ingresar el status de la reparacion
        #no hay forma se seleccionar que reparacion se hace o bien eso es detalles reparacion
        lbl_status_reparacion = tk.Label(self.tab_reparacion, text="Status:")
        lbl_status_reparacion.grid(row=0, column=0, padx=10, pady=10)
        self.entry_status_reparacion = tk.Entry(self.tab_reparacion)
        self.entry_status_reparacion.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el costo total de la reparacion
        lbl_CostoTotal_reparacion = tk.Label(self.tab_reparacion, text="Costo Total:")
        lbl_CostoTotal_reparacion.grid(row=1, column=0, padx=10, pady=10)
        self.entry_CostoTotal_reparacion = tk.Entry(self.tab_reparacion)
        self.entry_CostoTotal_reparacion.grid(row=1, column=1, padx=10, pady=10)
        # Botón para agregar producto a la reparacion 
        #no jala la seccion btn
        btn_agregar_reparacion = tk.Button(self.tab_reparacion, text="Agregar reparacion", command=self.detalle_venta)
        btn_agregar_reparacion.grid(row=2, column=0, columnspan=5, pady=10)

    def inicializar_interfaz_empleados(self):
        # Etiqueta y cuadro de texto para ingresar el nombre al usuario
        lbl_NombreUsuario = tk.Label(self.tab_empleados, text="Nombre usuario:")
        lbl_NombreUsuario.grid(row=0, column=0, padx=10, pady=10)
        self.entry_NombreUsuario = tk.Entry(self.tab_empleados)
        self.entry_NombreUsuario.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el contraseña al usuario
        lbl_Contraseña = tk.Label(self.tab_empleados, text="Contraseña:")
        lbl_Contraseña.grid(row=1, column=0, padx=10, pady=10)
        self.entry_Contraseña = tk.Entry(self.tab_empleados)
        self.entry_Contraseña.grid(row=1, column=1, padx=10, pady=10) 

        # Etiqueta y cuadro de texto para ingresar el rol al usuario
        lbl_Rol = tk.Label(self.tab_empleados, text="Rol del usuario:")
        lbl_Rol.grid(row=2, column=0, padx=10, pady=10)
        self.entry_Rol = tk.Entry(self.tab_empleados)
        self.entry_Rol.grid(row=2, column=1, padx=10, pady=10)   

        # Etiqueta y cuadro de texto para ingresar el status del usuario
        lbl_Status_Usuario = tk.Label(self.tab_empleados, text="Status:")
        lbl_Status_Usuario.grid(row=3, column=0, padx=10, pady=10)
        self.entry_Status_Usuario = tk.Entry(self.tab_empleados)
        self.entry_Status_Usuario.grid(row=3, column=1, padx=10, pady=10)
        # Botón para agregar usuario 
        #no jala la seccion btn
        btn_agregar_Usuario = tk.Button(self.tab_empleados, text="Agregar usuario", command=self.detalle_venta)
        btn_agregar_Usuario.grid(row=4, column=0, columnspan=5, pady=10)
    def inicializar_interfaz_usuarios(self):

        lbl_NombreUsuario = tk.Label(self.tab_usuarios, text="Nombre usuario:")
        lbl_NombreUsuario.grid(row=0, column=0, padx=10, pady=10)
        self.entry_NombreUsuario = tk.Entry(self.tab_usuarios)
        self.entry_NombreUsuario.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y cuadro de texto para ingresar el contraseña al usuario
        lbl_Contraseña = tk.Label(self.tab_usuarios, text="Contraseña:")
        lbl_Contraseña.grid(row=1, column=0, padx=10, pady=10)
        self.entry_Contraseña = tk.Entry(self.tab_usuarios)
        self.entry_Contraseña.grid(row=1, column=1, padx=10, pady=10) 

        btn_agregar_Usuario = tk.Button(self.tab_usuarios, text="Agregar usuario", command=self.detalle_venta)
        btn_agregar_Usuario.grid(row=4, column=0, columnspan=5, pady=10)

       
 
    
    def detalle_venta(self):
        cantidad = self.entry_cantidad.get()#
        precio_del_producto = self.entry_precio_del_producto.get()#
        if not cantidad or not cantidad_stock or not precio_del_producto:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            # Convertir la cantidad a un entero
            cantidad_stock = int(cantidad_stock)
            precio_del_producto = float(precio_del_producto)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        # Insertar el nuevo producto en el inventario
        self.db_manager.agregar_producto(cantidad, precio_del_producto)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Producto agregado al inventario con éxito.")

        # Limpiar los campos de entrada después de agregar el producto
        self.entry_cantidad = None
        self.entry_precio_del_producto = None
    
    def agregar_reparacion(self):
        reparacion_cantidad = self.entry_detalle_cantidad.get()#
        detalle_costo = self.entry_detalle_costo.get()#

        if not reparacion_cantidad or not detalle_costo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            # Convertir la cantidad a un entero
            reparacion_cantidad = int(reparacion_cantidad)
            detalle_costo = float(detalle_costo)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        # Insertar el nuevo producto en el inventario
        self.db_manager.agregar_producto(nombre_producto, descripcion_producto, precio_producto, cantidad_stock, status_producto)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Producto agregado al inventario con éxito.")

        # Limpiar los campos de entrada después de agregar el producto
        self.entry_detalle_cantidad = None
        self.entry_detalle_costo = None
        
        # Inicializar la base de datos
        self.db_manager = DBManager()
    
    
    #def agregar_proveedor(self):
    #def agregar_cliente(self):
    
    #def detalle_reparacion(self):
    #def agregar_empleado(self):

    #def agregar_usuario(self):
        

    def agregar_producto(self):
        # Obtener la información ingresada por el usuario
        nombre_producto = self.entry_nombre_producto.get()#
        descripcion_producto = self.entry_descripcion.get()#
        precio_producto = self.entry_precio_producto.get()#
        cantidad_stock = self.entry_stock.get()#
        status_producto = self.entry_status_producto.get()
        fecha_creacion = datetime.now()
        # Validar que se hayan ingresado valores
        if not nombre_producto or not cantidad_stock or not descripcion_producto or not precio_producto or not status_producto:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            # Convertir la cantidad a un entero
            cantidad_stock = int(cantidad_stock)
            precio_producto = float(precio_producto)
            status_producto = int(status_producto)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        # Insertar el nuevo producto en el inventario
        self.db_manager.agregar_producto(nombre_producto, descripcion_producto, precio_producto, cantidad_stock, status_producto)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Producto agregado al inventario con éxito.")

        # Limpiar los campos de entrada después de agregar el producto
        """ self.entry_nombre_producto = None
        self.entry_descripcion = None
        self.entry_precio = None
        self.entry_stock = None
        self.entry_status_producto = None """
#        self.entry_fecha_creacion = None
        # Inicializar la base de datos
        self.db_manager = DBManager()

    # ... (resto del código es igual)

class DBManager:
    def __init__(self):
        # Conectar a la base de datos
        print("*******************************************************************************************************************************")
        self.conexion = sqlite3.connect('Electronica_Mimendi.db')
        self.cursor = self.conexion.cursor()

        # Crear tablas si no existen
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Producto (
                ID_Producto INTEGER PRIMARY KEY,
                Nombre TEXT UNIQUE,
                Descripcion TEXT,
                Precio REAL,
                Stock INTEGER,
                Status INTEGER,
                CreadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaCreacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                ModificadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaModificacion DATETIME
            )
        ''')
        print("Tabla creada con exito.")
        self.conexion.commit()
    def agregar_producto(self, nombre, descripcion, precio, stock, status):
        # Insertar el nuevo producto en la tabla 'Producto'
        creadopor = 1  # Puedes ajustar esto según tus necesidades
        modificado_por = 2  # Puedes ajustar esto según tus necesidades
        #Pewndiente el creado por
        self.cursor.execute("INSERT INTO Producto (Nombre, Descripcion, Precio, Stock, Status, CreadoPor, FechaCreacion, ModificadoPor, FechaModificacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (nombre, descripcion, precio, stock, status, creadopor, fecha_sqlite, modificado_por, fecha_sqlite))
        self.conexion.commit()

    def __del__(self):
        # Cerrar la conexión a la base de datos al destruir el objeto
        self.conexion.close()

# Resto del código...

if __name__ == "__main__":
    root = tk.Tk()
    app = PuntoDeVentaApp(root)
    root.mainloop() 
