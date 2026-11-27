import tkinter as tk
from tkinter import ttk
from tkinter import ttk

ventana = tk.Tk()  # Ventana principal
ventana.title("Formulario con grid")

marco = ttk.Frame(ventana, padding=16)  # Agrupar controles
marco.grid(row=0, column=0, sticky="nsew")  # Empaquetar el marco

ttk.Label(marco, text="Correo:").grid(
    row=0, column=0, padx=5, pady=6)  # Etiqueta para el correo

correo = ttk.Entry(marco, width=28)
correo.grid(row=0, column=1, padx=5, pady=6)  # Empaquetar
# Empaquetar el campo de entrada

ttk.Button(marco, text="Aceptar").grid(row=1, column=1,
    sticky="e")
# sticky='e' (Alineado a la derecha/Este)
# Botón de aceptar

ventana.mainloop()