#### **© Alfonso Andrés Giménez Sánchez**. Todos los derechos reservados
# **Web - Scraping. AIRBNB**
## **Implementación de Librerías y Paquetes**
import requests
from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import numpy as np
import os
import re
from datetime import datetime
from translate import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
## **Inicio del Proyecto**
print("\nBienvenido a Scraping-Web de Airbnb")
print("Comenzamos con el proyecto\n")
contador_inicio = time.time()
print("En proceso...")
## **Apertura del Navegador en el Sitio Web**
browser = uc.Chrome(headless=False)

time.sleep(3)

url = 'https://www.airbnb.es'

browser.get(url)

time.sleep(2)
## **Eliminación de Mensaje de Cookies**
cockies_botton = browser.find_element(By.XPATH, "//button[contains(text(), 'Solo las necesarias')]")

cockies_botton.click()

time.sleep(0.5)
## **Extracción del HTML**
html = browser.page_source

soup = bs(html, 'lxml')
## **Lectura de Datos desde el Fichero**
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

variables = cargar_variables('input/input_ejemplo.txt')

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
## **Selección del Destino del Viaje**
Destino = f"{ciudad}, {pais}"

campo_destino = browser.find_element(By.ID, "bigsearch-query-location-input")
campo_destino.send_keys(Destino)
campo_destino.send_keys(Keys.ENTER)

time.sleep(2)
## **Selección de Fechas del Viaje**
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
## **Selección de Viajeros del Viaje**
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
## **Realización de la Búsqueda de Ubicaciones para el Viaje**
search_button = browser.find_element(By.XPATH, "//button[@data-testid='structured-search-input-search-button']")
search_button.click()

time.sleep(5)
## **Obtención de Links de los Alojamientos en una Página**
data = []

links = list()

alojamientos = browser.find_elements(By.XPATH, "//div[@itemprop='itemListElement']")

for url in alojamientos:
    try:
        url = url.find_element(By.XPATH, ".//meta[@itemprop='url']").get_attribute("content")
        links.append(url)
    except Exception as e:
        print("Error en una tarjeta:", e)
        continue
## **Extracción de Datos de los Alojamientos de una Página**
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
        'Precio por noche': precio_noche,
        'Precio total': precio_total,
        'Servicios': servicios,
        'Latitud': latitud,
        'Longitud': longitud,
        'URL': url
    })
## **Cierre del Navegador**
browser.close()
browser.quit()
## **Creación de Dataframe con Datos Extraídos de cada Alojamiento**
df = pd.DataFrame(data)
## **Cálculo de Precio por Viajero**
# Limpiar el precio y convertirlo a float
def extraer_precio(precio_str):
    if isinstance(precio_str, str) and '€' in precio_str:
        try:
            numero = precio_str.split(' ')[0].replace('.', '').replace(',', '.')
            return float(numero)
        except ValueError:
            return None
    return None

df['Precio por noche por viajero'] = df['Precio por noche'].apply(lambda x: extraer_precio(x) / numero_adultos if extraer_precio(x) is not None else "No Disponible")

df['Precio total por viajero'] = df['Precio total'].apply(lambda x: extraer_precio(x) / numero_adultos if extraer_precio(x) is not None else "No Disponible")
                                                          
df = df[['Nombre', 'Precio por noche', 'Precio por noche por viajero', 'Precio total', 'Precio total por viajero', 'Latitud', 'Longitud', 'Servicios', 'URL']]
## **Limpieza y Ordenación de Datos**
### **Eliminación de Filas No Disponibles**
indices = df[df.eq("No Disponible").any(axis=1)].index.tolist()
df = df.drop(indices)
df = df.reset_index(drop=True)
### **Formateo de Servicios con Viñetas**
# Formatear los servicios con viñetas
def formatear_servicios(servicios):
    if servicios and isinstance(servicios, str):
        return "\n".join([f"- {servicio.strip()}" for servicio in servicios.split(",") if servicio.strip()])
    return "No disponible"

df['Servicios'] = df['Servicios'].apply(formatear_servicios)
### **Aproximación y Redondeo de Precios**
columnas_a_redondear = ['Precio por noche por viajero', 'Precio total por viajero']

for columna in columnas_a_redondear:
    # Aseguramos que son numéricos
    df[columna] = pd.to_numeric(df[columna], errors='coerce')
    
    # Redondeamos hacia arriba y convertimos a enteros
    df[columna] = np.ceil(df[columna]).astype(float)
### **Conversión de Datos Económicos a Datos Numéricos**
# Función para limpiar y convertir los precios a float
def convertir_a_entero(precio):
    if isinstance(precio, str):
        return int(precio.replace("€", "").replace(".", "").replace(",", ".").strip())
    return precio

# Aplicar la función a las columnas correspondientes
df["Precio por noche"] = df["Precio por noche"].apply(convertir_a_entero)
df["Precio total"] = df["Precio total"].apply(convertir_a_entero)
df["Precio por noche por viajero"] = pd.to_numeric(df["Precio por noche por viajero"]).astype(int)
df["Precio total por viajero"] = pd.to_numeric(df["Precio total por viajero"]).astype(int)
## **Exportación de Datos a un CSV**
# Asegurarse de que el directorio exista
os.makedirs('output', exist_ok=True)

# Limpiar la fecha para evitar errores con '/'
fecha_entrada_str = fecha_entrada.replace('/', '-')
fecha_salida_str = fecha_salida.replace('/', '-')
numero_total_personas = numero_adultos + numero_niños + numero_bebes + numero_mascotas

# Guardar el archivo
df.to_csv(
    f'output/Alojamientos. {ciudad}. {numero_total_personas} Personas. {fecha_entrada_str} | {fecha_salida_str}.csv',
    index=False,
    encoding='utf-8'
)
## **Finalización del Proyecto**
print("\nEl proceso ha terminado.")
contador_final = time.time()
tiempo_total = contador_final - contador_inicio

tiempo_total = np.ceil(tiempo_total)

minutos = int(tiempo_total // 60)
segundos = int(tiempo_total % 60)

tiempo = f"{minutos} minutos y {segundos} segundos"

print(f"El tiempo transcurrido del proyecto ha sido de: {tiempo}.")
print("El archivo CSV se ha guardado en la carpeta 'output'.")
print("\nGracias por usar el programa.")