import tkinter as tk
import numpy as np
from tkinter import messagebox

def producto(vector1, vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    return np.dot(vector1, vector2)

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{pantalla_ancho}x{pantalla_alto}+{x}+{y}')

def realizar_producto_interior():
    ventana = tk.Toplevel()
    ventana.title("Producto Interior")
    centrar_ventana(ventana, 400, 400)
    ventana.configure(bg='#E0F7FA')

    etiqueta_1 = tk.Label(ventana, text="Ingrese el primer vector (ejemplo: [num,num]) ", font=("Arial", 12), bg='#E0F7FA', fg="black")
    etiqueta_1.pack(pady=10)
    entrada_1 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entrada_1.pack(pady=10)

    etiqueta_2 = tk.Label(ventana, text="Ingrese el segundo vector (ejemplo: [num,num]) ", font=("Arial", 12), bg='#E0F7FA', fg="black")
    etiqueta_2.pack(pady=10)
    entrada_2 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entrada_2.pack(pady=10)

    def calcular():
        try:
            vector1 = eval(entrada_1.get())
            vector2 = eval(entrada_2.get())
            resultado = producto(vector1, vector2)
            messagebox.showinfo("Resultado", f"El producto interior es: {resultado}")
        except Exception as e:
            messagebox.showerror("Error", "Error en la entrada. Por favor ingresa dos vectores válidos.")

    btn_calcular = tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12, "bold"), bg='#4FC3F7', fg='black')
    btn_calcular.pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    realizar_producto_interior()
