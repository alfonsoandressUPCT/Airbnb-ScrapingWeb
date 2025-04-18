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
from datetime import datetime
from translate import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
## **Apertura del Navegador en el Sitio Web**
browser = uc.Chrome()

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

soup
## **Selección del Datos del Viaje**
print("\n-----Bienvenido a la web scraping de Airbnb-----")

print("\n\t Introduce el país donde desea viajar")
pais = input('\t\nPaís: ').capitalize()

print("\n\t Introduce la ciudad donde desea viajar")
ciudad = input("\t\nCiudad: ").capitalize()

meses = {
    "01": "Enero", 
    "02": "Febrero", 
    "03": "Marzo", 
    "04": "Abril",
    "05": "Mayo", 
    "06": "Junio", 
    "07": "Julio", 
    "08": "Agosto",
    "09": "Septiembre", 
    "10": "Octubre", 
    "11": "Noviembre", 
    "12": "Diciembre"
}

def definir_fechas():
    while True:
        try:
            fecha_entrada_in = input("\n\t Introduce la fecha de entrada (dd/mm/aaaa): ")
            dia_entrada_semana = str(input("\n\t¿Qué día de la semana es? (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): "))
            entrada = datetime.strptime(fecha_entrada_in, "%d/%m/%Y")
            fecha_entrada = fecha_entrada_in.split("/")

            dia_entrada = str(fecha_entrada[0])
            mes_entrada = str(fecha_entrada[1])
            mes_entrada_nombre = meses[mes_entrada].lower()
            año_entrada = str(fecha_entrada[2])

            fecha_salida_in = input("\n\t Introduce la fecha de salida (dd/mm/aaaa): ")
            dia_salida_semana = str(input("\n\t¿Qué día de la semana es? (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): "))
            salida = datetime.strptime(fecha_salida_in, "%d/%m/%Y")
            fecha_salida = fecha_salida_in.split("/")

            dia_salida = str(fecha_salida[0])
            mes_salida = fecha_salida[1]
            mes_salida_nombre = meses[mes_salida].lower()
            año_salida = str(fecha_salida[2])

            if salida <= entrada:
                print("❌ La fecha de salida no puede ser anterior o igual a la de entrada. Inténtalo de nuevo.")
            else:
                return fecha_entrada_in, fecha_salida_in, dia_entrada, dia_entrada_semana, mes_entrada, mes_entrada_nombre, año_entrada, dia_salida, dia_salida_semana, mes_salida, mes_salida_nombre, año_salida
        except ValueError:
            print("❌ Formato de fecha inválido. Usa el formato dd/mm/aaaa.")

fecha_entrada, fecha_salida, dia_entrada, dia_entrada_semana, mes_entrada, mes_entrada_nombre, año_entrada, dia_salida, dia_salida_semana, mes_salida, mes_salida_nombre, año_salida = definir_fechas()

print("\n\t Introduce el número de adultos")
numero_adultos = int(input("\n\tAdultos: "))

print("\n\t Introduce el número de niños")
numero_niños = int(input("\t\nNiños: "))

print("\n\t Introduce el número de bebés")
numero_bebes = int(input("\t\nBebés: "))

print("\n\t Introduce el número de mascotas")
numero_mascotas = int(input("\t\nMascotas: "))

time.sleep(5)
## **Selección del Destino del Viaje**
Destino = f"{ciudad}, {pais}"

campo_destino = browser.find_element(By.ID, "bigsearch-query-location-input")
campo_destino.send_keys(Destino)
campo_destino.send_keys(Keys.ENTER)

time.sleep(5)
## **Selección de Fechas del Viaje**
translator = Translator(to_lang="en", from_lang="es")

mes_año = f"{mes_entrada_nombre} {año_entrada}"

mes_actual = browser.find_element(By.XPATH, '//h2[contains(@class, "h19aqaok")]').text

while mes_actual != mes_año:
   
    boton_siguiente = browser.find_element(By.XPATH, '//button[@aria-label[contains(.,"cambiar al mes siguiente")]]').click()
    time.sleep(1)
    mes_actual = browser.find_element(By.XPATH, '//h2[contains(@class, "h19aqaok")]').text

time.sleep(3)

dia_entrada_semana_traducido = translator.translate(dia_entrada_semana)
mes_entrada_traducido = translator.translate(mes_entrada_nombre)

tarjeta_fecha = f"{dia_entrada}, {dia_entrada_semana_traducido}, {mes_entrada_traducido} {año_entrada}. Disponible. Selecciona este día como fecha de llegada." # Texto único del atributo aria-label 

date_button = browser.find_element(By.XPATH, f"//button[@aria-label='{tarjeta_fecha}']") 
date_button.click()

time.sleep(3)

dia_salida_semana_traducido = translator.translate(dia_salida_semana)
mes_salida_traducido = translator.translate(mes_salida_nombre)

tarjeta_fecha = f"{dia_salida}, {dia_salida_semana_traducido}, {mes_salida_traducido} {año_salida}. Disponible. Selecciona este día como fecha de salida." # Texto único del atributo aria-label 

date_button = browser.find_element(By.XPATH, f"//button[@aria-label='{tarjeta_fecha}']") 
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
    time.sleep(3)

    try:
        # Cierra el botón del traductor si aparece
        traductor_botton = browser.find_element(By.XPATH, "//button[@aria-label='Cerrar']")
        traductor_botton.click()
    except:
        pass  # Si no aparece, continúa

    time.sleep(1)

    try:
        nombre = browser.find_element(By.XPATH, "//h1[contains(@class, 'hpipapi')]").text
    except:
        nombre = url.find_element(By.XPATH, ".//meta[@itemprop='name']").get_attribute("content")

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

    time.sleep(1)

    data.append({
        'Nombre': nombre,
        'Precio por noche': precio_noche,
        'Precio total': precio_total,
        'Servicios': servicios,
        'URL': url
    })
## **Creación de Dataframe con Datos Extraídos de cada Alojamiento**
# Convertir el diccionario 'data' a un DataFrame
df = pd.DataFrame(data)

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
                                                          
df = df[['Nombre', 'Precio por noche', 'Precio por noche por viajero', 'Precio total', 'Precio total por viajero', 'Servicios', 'URL']]

# Formatear los servicios con viñetas
def formatear_servicios(servicios):
    if servicios and isinstance(servicios, str):
        return "\n".join([f"- {servicio.strip()}" for servicio in servicios.split(",") if servicio.strip()])
    return "No disponible"

df['Servicios'] = df['Servicios'].apply(formatear_servicios)
## **Exportación de Datos a un CSV**
# Asegurarse de que el directorio exista
os.makedirs('output', exist_ok=True)

# Limpiar la fecha para evitar errores con '/'
fecha_entrada_str = fecha_entrada.replace('/', '-')
fecha_salida_str = fecha_salida.replace('/', '-')

# Guardar el archivo
df.to_csv(
    f'output/Alojamientos. {ciudad}. {fecha_entrada_str} - {fecha_salida_str}.csv',
    index=False,
    encoding='utf-8'
)
## **Finalización del Proyecto y Cierre del Navegador**
browser.close()
browser.quit()