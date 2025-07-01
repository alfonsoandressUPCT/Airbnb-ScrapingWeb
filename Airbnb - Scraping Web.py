# %% [markdown]
# #### **© Alfonso Andrés Giménez Sánchez**. Todos los derechos reservados

# %% [markdown]
# # **AIRBNB - WEB SCRAPING. Proyecto de Ciencia de Datos**

# %% [markdown]
# ## **1. Implementación de Librerías y Paquetes**

# %% [markdown]
# ### **1.1. Web Scraping**

# %%
import requests
import undetected_chromedriver as uc

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# %% [markdown]
# ### **1.2. Análisis y Manipulación de Datos**

# %%
import pandas as pd
import numpy as np
import re

from datetime import datetime

# %% [markdown]
# ### **1.3. Geolocalización y Visualización en Mapas**

# %%
import folium

from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim

# %% [markdown]
# ### **1.4. Traducción**

# %%
from translate import Translator

# %% [markdown]
# ### **1.5. Visualización de Datos**

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ### **1.6 Ventana Gráfica**

# %%
import customtkinter as Ctk
import tkinter as Tk

from tkcalendar import Calendar, DateEntry
from datetime import datetime
from PIL import Image, ImageTk

# %% [markdown]
# ### **1.7. Otras Utilidades**

# %%
from collections import Counter

import warnings
import random
import time
import os
import ssl
import sys
import shutil

ssl._create_default_https_context = ssl._create_unverified_context

# %% [markdown]
# ## **2. Inicio del Programa**

# %% [markdown]
# ### **2.1 Función de Inicio de Programa**

# %%
def comenzar_programa():
    mostrar_mensaje("2.1 Inicio del Programa")
        
    # %% [markdown]
    # ### **2.2 Inicio del Contador**
    
    # %%
    mostrar_mensaje("2.2 Inicio del Contador")

    # %%
    global contador_inicio
    contador_inicio = time.time()

    # %% [markdown]
    # ## **3. Extracción de Datos**

    # %%
    mostrar_mensaje("3. Extracción de Datos")
        
    # %% [markdown]
    # ### **3.1. Apertura del Navegador en el Sitio Web**

    # %%
    mostrar_mensaje("3.1. Apertura del Navegador en el Sitio Web")

    # %%
    browser = uc.Chrome(headless=False)

    time.sleep(3)

    url = 'https://www.airbnb.es'

    browser.get(url)

    time.sleep(3)

    # %% [markdown]
    # ### **3.2. Eliminación de Mensaje de Cookies**

    # %%
    mostrar_mensaje("3.2. Eliminación de Mensaje de Cookies")

    # %%
    cockies_botton = browser.find_element(By.XPATH, "//button[contains(text(), 'Solo las necesarias')]")

    cockies_botton.click()

    time.sleep(0.5)

    # %% [markdown]
    # ### **3.3. Extracción del HTML**

    # %%
    mostrar_mensaje("3.3. Extracción del HTML")

    # %%
    html = browser.page_source

    soup = bs(html, 'lxml')

    # %% [markdown]
    # ### **3.4. Lectura de Datos desde el Fichero y Creación de Carpeta para Resultados**

    # %%
    mostrar_mensaje("3.4. Lectura de Datos")

    # %%
    pais = destination_frame_country.get()
    ciudad = destination_frame_city.get()

    numero_adultos = guests_adults_value_label.cget("text")
    numero_niños = guests_childs_value_label.cget("text")
    numero_bebes = guests_babys_value_label.cget("text")
    numero_mascotas = guests_pets_value_label.cget("text")

    fecha_entrada = fecha_entrada_entry.get()
    fecha_salida = fecha_salida_entry.get()

    fecha_entrada_objetivo = datetime.strptime(fecha_entrada, "%d/%m/%Y")
    fecha_salida_objetivo = datetime.strptime(fecha_salida, "%d/%m/%Y")

    fecha_entrada_lista = list(fecha_entrada_objetivo)

    dia_entrada = str(fecha_entrada[0:2])

    dia_entrada_nombre = fecha_entrada_objetivo.strftime("%A")

    mes_entrada = str(fecha_entrada[3:5])

    mes_entrada_nombre = fecha_entrada_objetivo.strftime("%B")

    año_entrada = str(fecha_entrada[6:10])

    if dia_entrada[0] == '0':
        dia_entrada = dia_entrada[1:]

    dia_salida = str(fecha_salida[0:2])

    dia_salida_nombre = fecha_salida_objetivo.strftime("%A")

    mes_salida = str(fecha_salida[3:5])

    mes_salida_nombre = fecha_salida_objetivo.strftime("%B")

    año_salida = str(fecha_salida[6:10])

    if dia_salida[0] == '0':
        dia_salida = dia_salida[1:]

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

    # %% [markdown]
    # ### **3.5. Selección del Destino del Viaje**

    # %%
    mostrar_mensaje("3.5. Selección del Destino del Viaje")

    # %%
    Destino = f"{ciudad}, {pais}"

    campo_destino = browser.find_element(By.ID, "bigsearch-query-location-input")
    campo_destino.send_keys(Destino)
    campo_destino.send_keys(Keys.ENTER)

    time.sleep(2)

    # %% [markdown]
    # ### **3.6. Selección de Fechas del Viaje**

    # %%
    mostrar_mensaje("3.6. Selección de Fechas del Viaje")

    # %%
    translator = Translator(to_lang="es", from_lang="en")

    mes_entrada_nombre_español = Translator(to_lang="es").translate(mes_entrada_nombre).lower()

    mes_año = f"{mes_entrada_nombre_español} {año_entrada}"

    mes_actual = browser.find_element(By.XPATH, '//h2[contains(@class, "h19aqaok")]').text

    while mes_actual != mes_año:
    
        boton_siguiente = browser.find_element(By.XPATH, '//button[@aria-label[contains(.,"cambiar al mes siguiente")]]').click()
        time.sleep(1)
        mes_actual = browser.find_element(By.XPATH, '//h2[contains(@class, "h19aqaok")]').text

    time.sleep(5)

    tarjeta_fecha_entrada = f"{dia_entrada}, {dia_entrada_nombre}, {mes_entrada_nombre} {año_entrada}. Disponible. Selecciona este día como fecha de llegada." # Texto único del atributo aria-label 

    date_button = browser.find_element(By.XPATH, f"//button[@aria-label='{tarjeta_fecha_entrada}']")
    date_button.click()

    time.sleep(3)

    tarjeta_fecha_salida = f"{dia_salida}, {dia_salida_nombre}, {mes_salida_nombre} {año_salida}. Disponible. Selecciona este día como fecha de salida." # Texto único del atributo aria-label 

    date_button = browser.find_element(By.XPATH, f"//button[@aria-label='{tarjeta_fecha_salida}']") 
    date_button.click()

    # %% [markdown]
    # ### **3.7. Selección de Viajeros del Viaje**

    # %%
    mostrar_mensaje("3.7. Selección de Viajeros del Viaje")

    # %%
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


    # %% [markdown]
    # ### **3.8. Realización de la Búsqueda de Ubicaciones para el Viaje**

    # %%
    mostrar_mensaje("3.8. Realización de la Búsqueda de Ubicaciones para el Viaje")

    # %%
    search_button = browser.find_element(By.XPATH, "//button[@data-testid='structured-search-input-search-button']")
    search_button.click()

    time.sleep(5)

    # %% [markdown]
    # ### **3.9. Extracción de Datos de los Alojamientos**

    # %%
    mostrar_mensaje("3.9. Extracción de Datos de los Alojamientos")

    # %%
    data = []


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

    # %% [markdown]
    # ### **3.10. Cierre del Navegador**

    # %%
    mostrar_mensaje("3.10. Cierre del Navegador")

    # %%
    browser.close()
    browser.quit()

    # %% [markdown]
    # ### **3.11. Creación de Dataframe con Datos Extraídos de cada Alojamiento**

    # %%
    mostrar_mensaje("3.11. Creación de Dataframe con Datos Extraídos de cada Alojamiento")

    # %%
    df = pd.DataFrame(data)

    # %% [markdown]
    # ## **4. Limpieza y Ordenación de Datos**

    # %%
    mostrar_mensaje("4. Limpieza y Ordenación de Datos")

    # %% [markdown]
    # ### **4.1. Cálculo de Precio por Viajero**

    # %%
    mostrar_mensaje("4.1. Cálculo de Precio por Viajero")

    # %%
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

    # %% [markdown]
    # ### **4.2. Eliminación de Filas No Disponibles**

    # %%
    mostrar_mensaje("4.2. Eliminación de Filas No Disponibles")

    # %%
    indices = df[df.eq("No Disponible").any(axis=1)].index.tolist()
    df = df.drop(indices)
    df = df.reset_index(drop=True)

    # %% [markdown]
    # ### **4.3. Formateo de Servicios con Viñetas**

    # %%
    mostrar_mensaje("4.3. Formateo de Servicios con Viñetas")

    # %%
    # Formatear los servicios con viñetas
    def formatear_servicios(servicios):
        if servicios and isinstance(servicios, str):
            return "\n".join([f"- {servicio.strip()}" for servicio in servicios.split(",") if servicio.strip()])
        return "No disponible"

    df['Servicios'] = df['Servicios'].apply(formatear_servicios)

    # %% [markdown]
    # ### **4.4. Aproximación y Redondeo de Precios**

    # %%
    mostrar_mensaje("4.4. Aproximación y Redondeo de Precios")

    # %%
    columnas_a_redondear = ['Precio por Noche por Viajero', 'Precio Total por Viajero']

    for columna in columnas_a_redondear:
        # Aseguramos que son numéricos
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        
        # Redondeamos hacia arriba y convertimos a enteros
        df[columna] = np.ceil(df[columna]).astype(float)

    # %% [markdown]
    # ### **4.5. Conversión de Datos Económicos a Datos Numéricos**

    # %%
    mostrar_mensaje("4.5. Conversión de Datos Económicos a Datos Numéricos")

    # %%
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

    # %% [markdown]
    # ### **4.6. Capitalización de Nombre de los Títulos**

    # %%
    mostrar_mensaje("4.6. Capitalización de Nombre de los Títulos")

    # %%
    df['Nombre'] = df['Nombre'].str.title()

    # %% [markdown]
    # ## **5. Interpretación de Datos**

    # %%
    mostrar_mensaje("5. Interpretación de Datos")

    # %% [markdown]
    # ### **5.1. Análisis Económico**

    # %%
    mostrar_mensaje("5.1. Análisis Económico")

    # %% [markdown]
    # #### **5.1.1. Medias de los Precios**

    # %%
    mostrar_mensaje("5.1.1. Medias de los Precios")

    # %%
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

    # %% [markdown]
    # #### **5.1.2. Medianas de los Precios**

    # %%
    mostrar_mensaje("5.1.2. Medianas de los Precios")

    # %%
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

    # %% [markdown]
    # #### **5.1.3. Desviaciones Estándar de los Precios**

    # %%
    mostrar_mensaje("5.1.3. Desviaciones Estándar de los Precios")

    # %%
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

    # %% [markdown]
    # #### **5.1.4. Modas de los Precios**

    # %%
    mostrar_mensaje("5.1.4. Modas de los Precios")

    # %%
    moda_precio_noche = df['Precio por Noche'].mode()[0]
    df['Moda Precio por Noche'] = df['Precio por Noche'].apply(lambda x: 'X' if x == moda_precio_noche else '')

    moda_precio_noche_viajero = df['Precio por Noche por Viajero'].mode()[0]
    df['Moda Precio por Noche por Viajero'] = df['Precio por Noche por Viajero'].apply(lambda x: 'X' if x == moda_precio_noche_viajero else '')

    moda_precio_total = df['Precio Total'].mode()[0]
    df['Moda Precio Total'] = df['Precio Total'].apply(lambda x: 'X' if x == moda_precio_total else '')

    moda_precio_total_viajero = df['Precio Total por Viajero'].mode()[0]
    df['Moda Precio Total por Viajero'] = df['Precio Total por Viajero'].apply(lambda x: 'X' if x == moda_precio_total_viajero else '')

    # %% [markdown]
    # #### **5.1.5. Precios Máximos**

    # %%
    mostrar_mensaje("5.1.5. Precios Máximos")

    # %%
    maximo_precio_noche = df['Precio por Noche'].max()
    df['Máximo Precio por Noche'] = df['Precio por Noche'].apply(lambda x: 'X' if x == maximo_precio_noche else '')

    maximo_precio_noche_viajero = df['Precio por Noche por Viajero'].max()
    df['Máximo Precio por Noche por Viajero'] = df['Precio por Noche por Viajero'].apply(lambda x: 'X' if x == maximo_precio_noche_viajero else '')

    maximo_precio_total = df['Precio Total'].max()
    df['Máximo Precio Total'] = df['Precio Total'].apply(lambda x: 'X' if x == maximo_precio_total else '')

    maximo_precio_total_viajero = df['Precio Total por Viajero'].max()
    df['Máximo Precio Total por Viajero'] = df['Precio Total por Viajero'].apply(lambda x: 'X' if x == maximo_precio_total_viajero else '')

    # %% [markdown]
    # #### **5.1.6. Precios Mínimos**

    # %%
    mostrar_mensaje("5.1.6. Precios Mínimos")

    # %%
    minimo_precio_noche = df['Precio por Noche'].min()
    df['Mínimo Precio por Noche'] = df['Precio por Noche'].apply(lambda x: 'X' if x == minimo_precio_noche else '')

    minimo_precio_noche_viajero = df['Precio por Noche por Viajero'].min()
    df['Mínimo Precio por Noche por Viajero'] = df['Precio por Noche por Viajero'].apply(lambda x: 'X' if x == minimo_precio_noche_viajero else '')

    minimo_precio_total = df['Precio Total'].min()
    df['Mínimo Precio Total'] = df['Precio Total'].apply(lambda x: 'X' if x == minimo_precio_total else '')

    minimo_precio_total_viajero = df['Precio Total por Viajero'].min()
    df['Mínimo Precio Total por Viajero'] = df['Precio Total por Viajero'].apply(lambda x: 'X' if x == minimo_precio_total_viajero else '')

    # %% [markdown]
    # #### **5.1.7. Representación Gráfica de Precios**

    # %%
    mostrar_mensaje("5.1.7. Representación Gráfica de Precios")

    # %% [markdown]
    # ##### **5.1.7.1. Histogramas**

    # %%
    mostrar_mensaje("5.1.7.1. Histogramas")

    # %%
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

    # %% [markdown]
    # ##### **5.1.7.2. Diagramas de Caja**

    # %%
    mostrar_mensaje("5.1.7.2. Diagramas de Caja")

    # %%
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

    # %% [markdown]
    # ### **5.2. Análisis de Servicios**

    # %%
    mostrar_mensaje("5.2. Análisis de Servicios")

    # %% [markdown]
    # #### **5.2.1. Extracción de los Servicios**

    # %%
    mostrar_mensaje("5.2.1. Extracción de los Servicios")

    # %%
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

    # %% [markdown]
    # #### **5.2.2. Contamos las Frecuencias de los Servicios**

    # %%
    mostrar_mensaje("5.2.2. Contamos las Frecuencias de los Servicios")

    # %%
    frecuencias_servicios = Counter(todos_los_servicios)

    # %% [markdown]
    # #### **5.2.3. Creación de un Dataframe de los Servicios**

    # %%
    mostrar_mensaje("5.2.3. Creación de un Dataframe de los Servicios")

    # %%
    servicios_df = pd.DataFrame(frecuencias_servicios.items(), columns=['Servicio', 'Frecuencia'])
    servicios_df = servicios_df.sort_values(by='Frecuencia', ascending=False)

    # %% [markdown]
    # #### **5.2.4. Representación Gráfica de los Servicios**

    # %%
    mostrar_mensaje("5.2.4. Representación Gráfica de los Servicios")

    # %%
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

    # %% [markdown]
    # #### **5.2.5. Cálculo del Número de Servicios por Alojamiento**

    # %%
    mostrar_mensaje("5.2.5. Cálculo del Número de Servicios por Alojamiento")

    # %%
    df['Numero de Servicios'] = df['Servicios'].apply(lambda x: len(x.split('\n')) if isinstance(x, str) else 0)

    # %% [markdown]
    # ### **5.3. Análisis Geográfico**

    # %%
    mostrar_mensaje("5.3. Análisis Geográfico")

    # %% [markdown]
    # ##### **5.3.1. Obtener las Coordenadas de Nuestra Ciudad**

    # %%
    mostrar_mensaje("5.3.1. Obtener las Coordenadas de Nuestra Ciudad")

    # %%
    geolocator = Nominatim(user_agent="geoapiEjemplo")

    location = geolocator.geocode(f"{ciudad}, {pais}")

    latitud_ciudad = location.latitude
    longitud_ciudad = location.longitude

    # %% [markdown]
    # ##### **5.3.2. Creación del Mapa**

    # %%
    mostrar_mensaje("5.3.2. Creación del Mapa")

    # %%
    mapa = folium.Map(location=[latitud_ciudad, longitud_ciudad], zoom_start=13)

    cluster = MarkerCluster().add_to(mapa) # Agrupador de marcadores

    # %% [markdown]
    # ##### **5.3.3. Añadir Elementos Clasificados al Mapa** 

    # %%
    mostrar_mensaje("5.3.3. Añadir Elementos Clasificados al Mapa")

    # %%
    for _, row in df.iterrows():
        tooltip = f"Nombre: {row['Nombre']} <br> Precio Total: {row['Precio Total']} € <br> Precio Total por Viajero: {row['Precio Total por Viajero']} € <br> Precio por Noche: {row['Precio por Noche']} € <br> Precio por Noche por Viajero: {row['Precio por Noche por Viajero']} €  <br> Número de Servicios: {row['Numero de Servicios']} <br><a href='{row['URL']}' target='_blank'>Ver alojamiento</a>"
        
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

    # %% [markdown]
    # ## **6. Exportación de Datos**

    # %%
    mostrar_mensaje("6. Exportación de Datos")

    # %% [markdown]
    # ### **6.1. Reordenación del Dataframe**

    # %%
    mostrar_mensaje("6.1. Reordenación del Dataframe")

    # %%
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

    # %% [markdown]
    # ### **6.2. Exportación del CSV**

    # %%
    mostrar_mensaje("6.2. Exportación del CSV")

    # %%
    # Asegurarse de que el directorio exista
    os.makedirs('output', exist_ok=True)

    # Guardar el archivo
    df.to_csv(
        f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis de Datos/Alojamientos. {ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}.csv',
        index=False,
        encoding='utf-8'
    )

    # %% [markdown]
    # ### **6.3. Exportación del Fichero de Texto**

    # %%
    mostrar_mensaje("6.3. Exportación del Fichero de Texto")

    # %%
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

    # %% [markdown]
    # ### **6.4. Exportación del Mapa Interactivo**

    # %%
    mostrar_mensaje("6.4. Exportación del Mapa Interactivo")

    # %%
    mapa.save(f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}/Análisis Geográfico/Mapa. {ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}.html')

    # %% [markdown]
    # ### **6.5. Copia del Fichero Input.txt**

    # %%
    mostrar_mensaje("6.5. Copia del Fichero Input.txt")

    # %%
    ruta_input_origen = f'input/input.txt'
    ruta_directorio_destino = f'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}'
    ruta_input_destino = os.path.join(ruta_directorio_destino, 'input.txt')

    # Copiar el archivo
    shutil.copy(ruta_input_origen, ruta_input_destino)

    # Renombrar el archivo dentro del mismo directorio
    nuevo_nombre = 'Datos Usados Realizar Búsqueda.txt'
    ruta_nuevo_nombre = os.path.join(ruta_directorio_destino, nuevo_nombre)

    os.rename(ruta_input_destino, ruta_nuevo_nombre)

    # %% [markdown]
    # ## **7. Finalización del Proyecto**

    # %%
    mostrar_mensaje("7. Finalización del Proyecto")

    # %%
    contador_final = time.time()
    tiempo_total = contador_final - contador_inicio

    tiempo_total = np.ceil(tiempo_total)

    minutos = int(tiempo_total // 60)
    segundos = int(tiempo_total % 60)

    tiempo = f"{minutos} minutos y {segundos} segundos"

    mostrar_contador_programa(f"El tiempo transcurrido de la búsqueda ha sido de: {tiempo}.")
    mostrar_mensaje_exportacion(f"Los resultados se han guardado en la carpeta 'output/{ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}'.")
    mostrar_mensaje("Gracias por usar el programa.")

# %% [markdown]
# ## **8. Ventana Gráfica**

# %% [markdown]
# ### **8.1 Creación y Configuración de la Ventana**

# %% [markdown]
# #### **8.1.1 Ventana Principal de la Aplicación**

# %%
app = Ctk.CTk()

# %% [markdown]
# #### **8.1.2 Configuración de la Aplicación**

# %%
Ctk.set_appearance_mode("system") 
app.title("Airbnb - Web Scraping")
app.geometry("1080x720")
app.resizable(False, False)
app.configure(bg="#000000")

# %% [markdown]
# #### **8.1.3 Icono de la Aplicación**

# %%
ruta = "icons/airbnb.png"
print("Directorio actual:", os.getcwd())
icon_image = Image.open("icons/airbnb.png")
icon_photo = ImageTk.PhotoImage(icon_image)
app.iconphoto(False, icon_photo)

# %% [markdown]
# ### **8.2 Input Frame**

# %% [markdown]
# #### **8.2.1 Creación del Input Frame**

# %%
input_frame = Ctk.CTkFrame(app, width=300, height=600, fg_color="#FF5A5F")
input_frame.place(x=0, y=0)

# %% [markdown]
# #### **8.2.2 Título del Input Frame**

# %%
input_label_title = Ctk.CTkLabel(input_frame, 
                                text="Parámetros de Búsqueda", 
                                font=("AirbnbCereal_W_Blk", 20, "bold"), 
                                text_color="#FFFFFF", width=300, height=70, anchor="center",
                                corner_radius=0, bg_color="#FF5A5F")
input_label_title.place(x=0, y=0)

# %% [markdown]
# #### **8.2.3 Frame de Destino**

# %% [markdown]
# ##### **8.2.3.1 Creación del Frame de Destino**

# %%
input_destination_frame = Ctk.CTkFrame(input_frame, width=300, height=120, fg_color="#FF5A5F")
input_destination_frame.place(x=0, y=70)

# %% [markdown]
# ##### **8.2.3.2 Título del Frame de Destino**

# %%
destination_label_title = Ctk.CTkLabel(input_destination_frame, 
                                text="Destino", 
                                font=("AirbnbCereal_W_Bk", 20, "bold"), 
                                text_color="#FFFFFF", width=245, height=50, anchor="w",
                                corner_radius=0, bg_color="#FF5A5F")
destination_label_title.place(x=30, y=0)

# %% [markdown]
# ##### **8.2.3.3 Entrada del País de Destino**

# %%
destination_frame_country = Ctk.CTkEntry(input_destination_frame,
                                                font=("AirbnbCereal_W_Bk",14),
                                                fg_color="#484848",
                                                text_color="#767676", width=225, height=25,
                                                placeholder_text="Pais")
destination_frame_country.place(x=55, y=50)

# %% [markdown]
# ##### **8.2.3.4 Entrada de la Ciudad de Destino**

# %%
destination_frame_city = Ctk.CTkEntry(input_destination_frame,
                                                font=("AirbnbCereal_W_Bk",14),
                                                fg_color="#484848",
                                                text_color="#767676", width=225, height=25,
                                                placeholder_text="Ciudad")
destination_frame_city.place(x=55, y=85)

# %% [markdown]
# #### **8.2.4 Frame de Huéspedes**

# %% [markdown]
# ##### **8.2.4.1 Creación del Frame de Huéspedes**

# %%
input_guest_frame = Ctk.CTkFrame(input_frame, width=300, height=200, fg_color="#FF5A5F")
input_guest_frame.place(x=0, y=200)

# %% [markdown]
# ##### **8.2.4.2 Título del Frame de Huéspedes**

# %%
guests_label_title = Ctk.CTkLabel(input_guest_frame, 
                                text="Huéspedes", 
                                font=("AirbnbCereal_W_Bk", 20, "bold"), 
                                text_color="#FFFFFF", width=245, height=50, anchor="w",
                                corner_radius=0, bg_color="#FF5A5F")
guests_label_title.place(x=30, y=0)

# %% [markdown]
# ##### **8.2.4.3 Frame de Adultos**

# %% [markdown]
# ###### **8.2.4.3.1 Creación del Frame de Adultos**

# %%
guests_adults_frame = Ctk.CTkFrame(input_guest_frame, width=300, height=25, fg_color="#FF5A5F")
guests_adults_frame.place(x=50, y=50)

# %% [markdown]
# ###### **8.2.4.3.2 Título del Frame de Adultos**

# %%
guests_adults_label_title = Ctk.CTkLabel(guests_adults_frame,
                                    text="Adultos",
                                    font=("AirbnbCereal_W_Bk", 14, "bold"),
                                    text_color="#FFFFFF", width=100, height=25, anchor="w",
                                    corner_radius=0, bg_color="#FF5A5F")
guests_adults_label_title.place(x=10, y=0)

# %% [markdown]
# ###### **8.2.4.3.3 Botones del Frame de Adultos**

# %%
guests_adults_value_label = Ctk.CTkLabel(guests_adults_frame,
                                        text="0",
                                        font=("AirbnbCereal_W_Bk", 14, "bold"),
                                        text_color="#FFFFFF", width=30, height=25, anchor="center",
                                        corner_radius=0, bg_color="#FF5A5F")
guests_adults_value_label.place(x=250, y=0)

adults_count = 0

def aumentar_adultos():
    global adults_count
    adults_count += 1
    guests_adults_value_label.configure(text=str(adults_count))

def reducir_adultos():
    global adults_count
    if adults_count > 0:
        adults_count -= 1
        guests_adults_value_label.configure(text=str(adults_count))

# Botón -
guests_adults_button_decrement = Ctk.CTkButton(
    guests_adults_frame,
    text="-",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=reducir_adultos
)
guests_adults_button_decrement.place(x=100, y=0)

# Valor actual
guests_adults_value_label = Ctk.CTkLabel(
    guests_adults_frame,
    text=str(adults_count),
    font=("AirbnbCereal_W_Bk", 14),
    width=30,
    text_color="#FFFFFF",
    fg_color="transparent"
)
guests_adults_value_label.place(x=135, y=0)

# Botón +
guests_adults_button_increment = Ctk.CTkButton(
    guests_adults_frame,
    text="+",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=aumentar_adultos
)
guests_adults_button_increment.place(x=170, y=0)

# %% [markdown]
# ##### **8.2.4.4 Frame de Niños**

# %% [markdown]
# ###### **8.2.4.4.1 Creación del Frame de Niños**

# %%
guests_childs_frame = Ctk.CTkFrame(input_guest_frame, width=300, height=25, fg_color="#FF5A5F")
guests_childs_frame.place(x=50, y=80)

# %% [markdown]
# ###### **8.2.4.4.2 Título del Frame de Niños**

# %%
guests_childs_label_title = Ctk.CTkLabel(guests_childs_frame,
                                    text="Niños",
                                    font=("AirbnbCereal_W_Bk", 14, "bold"),
                                    text_color="#FFFFFF", width=100, height=25, anchor="w",
                                    corner_radius=0, bg_color="#FF5A5F")
guests_childs_label_title.place(x=10, y=0)

# %% [markdown]
# ###### **8.2.4.4.3 Botones del Frame de Niños**

# %%
guests_childs_value_label = Ctk.CTkLabel(guests_childs_frame,
                                        text="0",
                                        font=("AirbnbCereal_W_Bk", 14, "bold"),
                                        text_color="#FFFFFF", width=30, height=25, anchor="center",
                                        corner_radius=0, bg_color="#FF5A5F")
guests_childs_value_label.place(x=250, y=0)

childs_count = 0

def aumentar_niños():
    global childs_count
    childs_count += 1
    guests_childs_value_label.configure(text=str(childs_count))

def reducir_niños():
    global childs_count
    if childs_count > 0:
        childs_count -= 1
        guests_childs_value_label.configure(text=str(childs_count))

# Botón -
guests_childs_button_decrement = Ctk.CTkButton(
    guests_childs_frame,
    text="-",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=reducir_niños
)
guests_childs_button_decrement.place(x=100, y=0)


# Valor actual
guests_childs_value_label = Ctk.CTkLabel(
    guests_childs_frame,
    text=str(childs_count),
    font=("AirbnbCereal_W_Bk", 14),
    width=30,
    text_color="#FFFFFF",
    fg_color="transparent"
)
guests_childs_value_label.place(x=135, y=0)


# Botón +
guests_childs_button_increment = Ctk.CTkButton(
    guests_childs_frame,
    text="+",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=aumentar_niños
)
guests_childs_button_increment.place(x=170, y=0)

# %% [markdown]
# ##### **8.2.4.5 Frame de Bebés**

# %% [markdown]
# ###### **8.2.4.5.1 Creación del Frame de Bebés**

# %%
guests_babys_frame = Ctk.CTkFrame(input_guest_frame, width=300, height=50, fg_color="#FF5A5F")
guests_babys_frame.place(x=50, y=110)

# %% [markdown]
# ###### **8.2.4.5.2 Título del Frame de Bebés**

# %%
guests_babys_label_title = Ctk.CTkLabel(guests_babys_frame,
                                    text="Bebés",
                                    font=("AirbnbCereal_W_Bk", 14, "bold"),
                                    text_color="#FFFFFF", width=100, height=25, anchor="w",
                                    corner_radius=0, bg_color="#FF5A5F")
guests_babys_label_title.place(x=10, y=0)

# %% [markdown]
# ###### **8.2.4.5.3 Botones del Frame de Bebés**

# %%
guests_babys_value_label = Ctk.CTkLabel(guests_babys_frame,
                                        text="0",
                                        font=("AirbnbCereal_W_Bk", 14, "bold"),
                                        text_color="#FFFFFF", width=30, height=25, anchor="center",
                                        corner_radius=0, bg_color="#FF5A5F")
guests_babys_value_label.place(x=250, y=0)

babys_count = 0

def aumentar_bebes():
    global babys_count
    babys_count += 1
    guests_babys_value_label.configure(text=str(babys_count))

def reducir_bebes():
    global babys_count
    if babys_count > 0:
        babys_count -= 1
        guests_babys_value_label.configure(text=str(babys_count))

# Botón -
guests_babys_button_decrement = Ctk.CTkButton(
    guests_babys_frame,
    text="-",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=reducir_bebes
)
guests_babys_button_decrement.place(x=100, y=0)


# Valor actual
guests_babys_value_label = Ctk.CTkLabel(
    guests_babys_frame,
    text=str(babys_count),
    font=("AirbnbCereal_W_Bk", 14),
    width=30,
    text_color="#FFFFFF",
    fg_color="transparent"
)
guests_babys_value_label.place(x=135, y=0)


# Botón +
guests_babys_button_increment = Ctk.CTkButton(
    guests_babys_frame,
    text="+",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=aumentar_bebes
)
guests_babys_button_increment.place(x=170, y=0)

# %% [markdown]
# ##### **8.2.4.6 Frame de Mascotas**

# %% [markdown]
# ###### **8.2.4.6.1 Creación del Frame de Mascotas**

# %%
guests_pets_frame = Ctk.CTkFrame(input_guest_frame, width=300, height=50, fg_color="#FF5A5F")
guests_pets_frame.place(x=50, y=140)

# %% [markdown]
# ###### **8.2.4.6.2 Título del Frame de Mascotas**

# %%
guests_pets_label_title = Ctk.CTkLabel(guests_pets_frame,
                                    text="Mascotas",
                                    font=("AirbnbCereal_W_Bk", 14, "bold"),
                                    text_color="#FFFFFF", width=100, height=25, anchor="w",
                                    corner_radius=0, bg_color="#FF5A5F")
guests_pets_label_title.place(x=10, y=0)

# %% [markdown]
# ###### **8.2.4.6.3 Botones del Frame de Mascotas**

# %%
guests_pets_value_label = Ctk.CTkLabel(guests_pets_frame,
                                        text="0",
                                        font=("AirbnbCereal_W_Bk", 14, "bold"),
                                        text_color="#FFFFFF", width=30, height=25, anchor="center",
                                        corner_radius=0, bg_color="#FF5A5F")
guests_pets_value_label.place(x=250, y=0)

pets_count = 0

def aumentar_mascotas():
    global pets_count
    pets_count += 1
    guests_pets_value_label.configure(text=str(pets_count))

def reducir_mascotas():
    global pets_count
    if pets_count > 0:
        pets_count -= 1
        guests_pets_value_label.configure(text=str(pets_count))

# Botón -
guests_pets_button_decrement = Ctk.CTkButton(
    guests_pets_frame,
    text="-",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=reducir_mascotas
)
guests_pets_button_decrement.place(x=100, y=0)


# Valor actual
guests_pets_value_label = Ctk.CTkLabel(
    guests_pets_frame,
    text=str(pets_count),
    font=("AirbnbCereal_W_Bk", 14),
    width=30,
    text_color="#FFFFFF",
    fg_color="transparent"
)
guests_pets_value_label.place(x=135, y=0)


# Botón +
guests_pets_button_increment = Ctk.CTkButton(
    guests_pets_frame,
    text="+",
    font=("AirbnbCereal_W_Bk", 14, "bold"),
    text_color="#FFFFFF",
    width=30,
    height=25,
    corner_radius=5,
    fg_color="#484848",
    command=aumentar_mascotas
)
guests_pets_button_increment.place(x=170, y=0)

# %% [markdown]
# #### **8.2.5 Frame de Calendario**

# %% [markdown]
# ##### **8.2.5.1 Creación del Frame de Calendario**

# %%
calendar_frame = Tk.Frame(input_frame, width=300, height=600, bg="#FF5A5F")
calendar_frame.place(x=0, y=370)

# %% [markdown]
# ##### **8.2.5.2 Título del Frame de Calendario**

# %%
calendar_label_title = Ctk.CTkLabel(calendar_frame,
                                text="Fechas",
                                font=("AirbnbCereal_W_Bk", 20, "bold"),
                                text_color="#FFFFFF", width=300, height=50, anchor="w",
                                corner_radius=0, bg_color="#FF5A5F")
calendar_label_title.place(x=30, y=10)

# %% [markdown]
# ##### **8.2.5.3 Botones y Entrada de Fechas del Calendario**

# %%
# Variables para almacenar ventanas emergentes (top-level)
top_calendar_entry = None
top_calendar_exit = None

### === FECHA DE ENTRADA ===
fecha_entrada_entry = Ctk.CTkEntry(calendar_frame, placeholder_text="Fecha de entrada", width=120, fg_color="#484848", text_color="#767676")
fecha_entrada_entry.place(x=50, y=80)

def mostrar_calendario_entrada():
    global top_calendar_entry

    if top_calendar_entry and top_calendar_entry.winfo_exists():
        return  # ya está abierto

    top_calendar_entry = Tk.Toplevel(calendar_frame)
    top_calendar_entry.geometry("+{}+{}".format(app.winfo_rootx() + 100, app.winfo_rooty() + 300))
    top_calendar_entry.overrideredirect(True)

    cal = Calendar(
        top_calendar_entry,
        selectmode='day',
        date_pattern='dd/mm/y',
        background="#FF5A5F",
        foreground="#FFFFFF",
        headersbackground="#FF5A5F",
        headersforeground="#FFFFFF",
        selectbackground="#FFFFFF",
        selectforeground="#FF5A5F"
    )
    cal.pack()

    cal.bind("<<CalendarSelected>>", lambda e: seleccionar_fecha(cal, fecha_entrada_entry, top_calendar_entry))

btn_fecha_entrada = Ctk.CTkButton(calendar_frame, text="📅", width=40, command=mostrar_calendario_entrada, fg_color="#484848", text_color="#767676")
btn_fecha_entrada.place(x=180, y=80)

### === FECHA DE SALIDA ===
fecha_salida_entry = Ctk.CTkEntry(calendar_frame, placeholder_text="Fecha de salida", width=120, fg_color="#484848", text_color="#767676")
fecha_salida_entry.place(x=50, y=130)

def mostrar_calendario_salida():
    global top_calendar_exit

    if top_calendar_exit and top_calendar_exit.winfo_exists():
        return

    top_calendar_exit = Tk.Toplevel(calendar_frame)
    top_calendar_exit.geometry("+{}+{}".format(app.winfo_rootx() + 100, app.winfo_rooty() + 370))
    top_calendar_exit.overrideredirect(True)

    cal = Calendar(
        top_calendar_exit,
        selectmode='day',
        date_pattern='dd/mm/y',
        background="#FF5A5F",
        foreground="#FFFFFF",
        headersbackground="#FF5A5F",
        headersforeground="#FFFFFF",
        selectbackground="#FFFFFF",
        selectforeground="#FF5A5F"
    )
    cal.pack()

    cal.bind("<<CalendarSelected>>", lambda e: seleccionar_fecha(cal, fecha_salida_entry, top_calendar_exit))

btn_fecha_salida = Ctk.CTkButton(calendar_frame, text="📅", width=40, command=mostrar_calendario_salida, fg_color="#484848", text_color="#767676")
btn_fecha_salida.place(x=180, y=130)

### === FUNCIÓN COMÚN PARA AMBOS ===
def seleccionar_fecha(calendario, campo_entry, ventana_top):
    fecha = calendario.get_date()
    campo_entry.delete(0, Ctk.END)
    campo_entry.insert(0, fecha)
    ventana_top.destroy()

# %% [markdown]
# ### **8.3 Start Frame**

# %% [markdown]
# #### **8.3.1 Creación del Start Frame**

# %%
start_frame = Ctk.CTkFrame(app, width=300, height=140, fg_color="#00a699")
start_frame.place(x=0, y=580)

# %% [markdown]
# #### **8.3.2 Título del Start Frame**

# %%
start_label_title = Ctk.CTkLabel(start_frame, 
                                text="",
                                width=300, height=70, anchor="center",
                                corner_radius=0, bg_color="#00a699")
start_label_title.place(x=0, y=0)

# %% [markdown]
# #### **8.3.3 Botón del Start Frame**

# %%
start_button = Ctk.CTkButton(start_frame,
                            text="Iniciar Búsqueda",
                            font=("AirbnbCereal_W_Blk", 20, "bold"),
                            text_color="#FFFFFF",
                            width=150, height=40,
                            border_color="#FFFFFF",
                            border_width=2,
                            corner_radius=0,
                            fg_color="#00a699",
                            command=comenzar_programa())  # Placeholder command
start_button.place(x=65, y=50)

# %% [markdown]
# ### **8.4 Process Frame**

# %% [markdown]
# #### **8.4.1 Creación del Process Frame**

# %%
process_frame = Ctk.CTkFrame(app, width=780, height=140, fg_color="#e2dece")
process_frame.place(x=300, y=580)

# %% [markdown]
# #### **8.4.2 Título del Process Frame**

# %%
def mostrar_contador_programa(mensaje):
    process_label_time.configure(text=mensaje)

process_label_time = Ctk.CTkLabel(process_frame, 
                                text="",
                                width=780, height=50, anchor="center",
                                corner_radius=0, bg_color="#e2dece")
process_label_time.place(x=0, y=0)

# %% [markdown]
# #### **8.4.3 Mostrar Texto a través de un Label**

# %%
process_label_mensage = Ctk.CTkLabel(process_frame,
                                text="",
                                font=("AirbnbCereal_W_Blk", 16, "bold"),
                                text_color="#000000", width=780, height=70, anchor="center",
                                corner_radius=0, bg_color="#e2dece")
process_label_mensage.place(x=0, y=50)

# Función para mostrar un nuevo mensaje (borra el anterior)
def mostrar_mensaje(nuevo_texto):
    process_label_mensage.configure(text=nuevo_texto)

# %% [markdown]
# ### **8.5 Output Frame**

# %% [markdown]
# #### **8.5.1 Creación del Output Frame**

# %%
output_frame = Ctk.CTkFrame(app, width=780, height=580, fg_color="#484848", corner_radius=0)
output_frame.place(x=300, y=0)

# %% [markdown]
# #### **8.5.2 Título del Output Frame**

# %%
output_label_title = Ctk.CTkLabel(output_frame, 
                                text="Resultados de la Búsqueda",
                                text_color="#FFFFFF",
                                font=("AirbnbCereal_W_Blk", 20, "bold"),
                                width=780, height=70, anchor="center",
                                corner_radius=0, bg_color="#484848")
output_label_title.place(x=0, y=0)

#%% [markdown]
#### **8.5.3 Mensaje de Exportación de la Búsqueda a través de un Label**

# %%
def mostrar_mensaje_exportacion(mensaje):
    message_output_label.configure(text=mensaje)

message_output_label = Ctk.CTkLabel(output_frame,
                                text="",
                                font=("AirbnbCereal_W_Blk", 16, "bold"),
                                text_color="#FFFFFF", width=780, height=70, anchor="center",
                                corner_radius=0, bg_color="#484848")
message_output_label.place(x=0, y=510)


# %% [markdown]
# ### **8.6 Ejecución de la Ventana Gráfica**

# %%
app.mainloop()


