import tkinter as tk
import urllib.request


def comprobamos_conectividad():
    # Limpiamos el canvas cada vez que llamamos a la funcion para que no se vea un texto encima del otro
    resultado_canvas.delete("all")
    

    url = entrada.get()
    if not url.startswith("https"):
        url = "https://" + url
    try:
        responde = urllib.request.urlopen(url)
        estado_actual = responde.getcode()
        if estado_actual == 200:
            texto = "El sitio Web introducido se encuentra "
            palabra = "ACTIVO"
            color_palabra = "green"
        else:
            texto = "El sitio Web introducido NO se encuentra activo en estos momentos"
            palabra = "NO"
            color_palabra = "red"

        # Dibujar texto en el canvas
        resultado_canvas.create_text(300, 30, text=texto, fill="black", font=("Helvetica", 12), anchor="center")
        if palabra:
            resultado_canvas.create_text(300, 50, text=palabra, fill=color_palabra, font=("Helvetica", 12, "bold"), anchor="center")
    except Exception as e:
        resultado_canvas.create_text(300,30,text="Introduce una web valida",fill="red", font=("Helvetica", 14), anchor="center")
        resultado_canvas.create_text(300, 60, text=f"Error: {str(e)}", fill="red", font=("Helvetica", 10), anchor="center")

def seleccionar_texto(event):
    # Seleccionar todo el texto dentro del Entry
    entrada.selection_range(0, tk.END)
    return "break"  # Evitar que Tkinter procese el evento por defecto 

# Crear ventana principal
raiz = tk.Tk()
raiz.title("Comprobador de sitios Web")
raiz.geometry("800x600")

# Etiqueta de título
titulo = tk.Label(raiz, text="Introduce la Web", font=("bold", 24))
titulo.place(relx=0.5, rely=0.06, anchor="center", relwidth=0.3, relheight=0.04)

# Campo de entrada
entrada = tk.Entry(raiz)
entrada.place(relx=0.5, rely=0.15, anchor="center", relwidth=0.3, relheight=0.04)

# Botón para verificar
boton_verificar = tk.Button(raiz, text="Verificar", command=comprobamos_conectividad)
boton_verificar.place(relx=0.5, rely=0.25, anchor="center", relwidth=0.15, relheight=0.06)

# Canvas para resultados (fijo en el centro)
resultado_canvas = tk.Canvas(raiz, width=600, height=100, highlightthickness=0)
resultado_canvas.place(relx=0.5, rely=0.37, anchor="center")

# Ejecutar la aplicación
entrada.bind("<Control-a>",seleccionar_texto)
raiz.mainloop()
