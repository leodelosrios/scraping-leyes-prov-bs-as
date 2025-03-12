# 📜 Scraping de Leyes de la Provincia de Buenos Aires

Este proyecto permite realizar **web scraping** de la base de datos de normas jurídicas de la Provincia de Buenos Aires.
Utiliza **Python, asyncio y aiohttp** para realizar múltiples solicitudes en paralelo, extrayendo información de hasta **15.520 leyes** de manera eficiente. 🚀

## ⚡ Características

- 🔄 **Scraping Asíncrono**: Utiliza `aiohttp` y `asyncio` para obtener datos de manera paralela.
- 📑 **Almacenamiento en CSV**: Guarda los datos extraídos en un archivo `leyes.csv` con el siguiente formato:

  ```csv
  numero_ley,resumen,url
  1000,"Descripción de la ley 1000","https://normas.gba.gob.ar/ar-b/ley/1875/1000/12036"
  ```

- 🌐 **Extracción de Datos Clave**:
  - Número de ley 📌
  - Resumen 📝
  - URL 🔗
- 🚦 **Manejo de errores**: Ignora leyes inexistentes y maneja solicitudes fallidas.

## 🛠 Instalación y Uso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/leodelosrios/scraping-leyes-prov-bs-as.git
cd scraping-leyes-prov-bs-as
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar el script

```bash
python scraping.py
```

## 📢 Ejemplo de salida en consola

Cada vez que se encuentra una ley, se muestra en la terminal:

```bash
Ley encontrada: 1000
Ley encontrada: 1024
Ley encontrada: 1100
...
```

## 🏗 Tecnologías Utilizadas

- **Python 3** 🐍
- **aiohttp** (para solicitudes HTTP asíncronas) ⚡
- **asyncio** (para ejecutar tareas en paralelo) 🔄
- **BeautifulSoup** (para extraer datos del HTML) 🏗
- **CSV** (para almacenar los datos extraídos) 📂

## 📌 Contacto y Contribuciones

📧 Contacto: [GitHub](https://github.com/leodelosrios)

¡Gracias por tu interés en este proyecto! 😊
