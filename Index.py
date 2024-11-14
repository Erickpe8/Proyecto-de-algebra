import tkinter as tk
from transformacion import realizar_transformacion
from producto import realizar_producto_interior
from desco_qr import realizar_desco_qr

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

def main_window():
    root = tk.Tk()
    root.title("Proyecto Pedagogico de aula de Algebra")
    root.configure(bg='#E0F7FA') 

    root.attributes("-fullscreen", True) 

    label_titulo = tk.Label(root, text="Proyecto Pedagogico de aula de Algebra", font=("Arial", 32, "bold"), bg='#E0F7FA', fg='black')
    label_titulo.pack(pady=40)

    frame_seleccion = tk.Frame(root, bd=2, relief=tk.SOLID, padx=10, pady=10, bg='#B2EBF2')
    frame_seleccion.pack(pady=20, padx=20, fill=tk.X)

    label_seleccion = tk.Label(frame_seleccion, text="Selecciona una Operación", font=("Arial", 18), bg='#B2EBF2', fg='black')
    label_seleccion.pack()

    frame_opciones = tk.Frame(root, bd=2, relief=tk.SOLID, padx=20, pady=20, bg='#B2EBF2')
    frame_opciones.pack(pady=20, padx=20)

    btn_transformacion = tk.Button(frame_opciones, text="Transformación Lineal", command=realizar_transformacion, 
                                   width=20, height=3, bg='#4FC3F7', fg='black', font=("Arial", 14, "bold"))
    btn_transformacion.grid(row=0, column=0, padx=10)

    btn_producto = tk.Button(frame_opciones, text="Producto Interior", command=realizar_producto_interior, 
                             width=20, height=3, bg='#4FC3F7', fg='black', font=("Arial", 14, "bold"))
    btn_producto.grid(row=0, column=1, padx=10)

    btn_descomposicion = tk.Button(frame_opciones, text="Descomposición QR", command=realizar_desco_qr, 
                                   width=20, height=3, bg='#4FC3F7', fg='black', font=("Arial", 14, "bold"))
    btn_descomposicion.grid(row=0, column=2, padx=10)

    label_creditos = tk.Label(root, text="Desarrollado por: Daniel Daza, Josue Pineda y Neider Gomez ", font=("Arial", 12), bg='#E0F7FA', fg='black')
    label_creditos.pack(side="bottom", pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_window()
