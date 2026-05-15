import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def cargar_datos(ruta):
    textos = []
    etiquetas = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if ':' in linea:
                etiqueta, texto = linea.strip().split(':', 1)
                textos.append(texto.strip())
                etiquetas.append(etiqueta.strip())
    return textos, etiquetas

def limpiar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

textos, etiquetas = cargar_datos('intents.txt')
textos = [limpiar(t) for t in textos]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(textos)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X, etiquetas)

joblib.dump(modelo, 'modelo.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print('Modelo entrenado -', len(textos), 'ejemplos,', len(set(etiquetas)), 'intenciones')
