import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()  # Instanciar ventana principal
ventana.title("Saludo interactivo")
ventana.geometry("360x180")

def saludar():  # Función invocada cuando se hace clic
    nombre = entrada.get().strip()  # Leer y quitar espacios extremos
    if not nombre:  # Comprobar que exista un nombre
        messagebox.showwarning("Dato requerido", "Ingrese su nombre")  # Mostrar mensaje de advertencia
        return  # Detener el procesamiento si está vacío
    messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")  # Mostrar mensaje de saludo

ttk.Label(ventana, text="Nombre:").pack(pady=(16, 4))  # Etiqueta para el campo de entrada
entrada = ttk.Entry(ventana)  # Campo de una línea
entrada.pack(padx=20, fill="x")  # Empaquetar con relleno horizontal y margen lateral
ttk.Button(ventana, text="Saludar", command=saludar).pack(pady=12)  # Botón que invoca la función saludar al hacer
ventana.mainloop()  # Ejecutar interfaz