# **🏠 Airbnb-ScrapingWeb**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)
![License](https://img.shields.io/badge/Licencia-MIT-yellow)
![Status](https://img.shields.io/badge/Estado-Activo-brightgreen)


## **📋 Descripción del Proyecto**

Esta aplicación implementa un sistema avanzado de web scraping para la plataforma Airbnb, permitiendo a los usuarios obtener información detallada sobre alojamientos disponibles según criterios específicos. El proyecto incluye una interfaz gráfica intuitiva y genera análisis completos de los datos obtenidos, facilitando la comparación de precios, servicios y ubicaciones.

## **🚀 Características Principales**

- **🖥️ Interfaz Gráfica Intuitiva**: Diseñada con CustomTkinter y Tkinter, ofrece una experiencia de usuario moderna y funcional.

- **🔎 Búsqueda Personalizada y Detallada**: 
  - Selección precisa de destino (país y ciudad)
  - Configuración flexible del número y tipo de viajeros (adultos, niños, bebés, mascotas)
  - Selección de fechas de entrada y salida mediante calendario interactivo

- **🤖 Extracción Automatizada de Datos**: 
  - Navega automáticamente por Airbnb utilizando Selenium y ChromeDriver
  - Gestiona cookies y elementos interactivos del sitio
  - Obtiene datos completos de cada alojamiento

- **📊 Análisis Multidimensional de Resultados**:

  - **💸 Análisis Económico**: 
    - Estadísticas descriptivas (media, mediana, desviación estándar)
    - Visualizaciones avanzadas (histogramas, diagramas de caja, diagrmas de dispersión, diagramas de barras, diagramas de líneas)
    - Identificación de valores máximos, mínimos y modas

  - **🛠️ Análisis de Servicios**: 
    - Frecuencia y distribución de servicios ofrecidos
    - Visualización gráfica de los servicios más comunes

  - **🌍 Análisis Geográfico**: 
    - Mapa interactivo con clusters de alojamientos
    - Codificación por colores según nivel de precios. Rojo si es mayor que la media y verde si es menor.
    
- **💾 Exportación Completa de Resultados**: 
  - Archivos CSV con datos detallados
  - Visualizaciones en formato PNG de alta calidad
  - Mapas interactivos en HTML
  - Informes de estadísticas en formato TXT

## **🏛️ Estructura del Proyecto**

El proyecto está organizado en diferentes secciones funcionales:

1. **Implementación de Librerías y Paquetes**: Configuración de las herramientas necesarias para el scraping, análisis y visualización.

2. **Inicio del Programa**: Configuración inicial y preparación del entorno.

3. **Extracción de Datos**: Navegación automatizada y obtención de información.

4. **Limpieza y Ordenación de Datos**: Procesamiento para garantizar la calidad y consistencia.

5. **Interpretación de Datos**: Análisis estadístico y generación de visualizaciones.

6. **Exportación de Datos**: Almacenamiento de resultados en formatos accesibles.

7. **Ventana Gráfica**: Interfaz de usuario para controlar todo el proceso.

## **🔌 Requisitos del Sistema**

Para ejecutar correctamente la aplicación, es necesario tener instalados:

- Python 3.8 o superior
- Navegador Chrome actualizado
- Conexión a Internet estable
- Espacio en disco para almacenar resultados

## **🔋 Instalación**

1. Clona el repositorio:
```bash
git clone https://github.com/alfonsoandressUPCT/Airbnb-ScrapingWeb.git
cd Airbnb-ScrapingWeb
```

2. Crea un entorno virtual (opcional pero recomendable):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

4. Asegúrate de tener Chrome instalado en tu sistema y que la versión sea compatible con el ChromeDriver utilizado.

## **📸 Uso**

1. Ejecuta el script principal:
```bash
python "Airbnb - Scraping Web.py"
```

2. En la interfaz gráfica:

  - Introduce el país y ciudad de destino
  - Selecciona el número de viajeros (adultos, niños, bebés, mascotas)
  - Elige las fechas de entrada y salida con el calendario interactivo
  - Haz clic en "Iniciar Búsqueda"

3. La aplicación realizará el proceso de scraping y análisis automáticamente, mostrando el progreso en tiempo real.

4. Una vez completado, podrás acceder a los resultados mediante los botones de la interfaz o directamente en la carpeta output:

  - `[Ciudad]. [Número de Personas]. [Fecha Entrada] | [Fecha Salida]/`
    - `Análisis de Datos/:` Datos completos en formato CSV
    - `Análisis de Servicios/:` Gráficos de servicios disponibles
    - `Análisis Económico/:` Estadísticas y visualizaciones de precios
      - `Diagrama de Cajas/:` Visualizaciones de la distribución de precios
      - `Histograma/:` Distribución de frecuencias de precios
      - `Medidas Descriptivas/:` Estadísticas numéricas en formato texto
    - `Análisis Geográfico/:` Mapas interactivos con ubicaciones codificadas por precio

## **📈 Flujo de Trabajo del Programa**

1. **Configuración Inicial:** Carga de librerías y preparación del entorno.
2. **Apertura del Navegador:** Inicialización de Chrome con configuraciones anti-detección.
3. **Navegación en Airbnb:** Introducción automática de parámetros de búsqueda.
4. **Extracción de Datos:** Obtención de información de cada alojamiento.
5. **Procesamiento de Datos:** Limpieza y estructuración de la información.
6. **Análisis Estadístico:** Cálculo de métricas y generación de visualizaciones.
7. **Exportación de Resultados:** Almacenamiento en formatos accesibles.
8. **Presentación de Resultados:** Interfaz para explorar los análisis generados.

## **🧑‍💻 Consideraciones Técnicas**

- La aplicación utiliza técnicas avanzadas para evitar ser detectada como un bot.
- Se implementan pausas aleatorias para simular comportamiento humano.
- El código maneja excepciones para garantizar la robustez del proceso.
- Se optimiza el rendimiento para minimizar el tiempo de ejecución.

## **⚖️ Consideraciones Legales**

Este proyecto se proporciona únicamente con fines educativos y de investigación. El web scraping debe realizarse de acuerdo con los términos y condiciones de Airbnb. El uso de esta herramienta es responsabilidad del usuario final.

## **🤝 Contribuciones**

Las contribuciones son bienvenidas. Si deseas colaborar con el proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/NuevaCaracteristica`)
3. Realiza tus cambios y haz commit (`git commit -m 'Añade nueva característica'`)
4. Sube tus cambios (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## **📧 Autor**

**Alfonso Andrés Giménez Sánchez - Estudiante del Grado de Ciencia e Ingeniería de Datos en la Universidad Politécnica de Cartagena (UPCT) - [@alfonsoandressUPCT](https://github.com/alfonsoandressUPCT)**

## **📄 Licencia**

**© Alfonso Andrés Giménez Sánchez. Todos los derechos reservados.**