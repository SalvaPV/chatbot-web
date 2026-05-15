# Chatbot Web

Chatbot con PHP + Python + TF-IDF + Regresion Logistica.

## Como correrlo

### Windows (XAMPP)

1. Copiar la carpeta a `C:\xampp\htdocs\chatbot_web\`
2. Instalar Python y correr:
   ```
   pip install scikit-learn joblib
   ```
3. Abrir XAMPP y iniciar Apache
4. Ir a `http://localhost/chatbot_web`

### Mac

```bash
pip3 install scikit-learn joblib
php -S localhost:8080
```

Ir a `http://localhost:8080`

### Entrenar el modelo (opcional)

```bash
python train.py
```
