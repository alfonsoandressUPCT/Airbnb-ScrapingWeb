
# 🏠 Airbnb-ScrapingWeb

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
  ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
  ![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)
  ![License](https://img.shields.io/badge/Licencia-MIT-yellow)
  ![Status](https://img.shields.io/badge/Estado-Activo-brightgreen)
</div>

## 📋 Descripción

Airbnb-ScrapingWeb es una herramienta avanzada de web scraping desarrollada en Python diseñada para extraer y analizar datos de alojamientos de Airbnb. El proyecto permite recopilar información detallada como precios, ubicaciones, valoraciones y características de los alojamientos para análisis posterior.

Esta herramienta está desarrollada con fines educativos y de investigación, permitiendo entender mejor el mercado de alojamientos temporales y realizar análisis de datos para identificar tendencias, comparar precios y evaluar zonas geográficas.

## 🚀 Características principales

- 🔍 **Extracción automatizada** de datos de listados de Airbnb
- 💰 Análisis de precios por zona, temporada y tipo de alojamiento
- 📊 Visualización de datos con gráficos interactivos
- 📍 Geolocalización y representación en mapas de los alojamientos
- 💾 Exportación de datos a formatos CSV y Excel
- 📈 Monitoreo de cambios de precios a lo largo del tiempo
- 🤖 Integración con modelos de IA para análisis de datos avanzado
- 🌐 Soporte para traducción automática de descripciones

## 🔧 Requisitos previos

- Python 3.8 o superior
- Jupyter Notebook/JupyterLab
- Navegador web compatible con Selenium
- Conexión a Internet

## 🛠️ Tecnologías utilizadas

- **Web Scraping**: Selenium, BeautifulSoup4, Requests, Scrapy, Playwright
- **Análisis de datos**: Pandas, NumPy, Scikit-learn
- **Visualización**: Matplotlib, Seaborn, Plotly, Folium
- **Geocodificación**: GeoPy, GeoPandas
- **IA & NLP**: LlamaIndex, ChromaDB
- **Otros**: Traducción automática, manejo de archivos, utilidades diversas

## ⚙️ Instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/alfonsoandressUPCT/Airbnb-ScrapingWeb.git
cd Airbnb-ScrapingWeb
```

2. **Crear y activar un entorno virtual** (opcional pero recomendado):
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

3. **Instalar las dependencias**:
```bash
pip install -r requirements.txt
```

4. **Configurar el archivo de entrada**:
   - Crea una carpeta `input` si no existe
   - Dentro de esta carpeta, crea un archivo `input.txt` con los parámetros de búsqueda (ver ejemplo en la sección de uso)

## 🖥️ Uso

### Configuración del archivo de entrada

Crea un archivo `input/input.txt` con el siguiente formato:
```
ciudad = "Madrid"
pais = "España"
fecha_entrada = "01/05/2025"
fecha_salida = "05/05/2025"
numero_adultos = 2
numero_niños = 0
numero_bebes = 0
numero_mascotas = 0
numero_pagina = 3
```

### Ejecutar el proyecto

1. **Iniciar Jupyter Notebook**:
```bash
jupyter notebook
```

2. **Abrir y ejecutar el notebook principal**:
   - Navega hasta `Airbnb - Scraping Web.ipynb`
   - Ejecuta las celdas secuencialmente para realizar el proceso de scraping

### Flujo de trabajo

1. El sistema automatiza la navegación en Airbnb con los parámetros proporcionados
2. Extrae datos de los alojamientos (nombres, precios, servicios, ubicación)
3. Procesa y limpia los datos recopilados
4. Genera visualizaciones y análisis estadísticos
5. Exporta los resultados a archivos CSV/Excel

## 📊 Análisis y visualización

El proyecto incluye diversas funcionalidades para analizar los datos extraídos:

- **Mapas interactivos**: Visualización geoespacial de alojamientos con Folium
- **Análisis de precios**: Comparativas, tendencias y valores atípicos
- **Clustering**: Agrupación de alojamientos por características similares
- **Dashboards**: Paneles de control para visualizar métricas clave

## 🤖 Integración con IA

El proyecto incorpora capacidades de análisis mediante IA utilizando:

- Modelos locales mediante Ollama
- Embeddings y vectorización para búsquedas semánticas
- Análisis automatizado de características y tendencias

## ⚠️ Consideraciones éticas y legales

Este proyecto está diseñado exclusivamente con fines educativos y de investigación. Al utilizar esta herramienta, asegúrate de:

- Respetar los términos de servicio de Airbnb
- No saturar los servidores con demasiadas peticiones (implementa retrasos adecuados)
- Utilizar los datos de manera ética y responsable
- No almacenar ni procesar información personal de los anfitriones o huéspedes
- Cumplir con la legislación de protección de datos aplicable en tu jurisdicción

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del proyecto
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`)
4. Sube los cambios (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## ❓ Preguntas frecuentes

**P: ¿Es legal hacer web scraping en Airbnb?**  
R: El web scraping debe realizarse respetando los términos de servicio del sitio web y las leyes aplicables. Este proyecto es con fines educativos y debes usarlo responsablemente.

**P: ¿Cómo evitar ser bloqueado durante el scraping?**  
R: El proyecto implementa retrasos entre peticiones, rotación de user agents y técnicas anti-detección con undetected-chromedriver.

**P: ¿Puedo usar estos datos para un negocio comercial?**  
R: No se recomienda el uso comercial de datos extraídos sin permiso explícito de Airbnb.

## 📄 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).

## 📧 Contacto

Alfonso Andrés - [@alfonsoandressUPCT](https://github.com/alfonsoandressUPCT)

---

<div align="center">
  <p>© 2025 Alfonso Andrés Giménez Sánchez. Todos los derechos reservados.</p>
</div>
