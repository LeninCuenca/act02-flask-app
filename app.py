import requests
from flask import Flask
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def home():
    # URL del archivo
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'

    # Obtener el contenido del archivo
    response = requests.get(url)
    contenido = response.text.splitlines()

    # Encabezados
    encabezados = contenido[0].split('|')
    filas = []

    # Filtrar y separar las filas
    for linea in contenido[1:]:
        partes = linea.split('|')
        if partes[0][0] in ['3', '4', '5', '7']:
            filas.append(partes)

    # Construir la tabla HTML
    tabla = '<table border="1" cellpadding="5"><tr>'
    tabla += ''.join([f'<th>{col}</th>' for col in encabezados]) + '</tr>'
    for fila in filas:
        tabla += '<tr>' + ''.join([f'<td>{dato}</td>' for dato in fila]) + '</tr>'
    tabla += '</table>'

    return Markup(tabla)

if __name__ == '__main__':
    app.run(debug=True)
