#### **© Alfonso Andrés Giménez Sánchez**. Todos los derechos reservados
# **AIRBNB. Proyecto de Ciencia de Datos**
print("\nBienvenido a Scraping-Web de Airbnb")
print("Comenzamos con el proyecto\n")
## **1. Implementación de Librerías y Paquetes**
print("\n1. Implementación de Librerías y Paquetes")
### **1.1. Web Scraping**
print("\n\t1.1. Web Scraping")
print("\n\t\tProceso iniciado")
import requests
import undetected_chromedriver as uc

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
print("\n\t\tProceso finalizado")
### **1.2. Análisis y Manipulación de Datos**
print("\n\t1.2. Análisis y Manipulación de Datos")
print("\n\t\tProceso iniciado")
import pandas as pd
import numpy as np
import re

from datetime import datetime
print("\n\t\tProceso finalizado")
### **1.3. Geolocalización y Visualización en Mapas**
print("\n\t1.3. Geolocalización y Visualización en Mapas")
print("\n\t\tProceso iniciado")
import folium

from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
print("\n\t\tProceso finalizado")
### **1.4. Traducción**
print("\n\t1.4. Traducción")
print("\n\t\tProceso iniciado")
from translate import Translator
print("\n\t\tProceso finalizado")
### **1.5. Visualización de Datos**
print("\n\t1.5. Visualización de Datos")
print("\n\t\tProceso iniciado")
import matplotlib.pyplot as plt
import seaborn as sns
print("\n\t\tProceso finalizado")
### **1.6. Creación de un Agente de Inteligencia Artificial**
print("\n\t1.6. Creación de un Agente de Inteligencia Artificial")
print("\n\t\tProceso iniciado")
import subprocess
import chromadb
import logging
import striprtf.striprtf as striprtf

from llama_index.llms.ollama import Ollama

from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core import ServiceContext
from llama_index.core import StorageContext

from llama_index.core.vector_stores import SimpleVectorStore

from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.vector_stores.chroma import ChromaVectorStore

from llama_index.core import Settings

from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.core import PromptHelper

from dotenv import load_dotenv

from PIL import Image
print("\n\t\tProceso finalizado")
### **1.7. Otras Utilidades**
print("\n\t1.7. Otras Utilidades")
print("\n\t\tProceso iniciado")
from collections import Counter

import warnings
import random
import time
import os
import ssl
import shutil

ssl._create_default_https_context = ssl._create_unverified_context
print("\n\t\tProceso finalizado")
## **2. Inicio del Contador**
print("\n2. Inicio del Contador")
contador_inicio = time.time()
## **3. Extracción de Datos**
print("\n3. Extracción de Datos")
### **3.1. Apertura del Navegador en el Sitio Web**
print("\n\t3.1. Apertura del Navegador en el Sitio Web")
print("\n\t\tProceso iniciado")
browser = uc.Chrome(headless=False)

time.sleep(3)

url = 'https://www.airbnb.es'

browser.get(url)

time.sleep(2)
print("\n\t\tProceso finalizado")
### **3.2. Eliminación de Mensaje de Cookies**
print("\n\t3.2. Eliminación de Mensaje de Cookies")
print("\n\t\tProceso iniciado")
cockies_botton = browser.find_element(By.XPATH, "//button[contains(text(), 'Solo las necesarias')]")

cockies_botton.click()

time.sleep(0.5)
print("\n\t\tProceso finalizado")
### **3.3. Extracción del HTML**
print("\n\t3.3. Extracción del HTML")
print("\n\t\tProceso iniciado")
html = browser.page_source

soup = bs(html, 'lxml')
print("\n\t\tProceso finalizado")
### **3.4. Lectura de Datos desde el Fichero y Creación de Carpeta para Resultados**
print("\n\t3.4. Lectura de Datos desde el Fichero")
print("\n\t\tProceso iniciado")
def cargar_variables(ruta):
    variables = {}
    with open(ruta, 'r') as f:
        for linea in f:
            if '=' in linea:
                clave, valor = linea.strip().split('=', 1)
                clave = clave.strip()
                valor = valor.strip()
                try:
                    valor = eval(valor)
                except:
                    pass
                variables[clave] = valor
    return variables

variables = cargar_variables('input/input.txt')

for clave, valor in variables.items():
    globals()[clave] = valor

fecha_entrada_objetivo = datetime.strptime(fecha_entrada, "%d/%m/%Y")
fecha_salida_objetivo = datetime.strptime(fecha_salida, "%d/%m/%Y")

dia_entrada = str(fecha_entrada[0:2])

dia_entrada_nombre = fecha_entrada_objetivo.strftime("%A")

mes_entrada = str(fecha_entrada[3:5])

mes_entrada_nombre = fecha_entrada_objetivo.strftime("%B")

año_entrada = str(fecha_entrada[6:10])

dia_salida = str(fecha_salida[0:2])

dia_salida_nombre = fecha_salida_objetivo.strftime("%A")

mes_salida = str(fecha_salida[3:5])

mes_salida_nombre = fecha_salida_objetivo.strftime("%B")

año_salida = str(fecha_salida[6:10])

fecha_entrada_str = fecha_entrada.replace('/', '-')
fecha_salida_str = fecha_salida.replace('/', '-')

numero_total_personas = numero_adultos + numero_niños + numero_bebes + numero_mascotas

directorios = list()

directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis de Datos')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis de Servicios')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico/Diagrama de Cajas')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico/Histograma')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico/Medidas Descriptivas')
directorios.append(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Geográfico')

for directorio in directorios:
    if not os.path.exists(directorio):
        os.makedirs(directorio)
print("\n\t\tProceso finalizado")
### **3.5. Selección del Destino del Viaje**
print("\n\t3.5. Selección del Destino del Viaje")
print("\n\t\tProceso iniciado")
Destino = f"{ciudad}, {pais}"

campo_destino = browser.find_element(By.ID, "bigsearch-query-location-input")
campo_destino.send_keys(Destino)
campo_destino.send_keys(Keys.ENTER)

time.sleep(2)
print("\n\t\tProceso finalizado")
### **3.6. Selección de Fechas del Viaje**
print("\n\t3.6. Selección de Fechas del Viaje")
print("\n\t\tProceso iniciado")
translator = Translator(to_lang="es", from_lang="en")

mes_entrada_nombre_español = Translator(to_lang="es").translate(mes_entrada_nombre).lower()

mes_año = f"{mes_entrada_nombre_español} {año_entrada}"

mes_actual = browser.find_element(By.XPATH, '//h2[contains(@class, "h19aqaok")]').text

while mes_actual != mes_año:
   
    boton_siguiente = browser.find_element(By.XPATH, '//button[@aria-label[contains(.,"cambiar al mes siguiente")]]').click()
    time.sleep(1)
    mes_actual = browser.find_element(By.XPATH, '//h2[contains(@class, "h19aqaok")]').text

time.sleep(3)

tarjeta_fecha_entrada = f"{dia_entrada}, {dia_entrada_nombre}, {mes_entrada_nombre} {año_entrada}. Disponible. Selecciona este día como fecha de llegada." # Texto único del atributo aria-label 

date_button = browser.find_element(By.XPATH, f"//button[@aria-label='{tarjeta_fecha_entrada}']") 
date_button.click()

time.sleep(3)

tarjeta_fecha_salida = f"{dia_salida}, {dia_salida_nombre}, {mes_salida_nombre} {año_salida}. Disponible. Selecciona este día como fecha de salida." # Texto único del atributo aria-label 

date_button = browser.find_element(By.XPATH, f"//button[@aria-label='{tarjeta_fecha_salida}']") 
date_button.click()
print("\n\t\tProceso finalizado")
### **3.7. Selección de Viajeros del Viaje**
print("\n\t3.7. Selección de Viajeros del Viaje")
print("\n\t\tProceso iniciado")
viajeros_button = browser.find_element(By.XPATH, "//div[div[text()='Viajeros']]/div[text()='Añade viajeros']")
viajeros_button.click()

for n in range(0, numero_adultos):
    increase_adults_button = browser.find_element(By.XPATH, "//button[@data-testid='stepper-adults-increase-button']")
    increase_adults_button.click()
    time.sleep(0.5)

for n in range(0, numero_niños):
    increase_childrens_button = browser.find_element(By.XPATH, "//button[@data-testid='stepper-children-increase-button']")
    increase_childrens_button.click()
    time.sleep(0.5)

for n in range(0, numero_bebes):
    increase_babies_button = browser.find_element(By.XPATH, "//button[@data-testid='stepper-infants-increase-button']")
    increase_babies_button.click()
    time.sleep(0.5)

for n in range(0, numero_mascotas):
    increase_pets_button = browser.find_element(By.XPATH, "//button[@data-testid='stepper-pets-increase-button']")
    increase_pets_button.click()
    time.sleep(0.5)
print("\n\t\tProceso finalizado")
### **3.8. Realización de la Búsqueda de Ubicaciones para el Viaje**
print("\n\t3.8. Realización de la Búsqueda de Ubicaciones para el Viaje")
print("\n\t\tProceso iniciado")
search_button = browser.find_element(By.XPATH, "//button[@data-testid='structured-search-input-search-button']")
search_button.click()

time.sleep(5)
print("\n\t\tProceso finalizado")
### **3.9. Extracción de Datos de los Alojamientos**
print("\n\t3.9. Extracción de Datos de los Alojamientos")
print("\n\t\tProceso iniciado")
data = []

for pagina in range(numero_pagina):

    url_inicio_alojamientos = browser.current_url

    alojamientos = browser.find_elements(By.XPATH, "//div[@itemprop='itemListElement']")

    links = list()

    for url in alojamientos:
        try:
            url = url.find_element(By.XPATH, ".//meta[@itemprop='url']").get_attribute("content")
            links.append(url)
        except Exception as e:
            print("Error en una tarjeta:", e)
            continue

    for link in links:
        url = link

        if not url.startswith("http"):
            url = "https://" + url

        browser.get(url)
        time.sleep(4)

        try:
            # Cierra el botón del traductor si aparece
            traductor_botton = browser.find_element(By.XPATH, "//button[@aria-label='Cerrar']")
            traductor_botton.click()
        except:
            pass  # Si no aparece, continúa

        time.sleep(2)

        try:
            nombre = browser.find_element(By.XPATH, "//h1[contains(@class, 'hpipapi')]").text
        except:
            nombre = "No disponible"

        time.sleep(1)

        try:
            spans = browser.find_elements(By.XPATH, "//span[contains(text(),'€')]")
            precios_noche = [s.text for s in spans if "noche" in s.text.lower()]
            if precios_noche:
                precio_noche = precios_noche[0].split("€")[0].strip() + " €"
            else:
                precio_noche = "No disponible"
        except:
            precio_noche = "No disponible"

        time.sleep(1)

        try:
            spans_total = browser.find_elements(By.XPATH, "//span[@class='_j1kt73']")
            precios = [s.text for s in spans_total if "€" in s.text]
            if precios:
                precio_total = precios[0].split("€")[0].replace(",", "").strip() + " €"
            else:
                precio_total = "No disponible"
        except:
            precio_total = "No disponible"

        time.sleep(1)

        try:
            servicios_elements = browser.find_elements(By.CSS_SELECTOR, 'div._19xnuo97 > div > div:first-child')
            servicios = ", ".join([s.text for s in servicios_elements if s.text.strip()])
        except:
            servicios = "No disponible"

        scroll_pause_time = 0.5  # Tiempo de pausa entre desplazamientos
        screen_height = browser.execute_script("return window.innerHeight;")  # Altura de la ventana
        scroll_position = 0
        while True:
            # Desplázate hacia abajo
            browser.execute_script(f"window.scrollTo(0, {scroll_position});")
            scroll_position += screen_height  # Incrementa la posición de desplazamiento
            time.sleep(scroll_pause_time)  # Pausa para permitir la carga del contenido

            # Verifica si se ha llegado al final de la página
            new_scroll_height = browser.execute_script("return document.body.scrollHeight;")
            if scroll_position >= new_scroll_height:
                break

        time.sleep(2)

        try:
            url_element = browser.find_element(By.XPATH, "//a[@title='Informar a Google acerca de errores en las imágenes o en el mapa de carreteras']")
            url_coordenadas = url_element.get_attribute("href")

            match = re.search(r"@([-\d.]+),([-\d.]+)", url_coordenadas)

            lat = match.group(1)  # Latitud
            latitud = float(lat)  # Convertir a float
            lon = match.group(2)  # Longitud
            longitud = float(lon)  # Convertir a float

        except:
            latitud = "No Disponible"
            longitud = "No Disponible"

        time.sleep(2)

        data.append({
            'Nombre': nombre,
            'Precio por Noche': precio_noche,
            'Precio Total': precio_total,
            'Servicios': servicios,
            'Latitud': latitud,
            'Longitud': longitud,
            'URL': url
        })

    browser.get(url_inicio_alojamientos)

    time.sleep(2)

    scroll_pause_time = 0.5  # Tiempo de pausa entre desplazamientos
    screen_height = browser.execute_script("return window.innerHeight;")  # Altura de la ventana
    scroll_position = 0

    while True:
        # Desplázate hacia abajo
        browser.execute_script(f"window.scrollTo(0, {scroll_position});")
        scroll_position += screen_height  # Incrementa la posición de desplazamiento
        time.sleep(scroll_pause_time)  # Pausa para permitir la carga del contenido

        # Verifica si se ha llegado al final de la página
        new_scroll_height = browser.execute_script("return document.body.scrollHeight;")
        if scroll_position >= new_scroll_height:
            break

    time.sleep(2)
    
    boton_siguiente_pagina = browser.find_element(By.XPATH, '//*[@id="site-content"]/div/div[3]/div/div/div/nav/div/a[5]')
    boton_siguiente_pagina.click()
    
    time.sleep(2)
print("\n\t\tProceso finalizado")
### **3.10. Cierre del Navegador**
print("\n\t3.10. Cierre del Navegador")
print("\n\t\tProceso iniciado")
browser.close()
browser.quit()
print("\n\t\tProceso finalizado")
### **3.11. Creación de Dataframe con Datos Extraídos de cada Alojamiento**
print("\n\t3.11. Creación de Dataframe con Datos Extraídos de cada Alojamiento")
print("\n\t\tProceso iniciado")
df = pd.DataFrame(data)
print("\n\t\tProceso finalizado")
## **4. Limpieza y Ordenación de Datos**
print("\n4. Limpieza y Ordenación de Datos")
### **4.1. Cálculo de Precio por Viajero**
print("\n\t4.1. Cálculo de Precio por Viajero")
print("\n\t\tProceso iniciado")
# Limpiar el precio y convertirlo a float
def extraer_precio(precio_str):
    if isinstance(precio_str, str) and '€' in precio_str:
        try:
            numero = precio_str.split(' ')[0].replace('.', '').replace(',', '.')
            return float(numero)
        except ValueError:
            return None
    return None

df['Precio por Noche por Viajero'] = df['Precio por Noche'].apply(lambda x: extraer_precio(x) / numero_adultos if extraer_precio(x) is not None else "No Disponible")

df['Precio Total por Viajero'] = df['Precio Total'].apply(lambda x: extraer_precio(x) / numero_adultos if extraer_precio(x) is not None else "No Disponible")
                                                          
df = df[['Nombre', 'Precio por Noche', 'Precio por Noche por Viajero', 'Precio Total', 'Precio Total por Viajero', 'Latitud', 'Longitud', 'Servicios', 'URL']]
print("\n\t\tProceso finalizado")
### **4.2. Eliminación de Filas No Disponibles**
print("\n\t4.2. Eliminación de Filas No Disponibles")
print("\n\t\tProceso iniciado")
indices = df[df.eq("No Disponible").any(axis=1)].index.tolist()
df = df.drop(indices)
df = df.reset_index(drop=True)
print("\n\t\tProceso finalizado")
### **4.3. Formateo de Servicios con Viñetas**
print("\n\t4.3. Formateo de Servicios con Viñetas")
print("\n\t\tProceso iniciado")
# Formatear los servicios con viñetas
def formatear_servicios(servicios):
    if servicios and isinstance(servicios, str):
        return "\n".join([f"- {servicio.strip()}" for servicio in servicios.split(",") if servicio.strip()])
    return "No disponible"

df['Servicios'] = df['Servicios'].apply(formatear_servicios)
print("\n\t\tProceso finalizado")
### **4.4. Aproximación y Redondeo de Precios**
print("\n\t4.4. Aproximación y Redondeo de Precios")
print("\n\t\tProceso iniciado")
columnas_a_redondear = ['Precio por Noche por Viajero', 'Precio Total por Viajero']

for columna in columnas_a_redondear:
    # Aseguramos que son numéricos
    df[columna] = pd.to_numeric(df[columna], errors='coerce')
    
    # Redondeamos hacia arriba y convertimos a enteros
    df[columna] = np.ceil(df[columna]).astype(float)
print("\n\t\tProceso finalizado")
### **4.5. Conversión de Datos Económicos a Datos Numéricos**
print("\n\t4.5. Conversión de Datos Económicos a Datos Numéricos")
print("\n\t\tProceso iniciado")
# Función para limpiar y convertir los precios a float
def convertir_a_entero(precio):
    if isinstance(precio, str):
        return int(precio.replace("€", "").replace(".", "").replace(",", ".").strip())
    return precio

# Aplicar la función a las columnas correspondientes
df["Precio por Noche"] = df["Precio por Noche"].apply(convertir_a_entero)
df["Precio Total"] = df["Precio Total"].apply(convertir_a_entero)
df["Precio por Noche por Viajero"] = pd.to_numeric(df["Precio por Noche por Viajero"]).astype(int)
df["Precio Total por Viajero"] = pd.to_numeric(df["Precio Total por Viajero"]).astype(int)
print("\n\t\tProceso finalizado")
### **4.6. Capitalización de Nombre de los Títulos**
print("\n\t4.6. Capitalización de Nombre de los Títulos")
print("\n\t\tProceso iniciado")
df['Nombre'] = df['Nombre'].str.title()
print("\n\t\tProceso finalizado")
## **5. Interpretación de Datos**
print("\n5. Interpretación de Datos")
### **5.1. Análisis Económico**
print("\n\t5.1. Análisis Económico")
#### **5.1.1. Medias de los Precios**
print("\n\t\t5.1.1. Medias de los Precios")
print("\n\t\t\tProceso iniciado")
media_precio_noche = df['Precio por Noche'].mean()
media_precio_noche_viajero = df['Precio por Noche por Viajero'].mean()
media_precio_total = df['Precio Total'].mean()
media_precio_total_viajero = df['Precio Total por Viajero'].mean()

medias = (
    f"Medias de los Precios de Alojamientos en {ciudad}:\n"
    f"----------------------------------------\n"
    f"Media del Precio por Noche: {media_precio_noche:.2f} €\n"
    f"Media del Precio por Noche por Viajero: {media_precio_noche_viajero:.2f} €\n"
    f"Media del Precio Total: {media_precio_total:.2f} €\n"
    f"Media del Precio Total por Viajero: {media_precio_total_viajero:.2f} €\n"
)
print("\n\t\t\tProceso finalizado")
#### **5.1.2. Medianas de los Precios**
print("\n\t\t5.1.2. Medianas de los Precios")
print("\n\t\t\tProceso iniciado")
mediana_precio_noche = df['Precio por Noche'].median()
mediana_precio_noche_viajero = df['Precio por Noche por Viajero'].median()
mediana_precio_total = df['Precio Total'].median()
mediana_precio_total_viajero = df['Precio Total por Viajero'].median()

medianas = (
    f"Medianas de los Precios de Alojamientos en {ciudad}:\n"
    f"----------------------------------------\n"
    f"Mediana del Precio por Noche: {mediana_precio_noche:.2f} €\n"
    f"Mediana del Precio por Noche por Viajero: {mediana_precio_noche_viajero:.2f} €\n"
    f"Mediana del Precio Total: {mediana_precio_total:.2f} €\n"
    f"Mediana del Precio Total por Viajero: {mediana_precio_total_viajero:.2f} €\n"
)
print("\n\t\t\tProceso finalizado")
#### **5.1.3. Desviaciones Estándar de los Precios**
print("\n\t\t5.1.3. Desviaciones Estándar de los Precios")
print("\n\t\t\tProceso iniciado")
desviacion_precio_noche = df['Precio por Noche'].std()
desviacion_precio_noche_viajero = df['Precio por Noche por Viajero'].std()
desviacion_precio_total = df['Precio Total'].std()
desviacion_precio_total_viajero = df['Precio Total por Viajero'].std()

desviaciones_tipicas = (
    f"Desviaciones Típicas de los Precios de Alojamientos en {ciudad}:\n"
    f"----------------------------------------\n"
    f"Desviación Estándar del Precio por Noche: {desviacion_precio_noche:.2f} €\n"
    f"Desviación Estándar del Precio por Noche por Viajero: {desviacion_precio_noche_viajero:.2f} €\n"
    f"Desviación Estándar del Precio Total: {desviacion_precio_total:.2f} €\n"
    f"Desviación Estándar del Precio Total por Viajero: {desviacion_precio_total_viajero:.2f} €\n"
)
print("\n\t\t\tProceso finalizado")
#### **5.1.4. Modas de los Precios**
print("\n\t\t5.1.4. Modas de los Precios")
print("\n\t\t\tProceso iniciado")
moda_precio_noche = df['Precio por Noche'].mode()[0]
df['Moda Precio por Noche'] = df['Precio por Noche'].apply(lambda x: 'X' if x == moda_precio_noche else '')

moda_precio_noche_viajero = df['Precio por Noche por Viajero'].mode()[0]
df['Moda Precio por Noche por Viajero'] = df['Precio por Noche por Viajero'].apply(lambda x: 'X' if x == moda_precio_noche_viajero else '')

moda_precio_total = df['Precio Total'].mode()[0]
df['Moda Precio Total'] = df['Precio Total'].apply(lambda x: 'X' if x == moda_precio_total else '')

moda_precio_total_viajero = df['Precio Total por Viajero'].mode()[0]
df['Moda Precio Total por Viajero'] = df['Precio Total por Viajero'].apply(lambda x: 'X' if x == moda_precio_total_viajero else '')
print("\n\t\t\tProceso finalizado")
#### **5.1.5. Precios Máximos**
print("\n\t\t5.1.5. Precios Máximos")
print("\n\t\t\tProceso iniciado")
maximo_precio_noche = df['Precio por Noche'].max()
df['Máximo Precio por Noche'] = df['Precio por Noche'].apply(lambda x: 'X' if x == maximo_precio_noche else '')

maximo_precio_noche_viajero = df['Precio por Noche por Viajero'].max()
df['Máximo Precio por Noche por Viajero'] = df['Precio por Noche por Viajero'].apply(lambda x: 'X' if x == maximo_precio_noche_viajero else '')

maximo_precio_total = df['Precio Total'].max()
df['Máximo Precio Total'] = df['Precio Total'].apply(lambda x: 'X' if x == maximo_precio_total else '')

maximo_precio_total_viajero = df['Precio Total por Viajero'].max()
df['Máximo Precio Total por Viajero'] = df['Precio Total por Viajero'].apply(lambda x: 'X' if x == maximo_precio_total_viajero else '')
print("\n\t\t\tProceso finalizado")
#### **5.1.6. Precios Mínimos**
print("\n\t\t5.1.6. Precios Mínimos")
print("\n\t\t\tProceso iniciado")
minimo_precio_noche = df['Precio por Noche'].min()
df['Mínimo Precio por Noche'] = df['Precio por Noche'].apply(lambda x: 'X' if x == minimo_precio_noche else '')

minimo_precio_noche_viajero = df['Precio por Noche por Viajero'].min()
df['Mínimo Precio por Noche por Viajero'] = df['Precio por Noche por Viajero'].apply(lambda x: 'X' if x == minimo_precio_noche_viajero else '')

minimo_precio_total = df['Precio Total'].min()
df['Mínimo Precio Total'] = df['Precio Total'].apply(lambda x: 'X' if x == minimo_precio_total else '')

minimo_precio_total_viajero = df['Precio Total por Viajero'].min()
df['Mínimo Precio Total por Viajero'] = df['Precio Total por Viajero'].apply(lambda x: 'X' if x == minimo_precio_total_viajero else '')
print("\n\t\t\tProceso finalizado")
#### **5.1.7. Representación Gráfica de Precios**
print("\n\t\t5.1.7. Representación Gráfica de Precios")
##### **5.1.7.1. Histogramas**
print("\n\t\t\t5.1.7.1. Histogramas")
print("\n\t\t\t\tProceso iniciado")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Histograma de Precios por Noche
sns.histplot(df['Precio por Noche'], bins=20, color='blue', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Histograma de Precios por Noche')
axes[0, 0].set_xlabel('Precio por Noche (€)')
axes[0, 0].set_ylabel('Frecuencia')

# Histograma de Precios por Noche por Viajero
sns.histplot(df['Precio por Noche por Viajero'], bins=20, color='blue', kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Histograma de Precios por Noche por Viajero')
axes[0, 1].set_xlabel('Precio por Noche por Viajero (€)')
axes[0, 1].set_ylabel('Frecuencia')

# Histograma de Precios Totales
sns.histplot(df['Precio Total'], bins=20, color='blue', kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Histograma de Precios Totales')
axes[1, 0].set_xlabel('Precio Total (€)')
axes[1, 0].set_ylabel('Frecuencia')

# Histograma de Precios Totales por Viajero
sns.histplot(df['Precio Total por Viajero'], bins=20, color='blue', kde=True, ax=axes[1, 1])
axes[1, 1].set_title('Histograma de Precios Totales por Viajero')
axes[1, 1].set_xlabel('Precio Total por Viajero (€)')
axes[1, 1].set_ylabel('Frecuencia')

plt.tight_layout()
plt.savefig(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico/Histograma/Histograma - {ciudad}.png')
plt.close(fig)
print("\n\t\t\t\tProceso finalizado")
##### **5.1.7.2. Diagramas de Caja**
print("\n\t\t\t5.1.7.2. Diagramas de Caja")
print("\n\t\t\t\tProceso iniciado")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Diagrama de caja de Precios por Noche
sns.boxplot(data=df, y='Precio por Noche', ax=axes[0, 0], color='blue')
axes[0, 0].set_title('Diagrama de Caja de Precios por Noche')
axes[0, 0].set_ylabel('Precio por Noche (€)')

# Diagrama de caja de Precios por Noche por Viajero
sns.boxplot(data=df, y='Precio por Noche por Viajero', ax=axes[0, 1], color='blue')
axes[0, 1].set_title('Diagrama de Caja de Precios por Noche por Viajero')
axes[0, 1].set_ylabel('Precio por Noche por Viajero (€)')

# Diagrama de caja de Precios Totales
sns.boxplot(data=df, y='Precio Total', ax=axes[1, 0], color='blue')
axes[1, 0].set_title('Diagrama de Caja de Precios Totales')
axes[1, 0].set_ylabel('Precio Total (€)')

# Diagrama de caja de Precios Totales por Viajero
sns.boxplot(data=df, y='Precio Total por Viajero', ax=axes[1, 1], color='blue')
axes[1, 1].set_title('Diagrama de Caja de Precios Totales por Viajero')
axes[1, 1].set_ylabel('Precio Total por Viajero (€)')

plt.tight_layout()
plt.savefig(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico/Diagrama de Cajas/Diagrama Caja - {ciudad}.png')
plt.close(fig)
print("\n\t\t\t\tProceso finalizado")
### **5.2. Análisis de Servicios**
print("\n\t5.2. Análisis de Servicios")
#### **5.2.1. Extracción de los Servicios**
print("\n\t\t5.2.1. Extracción de los Servicios")
print("\n\t\t\tProceso iniciado")
# Copiamos solo la columna de servicios para trabajar
servicios_raw = df['Servicios'].dropna().copy()

def extraer_servicios(servicio_str):
    lineas = servicio_str.strip().split('\n')
    servicios_ok = []
    
    for linea in lineas:
        linea = linea.strip().lstrip('- ').strip()
        if linea.startswith("No disponible:"):
            continue
        servicios_ok.append(linea)
    
    return servicios_ok

# Aplicamos a cada alojamiento para obtener listas de servicios
listas_de_servicios = servicios_raw.apply(extraer_servicios)

# Aplanamos todas las listas en una sola
todos_los_servicios = [servicio for sublist in listas_de_servicios for servicio in sublist]
print("\n\t\t\tProceso finalizado")
#### **5.2.2. Contamos las Frecuencias de los Servicios**
print("\n\t\t5.2.2. Contamos las Frecuencias de los Servicios")
print("\n\t\t\tProceso iniciado")
frecuencias_servicios = Counter(todos_los_servicios)
print("\n\t\t\tProceso finalizado")
#### **5.2.3. Creación de un Dataframe de los Servicios**
print("\n\t\t5.2.3. Creación de un Dataframe de los Servicios")
print("\n\t\t\tProceso iniciado")
servicios_df = pd.DataFrame(frecuencias_servicios.items(), columns=['Servicio', 'Frecuencia'])
servicios_df = servicios_df.sort_values(by='Frecuencia', ascending=False)
print("\n\t\t\tProceso finalizado")
#### **5.2.4. Representación Gráfica de los Servicios**
print("\n\t\t5.2.4. Representación Gráfica de los Servicios")
print("\n\t\t\tProceso iniciado")
warnings.simplefilter(action='ignore', category=FutureWarning)
plt.figure(figsize=(12, 6))
sns.barplot(data=servicios_df.head(20), x='Frecuencia', y='Servicio', palette='crest')
plt.title(f'Servicios más comunes en los alojamientos de {ciudad}')
plt.xlabel('Número de alojamientos que lo ofrecen')
plt.ylabel('Servicio')
plt.tight_layout()
plt.savefig(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis de Servicios/Servicios - {ciudad}.png')
warnings.simplefilter(action='ignore', category=FutureWarning)
plt.close()
print("\n\t\t\tProceso finalizado")
#### **5.2.5. Cálculo del Número de Servicios por Alojamiento**
print("\n\t\t5.2.5. Cálculo del Número de Servicios por Alojamiento")
print("\n\t\t\tProceso iniciado")
df['Numero de Servicios'] = df['Servicios'].apply(lambda x: len(x.split('\n')) if isinstance(x, str) else 0)
print("\n\t\t\tProceso finalizado")
### **5.3. Análisis Geográfico**
print("\n\t5.3. Análisis Geográfico")
##### **5.3.1. Obtener las Coordenadas de Nuestra Ciudad**
print("\n\t\t5.3.1. Obtener las Coordenadas de Nuestra Ciudad")
print("\n\t\t\tProceso iniciado")
geolocator = Nominatim(user_agent="geoapiEjemplo")

location = geolocator.geocode(f"{ciudad}, {pais}")

latitud_ciudad = location.latitude
longitud_ciudad = location.longitude
print("\n\t\t\tProceso finalizado")
##### **5.3.2. Creación del Mapa**
print("\n\t\t5.3.2. Creación del Mapa")
print("\n\t\t\tProceso iniciado")
mapa = folium.Map(location=[latitud_ciudad, longitud_ciudad], zoom_start=13)

cluster = MarkerCluster().add_to(mapa) # Agrupador de marcadores
print("\n\t\t\tProceso finalizado")
##### **5.3.3. Añadir Elementos Clasificados al Mapa** 
print("\n\t\t5.3.3. Añadir Elementos Clasificados al Mapa")
print("\n\t\t\tProceso iniciado")
for _, row in df.iterrows():
    tooltip = f"Nombre: {row['Nombre']} <br> Precio total: {row['Precio Total']} € <br> Precio Total por Viajero: {row['Precio Total por Viajero']} € <br> Precio por Noche: {row['Precio por Noche']} € <br> Precio por Noche por Viajero: {row['Precio por Noche por Viajero']} €  <br> Número de Servicios: {row['Numero de Servicios']} <br><a href='{row['URL']}' target='_blank'>Ver alojamiento</a>"
    
    # Color según precio
    if row['Precio por Noche'] < 300:
        color = 'green'
    elif row['Precio por Noche'] < 600:
        color = 'orange'
    else:
        color = 'red'

    folium.CircleMarker(
        location=[row['Latitud'], row['Longitud']],
        radius=6,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(tooltip, max_width=300)
    ).add_to(cluster)
print("\n\t\t\tProceso finalizado")
## **6. Exportación de Datos**
print("\n6. Exportación de Datos")
### **6.1. Reordenación del Dataframe**
print("\n\t6.1. Reordenación del Dataframe")
print("\n\t\tProceso iniciado")
# Especificar el nuevo orden de las columnas
nuevo_orden = [
    'Nombre', 
    'Servicios', 'Numero de Servicios',
    'Precio Total', 'Máximo Precio Total', 'Mínimo Precio Total', 'Moda Precio Total', 
    'Precio Total por Viajero', 'Máximo Precio Total por Viajero', 'Mínimo Precio Total por Viajero', 'Moda Precio Total por Viajero', 
    'Precio por Noche', 'Máximo Precio por Noche', 'Mínimo Precio por Noche', 'Moda Precio por Noche', 
    'Precio por Noche por Viajero', 'Máximo Precio por Noche por Viajero', 'Mínimo Precio por Noche por Viajero', 'Moda Precio por Noche por Viajero', 
    'Latitud', 
    'Longitud', 
    'URL'
]

# Reordenar las columnas
df = df[nuevo_orden]
print("\n\t\tProceso finalizado")
### **6.2. Exportación del CSV**
print("\n\t6.2. Exportación del CSV")
print("\n\t\tProceso iniciado")
# Asegurarse de que el directorio exista
os.makedirs('output', exist_ok=True)

# Guardar el archivo
df.to_csv(
    f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis de Datos/Alojamientos. {ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}.csv',
    index=False,
    encoding='utf-8'
)
print("\n\t\tProceso finalizado")
### **6.3. Exportación del Fichero de Texto**
print("\n\t6.3. Exportación del Fichero de Texto")
print("\n\t\tProceso iniciado")
# Asegurarse de que el directorio exista
os.makedirs('output', exist_ok=True)

# Guardar el contenido en un archivo .txt
with open(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Económico/Medidas Descriptivas/Medidas Descriptivas - {ciudad}.txt', 'w', encoding='utf-8') as file:
    file.write("\n\n")
    file.write(medias)
    file.write("\n\n")
    file.write(medianas)
    file.write("\n\n")
    file.write(desviaciones_tipicas)
    file.write("\n\n")
print("\n\t\tProceso finalizado")
### **6.4. Exportación del Mapa Interactivo**
print("\n\t6.4. Exportación del Mapa Interactivo")
print("\n\t\tProceso iniciado")
mapa.save(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Geográfico/Mapa. {ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}.html')
print("\n\t\tProceso finalizado")
### **6.5. Copia del Fichero Input.txt**
print("\n\t6.5. Copia del Fichero Input.txt")
print("\n\t\tProceso iniciado")
ruta_input_origen = f'input/input.txt'
ruta_input_destino = f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Input.txt'

shutil.copy(
    ruta_input_origen,
    ruta_input_destino
)

nuevo_nombre = 'Datos Usados Realizar Búsqueda.txt'
os.rename(ruta_input_destino, nuevo_nombre)
print("\n\t\tProceso finalizado")
## **8. Finalización del Proyecto**
print("\n8. Finalización del Proyecto")
print("\nEl proceso ha terminado.")
contador_final = time.time()
tiempo_total = contador_final - contador_inicio

tiempo_total = np.ceil(tiempo_total)

minutos = int(tiempo_total // 60)
segundos = int(tiempo_total % 60)

tiempo = f"{minutos} minutos y {segundos} segundos"

print(f"El tiempo transcurrido del proyecto ha sido de: {tiempo}.")
print(f"\nLos resultados se han guardado en la carpeta 'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}'.")
print("\nGracias por usar el programa.")