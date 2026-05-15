import sys
import re
import random
import joblib

modelo = joblib.load('modelo.pkl')
vectorizer = joblib.load('vectorizer.pkl')

respuestas = {
    'saludo': [
        'Hola, en que puedo ayudarte?',
        'Bienvenido, como estas?',
        'Hey, que tal?'
    ],
    'compra': [
        'Que producto buscas?',
        'Tenemos varias opciones disponibles.',
        'Que deseas comprar?'
    ],
    'soporte': [
        'Cual es el problema?',
        'Te ayudo enseguida, explica el error.',
        'Vamos a solucionarlo.'
    ],
    'precio': [
        'Claro, tenemos diferentes precios segun el producto.',
        'Puedo consultarte los precios. Que producto te interesa?',
        'Los precios varian. Dime que buscas y te doy el costo.'
    ],
    'gracias': [
        'De nada, para eso estoy!',
        'Un placer ayudarte.',
        'A ti por preguntar, que tengas buen dia.'
    ],
    'horario': [
        'Abrimos de lunes a viernes de 9:00 a 18:00 y sabados de 10:00 a 14:00.',
        'Horario: L-V 9am-6pm y Sab 10am-2pm.',
        'Estamos abiertos entre semana de 9am a 6pm y los sabados hasta las 2pm.'
    ],
    'contacto': [
        'Puedes contactarnos al correo soporte@tienda.com o al telefono 555-1234.',
        'Nuestro correo es soporte@tienda.com y el telefono 555-1234.',
        'Contactanos en soporte@tienda.com o llamanos al 555-1234.'
    ],
    'ubicacion': [
        'Estamos en Av. Principal #123, Colonia Centro.',
        'Nos ubicamos en Av. Principal 123, Col. Centro.',
        'Direccion: Av. Principal #123, Colonia Centro.'
    ],
    'devolucion': [
        'Puedes devolver el producto dentro de 30 dias con el ticket.',
        'Aceptamos devoluciones hasta 30 dias. El producto debe estar en su empaque original.',
        'Claro, la devolucion tiene un plazo de 30 dias. Necesitas el ticket de compra.'
    ],
    'despedida': [
        'Adios, que tengas buen dia!',
        'Hasta luego, cuidate.',
        'Nos vemos, gracias por conversar.'
    ]
}

def limpiar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

# recive el texto desde PHP
entrada = sys.argv[1]
entrada = limpiar(entrada)

# predecir intencion
X = vectorizer.transform([entrada])
pred = modelo.predict(X)[0]
proba = modelo.predict_proba(X).max()

if proba < 0.25:
    print('No estoy seguro de entenderte. Puedes reformular?')
else:
    print(random.choice(respuestas[pred]))
