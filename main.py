from fastapi import FastAPI
import requests
import vtracer

app = FastAPI ()

@app.get("/")

def index ():
    return
import tkinter as tk
from tkinter import filedialog


def convert_image_to_svg():
    # Solicitar al usuario que seleccione una imagen
    filepath = filedialog.askopenfilename(title="Seleccionar imagen",
                                          filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")])
    if not filepath:
        return  # El usuario canceló la selección

    # Crear el nombre del archivo de salida (con extensión SVG)
    output_filepath = filepath.rsplit('.', 1)[0] + ".svg"

    # Parámetros de configuración para la conversión
    conversion_params = {
        'colormode': 'color',        # ["color"] or "binary"
        'hierarchical': 'stacked',   # ["stacked"] or "cutout"
        'mode': 'spline',            # ["spline"] "polygon", or "none"
        'filter_speckle': 4,         # default: 4
        'color_precision': 6,        # default: 6
        'layer_difference': 16,      # default: 16
        'corner_threshold': 60,      # default: 60
        'length_threshold': 4.0,     # in [3.5, 10] default: 4.0
        'max_iterations': 10,        # default: 10
        'splice_threshold': 45,      # default: 45
        'path_precision': 3          # default: 8
    }

    # Convertir la imagen a SVG con los parámetros de configuración
    vtracer.convert_image_to_svg_py(filepath, output_filepath, **conversion_params)

    print(f"Imagen convertida a SVG. Archivo de salida: {output_filepath}")

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de imagen a SVG")

# Botón para iniciar la conversión
convert_button = tk.Button(root, text="Convertir a SVG", command=convert_image_to_svg)
convert_button.pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()
