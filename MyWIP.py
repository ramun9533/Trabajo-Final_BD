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
        btn_agregar_cliente = tk.Button(self.tab_cliente, text="Agregar cliente", command=self.agregar_cliente)
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
        btn_agregar_proveedor = tk.Button(self.tab_proveedor, text="Agregar proveedor", command=self.agregar_proveedor)
        btn_agregar_proveedor.grid(row=5, column=0, columnspan=5, pady=10)

    def inicializar_interfaz_reparacion(self):
        # Etiqueta y cuadro de texto para ingresar el status de la reparacion
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
        # Etiquetas y cuadros de texto.
        lbl_nombre = tk.Label(self.tab_empleados, text="Nombre:")
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.tab_empleados)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        lbl_apellido_p = tk.Label(self.tab_empleados, text="Apellido Paterno:")
        lbl_apellido_p.grid(row=1, column=0, padx=10, pady=10)
        self.entry_apellido_p = tk.Entry(self.tab_empleados)
        self.entry_apellido_p.grid(row=1, column=1, padx=10, pady=10)

        lbl_apellido_m = tk.Label(self.tab_empleados, text="Apellido Materno:")
        lbl_apellido_m.grid(row=2, column=0, padx=10, pady=10)
        self.entry_apellido_m = tk.Entry(self.tab_empleados)
        self.entry_apellido_m.grid(row=2, column=1, padx=10, pady=10)

        lbl_status = tk.Label(self.tab_empleados, text="Status:")
        lbl_status.grid(row=3, column=0, padx=10, pady=10)
        self.entry_status = tk.Entry(self.tab_empleados)
        self.entry_status.grid(row=3, column=1, padx=10, pady=10)

        lbl_salario = tk.Label(self.tab_empleados, text="Salario:")
        lbl_salario.grid(row=4, column=0, padx=10, pady=10)
        self.entry_salario = tk.Entry(self.tab_empleados)
        self.entry_salario.grid(row=4, column=1, padx=10, pady=10)

        lbl_cargo = tk.Label(self.tab_empleados, text="Cargo:")
        lbl_cargo.grid(row=5, column=0, padx=10, pady=10)
        self.entry_cargo = tk.Entry(self.tab_empleados)
        self.entry_cargo.grid(row=5, column=1, padx=10, pady=10)

        lbl_telefono = tk.Label(self.tab_empleados, text="Teléfono:")
        lbl_telefono.grid(row=6, column=0, padx=10, pady=10)
        self.entry_telefono = tk.Entry(self.tab_empleados)
        self.entry_telefono.grid(row=6, column=1, padx=10, pady=10)

        lbl_fecha_inicio = tk.Label(self.tab_empleados, text="Fecha de Inicio:")
        lbl_fecha_inicio.grid(row=7, column=0, padx=10, pady=10)
        self.entry_fecha_inicio = tk.Entry(self.tab_empleados)
        self.entry_fecha_inicio.grid(row=7, column=1, padx=10, pady=10)

        boton_agregar_empleado = tk.Button(self.tab_empleados, text="Agregar empleado", command=self.agregar_empleado)
        boton_agregar_empleado.grid(row=8, column=0, columnspan=5, pady=10)

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

        btn_agregar_Usuario = tk.Button(self.tab_usuarios, text="Agregar usuario", command=self.agregar_usuario)
        btn_agregar_Usuario.grid(row=4, column=0, columnspan=5, pady=10)

       
    # Captura de datos
 
    
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
        self.entry_cantidad.delete(0, 'end')
        self.entry_precio_del_producto.delete(0, 'end')
    
    def agregar_reparacion(self):
        # Inicializar la base de datos
        self.db_manager = DBManager()

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
        self.db_manager.agregar_reparacion(reparacion_cantidad, detalle_costo)
        # self.db_manager.agregar_producto(nombre_producto, descripcion_producto, precio_producto, cantidad_stock, status_producto)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Reparacion agregada con éxito.")

        # Limpiar los campos de entrada después de agregar el producto
        self.entry_detalle_cantidad.delete(0, 'end')
        self.entry_detalle_costo.delete(0, 'end')
    
    
    #def agregar_proveedor(self):
    def agregar_proveedor(self):
        # Conexion con el editor.
        self.db_manager = DBManager()

        # Declarar parametros.
        nombre_proveedor = self.entry_proveedor.get()
        status_proveedor = self.entry_status.get()
        telefono_proveedor = self.entry_telefono.get()
        correo_proveedor = self.entry_telefono.get()

        if not nombre_proveedor or not status_proveedor or not telefono_proveedor or not correo_proveedor:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        # Llamar a la funcion para agregar al proveedor.
        self.db_manager.agregar_proveedor(nombre_proveedor, status_proveedor, telefono_proveedor, correo_proveedor)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Proveedor agregado con éxito.")

        # Limpiar los campos de entrada después de agregar el producto
        self.entry_proveedor.delete(0, 'end')
        self.entry_status.delete(0, 'end')
        self.entry_telefono.delete(0, 'end')
        self.entry_telefono.delete(0, 'end')
        self.entry_detalle_cantidad.delete(0, 'end')
        self.entry_detalle_costo.delete(0, 'end')

    #def agregar_cliente(self):
    def agregar_cliente(self):
        # Conexion con el editor.
        self.db_manager = DBManager()

        # Declarar variables.
        cliente = self.entry_nombre_cliente.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono_cliente.get()
        correo = self.entry_correo_cliente.get()

        if not cliente or not direccion or not telefono or not correo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        # Llamar a la funcion para insertar a los clientes.
        self.db_manager.agregar_cliente(cliente, direccion, telefono, correo)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Producto agregado al inventario con éxito.")

        self.entry_nombre_cliente.delete(0, 'end')
        self.entry_direccion.delete(0, 'end')
        self.entry_telefono_cliente.delete(0, 'end')
        self.entry_correo_cliente.delete(0, 'end')
    
    #def detalle_reparacion(self):
    #def agregar_empleado(self):
    def agregar_empleado(self):
        # Conexion con el editor.
        self.db_manager = DBManager()

        # Declarar variables.
        nombre = self.entry_nombre.get()
        apellido_p = self.entry_apellido_p.get()
        apellido_m = self.entry_apellido_m.get()
        status = self.entry_status.get()
        salario = self.entry_salario.get()
        cargo = self.entry_cargo.get()
        telefono = self.entry_telefono.get()
        fecha_inicio = self.entry_fecha_inicio.get()

        if not nombre or not apellido_p or not apellido_m or not status or not salario or not cargo or not telefono or not fecha_inicio:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        # Llamar a la funcion para insertar a los clientes.
        self.db_manager.agregar_empleado(nombre, apellido_p, apellido_m, status, salario, cargo, telefono, fecha_inicio)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Producto agregado al inventario con éxito.")

        self.entry_nombre.delete(0, 'end')
        self.entry_apellido_p.delete(0, 'end')
        self.entry_apellido_m.delete(0, 'end')
        self.entry_status.delete(0, 'end')
        self.entry_salario.delete(0, 'end')
        self.entry_cargo.delete(0, 'end')
        self.entry_telefono.delete(0, 'end')
        self.entry_fecha_inicio.delete(0, 'end')

    #def agregar_usuario(self):
    def agregar_usuario(self):
        # Inicializar la base de datos
        self.db_manager = DBManager()

        nombre_usuario = self.entry_NombreUsuario.get()
        contraseña = self.entry_Contraseña.get()

        if not nombre_usuario or not contraseña:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Insertar el nuevo producto en el inventario
        self.db_manager.agregar_usuario(nombre_usuario, contraseña)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Usuario agregado con éxito.")

        # Limpiar los campos.
        self.entry_NombreUsuario.delete(0, 'end')
        self.entry_Contraseña.delete(0, 'end')
        

    def agregar_producto(self):
        # Inicializar la base de datos
        self.db_manager = DBManager()

        # Obtener la información ingresada por el usuario
        nombre_producto = self.entry_nombre_producto.get()
        descripcion_producto = self.entry_descripcion.get()
        precio_producto = self.entry_precio_producto.get()
        cantidad_stock = self.entry_stock.get()
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

        # Limpiar los campos.
        self.entry_nombre_producto.delete(0, 'end')
        self.entry_descripcion.delete(0, 'end')
        self.entry_precio_producto.delete(0, 'end')
        self.entry_stock.delete(0, 'end')
        self.entry_status_producto.delete(0, 'end')

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
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Empleados (
                ID_Empleado INTEGER PRIMARY KEY,
                Nombre TEXT,
                ApellidoP TEXT,
                ApellidoM TEXT,
                Status INTEGER,
                Salario REAL,
                Cargo TEXT,
                Telefono TEXT,
                FechaInicio DATETIME DEFAULT CURRENT_TIMESTAMP,
                FechaModificacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                -- Restricción única para evitar empleados duplicados basados en nombre y apellidos
                CONSTRAINT unique_empleado UNIQUE (Nombre, ApellidoP, ApellidoM)
            )''')

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS DetalleReparacion (
                ID_DetalleReparacion INTEGER PRIMARY KEY,
                ID_Reparacion INTEGER REFERENCES Reparacion(ID_Reparacion),
                ID_Producto INTEGER REFERENCES Producto(ID_Producto),
                Cantidad INTEGER,
                Costo REAL,
                CreadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaCreacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                ModificadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaModificacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Cliente (
                ID_Cliente INTEGER PRIMARY KEY,
                Nombre TEXT,
                Direccion TEXT,
                Telefono TEXT,
                Correo TEXT,
                CreadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaCreacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                ModificadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaModificacion DATETIME DEFAULT CURRENT_TIMESTAMP
            ) """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Proveedor (
                ID_Proveedor INTEGER PRIMARY KEY,
                Nombre TEXT,
                ApellidoP TEXT,
                ApellidoM TEXT,
                Status INTEGER,
                Correo TEXT,
                Direccion TEXT,
                Telefono TEXT,
                CreadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaCreacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                ModificadoPor INTEGER REFERENCES Empleados(ID_Empleado),
                FechaModificacion DATETIME DEFAULT CURRENT_TIMESTAMP
            ) """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios (
            ID_Usuario INTEGER PRIMARY KEY,
            ID_Empleado INTEGER,
            NombreUsuario TEXT UNIQUE,
            Contraseña TEXT,
            Rol INTEGER,
            Status INTEGER,
            FOREIGN KEY (ID_Empleado) REFERENCES Empleados (ID_Empleado),
            FOREIGN KEY (Status) REFERENCES Empleados (Status)
        ) """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Empleados (
            ID_Empleado INTEGER PRIMARY KEY,
            Nombre TEXT,
            ApellidoP TEXT,
            ApellidoM TEXT,
            Status INTEGER,
            Salario REAL,
            Cargo TEXT,
            Telefono TEXT,
            FechaInicio DATETIME DEFAULT CURRENT_TIMESTAMP,
            FechaModificacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            ModificadoPor INTEGER REFERENCES Empleados(ID_Empleado),
            -- Restricción única para evitar empleados duplicados basados en nombre y apellidos
            CONSTRAINT unique_empleado UNIQUE (Nombre, ApellidoP, ApellidoM)
        )""")

        print("Tabla creada con exito.")
        self.conexion.commit()
    
    def agregar_empleado(self, nombre, apellido_p, apellido_m, status, salario, cargo, telefono, fecha_inicio):
        modificado_por = 2
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, Status, Salario, Cargo, Telefono, FechaInicio, FechaModificacion, ModificadoPor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (nombre, apellido_p, apellido_m, status, salario, cargo, telefono, fecha_inicio, fecha_actual, modificado_por))
        self.conexion.commit()
        self.conexion.close()

    def agregar_producto(self, nombre, descripcion, precio, stock, status):
        creadopor = 1
        modificado_por = 2
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO Producto (Nombre, Descripcion, Precio, Stock, Status, CreadoPor, FechaCreacion, ModificadoPor, FechaModificacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (nombre, descripcion, precio, stock, status, creadopor, fecha_actual, modificado_por, fecha_actual))
        self.conexion.commit()
        self.conexion.close()
    
    def agregar_reparacion(self, reparacion_cantidad, detalle_costo):
        creadopor = 1
        modificado_por = 2
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO DetalleReparacion (Cantidad, Costo, CreadoPor, FechaCreacion, ModificadoPor, FechaModificacion) VALUES (?, ?, ?, ?, ?, ?)",
                            (reparacion_cantidad, detalle_costo, creadopor, fecha_actual, modificado_por, fecha_actual))
        self.conexion.commit()
        self.conexion.close()

    def agregar_cliente(self, nombre, direccion, telefono, correo):
        creadopor = 1
        modificado_por = 2
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO Cliente (Nombre, Direccion, Telefono, Correo, CreadoPor, FechaCreacion, ModificadoPor, FechaModificacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (nombre, direccion, telefono, correo, creadopor, fecha_actual, modificado_por, fecha_actual))
        self.conexion.commit()
        self.conexion.close()

    def agregar_proveedor(self, nombre, status, telefono, correo):
        creadopor = 1
        modificado_por = 2
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO Proveedor (Nombre, Telefono, Correo, CreadoPor, FechaCreacion, ModificadoPor, FechaModificacion) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (nombre, telefono, correo, creadopor, fecha_actual, modificado_por, fecha_actual))
        self.conexion.commit()
        self.conexion.close()

    def agregar_usuario(self, nombre, contraseña):
        creadopor = 1
        modificado_por = 2
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO Usuarios (NombreUsuario, Contraseña) VALUES (?, ?)",
                            (nombre, contraseña))
        self.conexion.commit()
        self.conexion.close()

    def __del__(self):
        # Cerrar la conexión a la base de datos al destruir el objeto
        self.conexion.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PuntoDeVentaApp(root)
    root.mainloop() 
