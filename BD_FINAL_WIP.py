from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry('600x600')
root.title("Registro Empleados")

tree = None

label_0 = Label(root, text="Registro de empleados.", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

def display_data():
    conn = sqlite3.connect('credenciales_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Empleados WHERE Status=1')
    rows = cursor.fetchall()
    conn.close()

    global tree

    if rows:
        display_window = Toplevel(root)
        display_window.title("Registro Empleados")
        display_window.geometry('800x400')

        tree = ttk.Treeview(display_window)
        tree["columns"] = ("ID", "Nombre", "ApellidoP", "ApellidoM", "Status", "Salario", "Cargo", "Telefono", "FechaInicio", "FechaModificacion")
        tree.heading("ID", text="ID Empleado")
        tree.column("ID", width=80)
        tree.heading("Nombre", text="Nombre", command=lambda: sort_column(tree, "Nombre", False))
        tree.column("Nombre", width=100)
        tree.heading("ApellidoP", text="Apellido Paterno", command=lambda: sort_column(tree, "ApellidoP", False))
        tree.column("ApellidoP", width=100)
        tree.heading("ApellidoM", text="Apellido Materno", command=lambda: sort_column(tree, "ApellidoM", False))
        tree.column("ApellidoM", width=100)
        tree.heading("Status", text="Status", command=lambda: sort_column(tree, "Status", False))
        tree.column("Status", width=60)
        tree.heading("Salario", text="Salario", command=lambda: sort_column(tree, "Salario", False))
        tree.column("Salario", width=80)
        tree.heading("Cargo", text="Cargo", command=lambda: sort_column(tree, "Cargo", False))
        tree.column("Cargo", width=100)
        tree.heading("Telefono", text="Teléfono", command=lambda: sort_column(tree, "Telefono", False))
        tree.column("Telefono", width=100)
        tree.heading("FechaInicio", text="Fecha Inicio", command=lambda: sort_column(tree, "FechaInicio", False))
        tree.column("FechaInicio", width=100)
        tree.heading("FechaModificacion", text="Fecha Modificación", command=lambda: sort_column(tree, "FechaModificacion", False))
        tree.column("FechaModificacion", width=120)

        for row in rows:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        tree.pack(fill="both", expand=True)
    else:
        messagebox.showinfo("Registro Vacio", "No se encontraron registros de empleados.")

def sort_column(tree, col, reverse):
    # Realizar la ordenación de los datos
    data = [(tree.set(item, col), item) for item in tree.get_children("")]
    data.sort(reverse=reverse)

    # Volver a insertar los elementos ordenados en la vista
    for index, (_, item) in enumerate(data):
        tree.move(item, "", index)

        # Actualizar los valores de la columna de ordenamiento
        values = tree.item(item)["values"]
        tree.item(item, values=(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9]))

def create_data():
    nombre = entry_nombre.get()
    apellidoP = entry_apellidoP.get()
    apellidoM = entry_apellidoM.get()
    status = 1
    salario = entry_salario.get()
    cargo = entry_cargo.get()
    telefono = entry_telefono.get()
    fecha_inicio = entry_fecha_inicio.get()
    fecha_modificacion = entry_fecha_modificacion.get()

    if nombre and apellidoP and apellidoM and salario and cargo and telefono and fecha_inicio and fecha_modificacion:
        conn = sqlite3.connect('credenciales_usuarios.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, Status, Salario, Cargo, Telefono, FechaInicio, FechaModificacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (nombre, apellidoP, apellidoM, status, salario, cargo, telefono, fecha_inicio, fecha_modificacion))
        conn.commit()
        conn.close()
        messagebox.showinfo("Creacion exitosa", "El empleado se ha creado con exito.")
    else:
        messagebox.showerror("Error", "Llena los parametros, pendejo.")
        
        
label_nombre = Label(root, text="Nombre:", width=20, font=("bold", 10))
label_nombre.place(x=80, y=130)

entry_nombre = Entry(root)
entry_nombre.place(x=240, y=130)

label_apellidoP = Label(root, text="Apellido Paterno:", width=20, font=("bold", 10))
label_apellidoP.place(x=80, y=160)

entry_apellidoP = Entry(root)
entry_apellidoP.place(x=240, y=160)

label_apellidoM = Label(root, text="Apellido Materno:", width=20, font=("bold", 10))
label_apellidoM.place(x=80, y=190)

entry_apellidoM = Entry(root)
entry_apellidoM.place(x=240, y=190)

label_salario = Label(root, text="Salario:", width=20, font=("bold", 10))
label_salario.place(x=80, y=220)

entry_salario = Entry(root)
entry_salario.place(x=240, y=220)

label_cargo = Label(root, text="Cargo:", width=20, font=("bold", 10))
label_cargo.place(x=80, y=250)

entry_cargo = Entry(root)
entry_cargo.place(x=240, y=250)

label_telefono = Label(root, text="Teléfono:", width=20, font=("bold", 10))
label_telefono.place(x=80, y=280)

entry_telefono = Entry(root)
entry_telefono.place(x=240, y=280)

label_fecha_inicio = Label(root, text="Fecha Inicio:", width=20, font=("bold", 10))
label_fecha_inicio.place(x=80, y=310)

entry_fecha_inicio = Entry(root)
entry_fecha_inicio.place(x=240, y=310)

label_fecha_modificacion = Label(root, text="Fecha Modificación:", width=20, font=("bold", 10))
label_fecha_modificacion.place(x=80, y=340)

entry_fecha_modificacion = Entry(root)
entry_fecha_modificacion.place(x=240, y=340)

def delete_data():
    selected_item = tree.focus()
    if selected_item:
        confirmed = messagebox.askyesno("Confirmar cambios", "Estas seguro de que quieres eliminar a un empleado?")
        if confirmed:
            item_values = tree.item(selected_item)['values']
            employee_id = item_values[0]
            conn = sqlite3.connect('credenciales_usuarios.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE Empleados SET Status = ? WHERE ID_Empleado = ?', (0, employee_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Exito", "Estatus del empleado cambiado.")
            display_data()
    else:
        messagebox.showerror("Error", "Selecciona un empleado, pendejo.")
    

def update_data():
    selected_item = tree.focus()
    if selected_item:
        item_values = tree.item(selected_item)['values']
        employee_id = item_values[0]
        
        nombre = entry_nombre.get()
        apellidoP = entry_apellidoP.get()
        apellidoM = entry_apellidoM.get()
        salario = entry_salario.get()
        cargo = entry_cargo.get()
        telefono = entry_telefono.get()
        fecha_inicio = entry_fecha_inicio.get()
        fecha_modificacion = entry_fecha_modificacion.get()
        
        if nombre and apellidoP and apellidoM and salario and cargo and telefono and fecha_inicio and fecha_modificacion:
            confirmed = messagebox.askyesno("Confirmar actualizacion", "Estas segura de que quieres actualizar la informacion del empleado?")
            if confirmed:
                conn = sqlite3.connect('credenciales_usuarios.db')
                cursor = conn.cursor()
                cursor.execute('UPDATE Empleados SET Nombre=?, ApellidoP=?, ApellidoM=?, Salario=?, Cargo=?, Telefono=?, FechaInicio=?, FechaModificacion=? WHERE ID_Empleado=?',
                               (nombre, apellidoP, apellidoM, salario, cargo, telefono, fecha_inicio, fecha_modificacion, employee_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Exito", "Actualizacion de informacion exitosa.")
                display_data()
        else:
            messagebox.showerror("Error", "Porfavor llena todos los campos.")
    else:
        messagebox.showerror("Error", "Selecciona un empleado de la lista.")
        

Button(root, text='Actualizar datos.', width=20, bg='brown', fg='white', command=update_data).place(x=180, y=500)

Button(root, text='Mostrar datos.', width=20, bg='brown', fg='white', command=display_data).place(x=180, y=380)

Button(root, text='Crear entrada.', width=20, bg='brown', fg='white', command=create_data).place(x=180, y=420)

Button(root, text='Cambiar estatus.', width=20, bg='brown', fg='white', command=delete_data).place(x=180, y=460)

root.mainloop()