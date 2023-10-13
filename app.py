from flask import Flask, request, jsonify
import os
import vtracer

app = Flask(__name__)

def convert_image_to_svg(image_path, output_path, conversion_params):
    # Convertir la imagen a SVG con los parámetros de configuración
    vtracer.convert_image_to_svg_py(image_path, output_path, **conversion_params)

    print(f"Imagen convertida a SVG. Archivo de salida: {output_path}")

@app.route('/convert', methods=['POST'])
def convert_image():
    # Directorio donde se almacenarán las imágenes
    upload_directory = 'uploads'
    os.makedirs(upload_directory, exist_ok=True)

    # Recibir la imagen
    image_file = request.files['image']
    image_path = os.path.join(upload_directory, image_file.filename)
    image_file.save(image_path)

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

    # Nombre de archivo de salida (con extensión SVG)
    output_filename = image_file.filename.rsplit('.', 1)[0] + ".svg"
    output_path = os.path.join(upload_directory, output_filename)

    # Convertir la imagen a SVG
    convert_image_to_svg(image_path, output_path, conversion_params)

    return jsonify({"message": "Imagen convertida a SVG.", "svg_file": output_filename})


if __name__ == '__main__':
    # Utiliza el puerto proporcionado por Netlify, o 5000 si no está definido
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

