import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def descomposicion_qr(matriz):
    matriz = np.array(matriz)
    Q, R = np.linalg.qr(matriz)
    return Q, R

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{pantalla_ancho}x{pantalla_alto}+{x}+{y}')  

def crear_entradas(matriz_frame, filas, columnas):
    entradas = []
    for i in range(filas):
        fila_entradas = []
        for j in range(columnas):
            entry = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
            entry.grid(row=i, column=j, padx=5, pady=5)
            fila_entradas.append(entry)
        entradas.append(fila_entradas)
    return entradas

def calcular_descomposicion(entradas, filas, columnas):
    try:
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(entradas[i][j].get())
                fila.append(valor)
            matriz.append(fila)
        Q, R = descomposicion_qr(matriz)
        resultado_texto = f"Matriz Q:\n{Q}\n\nMatriz R:\n{R}"
        messagebox.showinfo("Resultado de la descomposición QR", resultado_texto)
    except Exception as e:
        messagebox.showerror("Error", "Hubo un problema con los datos ingresados. Asegúrate de que todo esté en el formato correcto.")

def mostrar_grafica_qr(entradas, filas, columnas, ventana):
    try:
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(entradas[i][j].get())
                fila.append(valor)
            matriz.append(fila)
        Q, _ = descomposicion_qr(matriz)
        fig = plt.Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        for i in range(Q.shape[1]):
            ax.plot([0, Q[0, i]], [0, Q[1, i]], label=f'Vector Q {i+1}', marker='o')
        ax.set_title("Vectores de la Matriz Q")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.legend()
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)
    except Exception as e:
        messagebox.showerror("Error", "Hubo un problema con los datos ingresados. Asegúrate de que todo esté en el formato correcto.")

def realizar_desco_qr():
    ventana = tk.Toplevel()
    ventana.title("Descomposición QR")
    centrar_ventana(ventana, 500, 600) 
    ventana.configure(bg='#E0F7FA')

    contenedor = tk.Frame(ventana, bg='#E0F7FA', padx=20, pady=20, bd=2, relief="solid")
    contenedor.pack(pady=20)

    label_filas = tk.Label(contenedor, text="Ingrese el número de filas:", font=("Arial", 12), bg='#E0F7FA', fg="black")
    label_filas.pack(pady=5)
    entry_filas = tk.Entry(contenedor, width=40, font=("Arial", 12))
    entry_filas.pack(pady=5)
    
    label_columnas = tk.Label(contenedor, text="Ingrese el número de columnas:", font=("Arial", 12), bg='#E0F7FA', fg="black")
    label_columnas.pack(pady=5)
    entry_columnas = tk.Entry(contenedor, width=40, font=("Arial", 12))
    entry_columnas.pack(pady=5)

    btn_calcular = None
    btn_grafica = None

    def generar_matriz():
        nonlocal btn_calcular, btn_grafica
        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())
            if filas <= 0 or columnas <= 0:
                raise ValueError("Las filas y columnas deben ser números positivos.")

            for widget in matriz_frame.winfo_children():
                widget.destroy()
            entradas = crear_entradas(matriz_frame, filas, columnas)
            
            if btn_calcular is None:
                btn_calcular = tk.Button(contenedor, text="Calcular Descomposición", command=lambda: calcular_descomposicion(entradas, filas, columnas), font=("Arial", 12, "bold"), bg='#4FC3F7', fg='black')
                btn_calcular.pack(pady=10)

            if btn_grafica is None:
                btn_grafica = tk.Button(contenedor, text="Mostrar Gráfica", command=lambda: mostrar_grafica_qr(entradas, filas, columnas, ventana), font=("Arial", 12, "bold"), bg='#4FC3F7', fg='black')
                btn_grafica.pack(pady=10)
            
            btn_generar.pack_forget()
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    matriz_frame = tk.Frame(contenedor)
    matriz_frame.pack(pady=10)

    btn_generar = tk.Button(contenedor, text="Generar Matriz", command=generar_matriz, font=("Arial", 12, "bold"), bg='#4FC3F7', fg='black')
    btn_generar.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    realizar_desco_qr()
