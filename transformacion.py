import tkinter as tk
import numpy as np
from tkinter import messagebox

def transformacion_lineal(matriz, vector):
    matriz = np.array(matriz)
    vector = np.array(vector)
    return np.dot(matriz, vector)

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{pantalla_ancho}x{pantalla_alto}+{x}+{y}')

def realizar_transformacion():
    ventana = tk.Toplevel()
    ventana.title("Transformación Lineal")
    centrar_ventana(ventana, 400, 400)
    ventana.configure(bg='#E0F7FA')

    etiqueta_matriz = tk.Label(ventana, text="Ingrese la matriz (ejemplo: [[num,num],[num,num]])", font=("Arial", 12), bg='#E0F7FA', fg="black")
    etiqueta_matriz.pack(pady=10)
    entrada_matriz = tk.Entry(ventana, width=40, font=("Arial", 12))
    entrada_matriz.pack(pady=10)

    etiqueta_vector = tk.Label(ventana, text="Ingrese el vector (ejemplo: [num,num]) ", font=("Arial", 12), bg='#E0F7FA', fg="black")
    etiqueta_vector.pack(pady=10)
    entrada_vector = tk.Entry(ventana, width=40, font=("Arial", 12))
    entrada_vector.pack(pady=10)

    def calcular():
        try:
            matriz = eval(entrada_matriz.get())
            vector = eval(entrada_vector.get())
            resultado = transformacion_lineal(matriz, vector)
            messagebox.showinfo("Resultado", f"El resultado de la transformación es: {resultado}")
        except Exception as e:
            messagebox.showerror("Error", "Error en la entrada. Por favor ingresa una matriz y un vector válidos.")

    btn_calcular = tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12, "bold"), bg='#4FC3F7', fg='black')
    btn_calcular.pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    realizar_transformacion()
