"""
Escenario A - Análisis de Datos Climáticos
Autores: Emperador, Javier / Navas, Adalberto
Descripción: Carga datos climáticos desde un CSV y genera estadísticas y gráficos.

Estructuras utilizadas:
- Datos Complejos
- Funciones
- Estructuras Repetitivas
- Manejo de Errores
"""

import csv
import os
import matplotlib.pyplot as plt # Dependencia para generar Graficos


# ==========================================================
# CONSTANTES
# ==========================================================

RUTA_DATOS = "../datos/clima.csv"
RUTA_GRAFICO = "../resultados/grafico_temperatura.png"
RUTA_GRAFICO_PROMEDIOS = "../resultados/grafico_promedios.png"
RUTA_GRAFICO_PRECIPITACIONES = "../resultados/grafico_precipitaciones.png"

DATOS_EJEMPLO = [
    {"fecha": "2024-01-01", "temperatura_maxima": 32.0, "temperatura_minima": 18.5, "precipitacion": 12.0},
    {"fecha": "2024-01-02", "temperatura_maxima": 30.1, "temperatura_minima": 20.0, "precipitacion":  0.0},
    {"fecha": "2024-01-03", "temperatura_maxima": 25.3, "temperatura_minima": 15.8, "precipitacion": 20.5},
    {"fecha": "2024-01-04", "temperatura_maxima": 22.8, "temperatura_minima": 12.0, "precipitacion": 35.0},
    {"fecha": "2024-01-05", "temperatura_maxima": 27.0, "temperatura_minima": 16.5, "precipitacion":  5.5},
]

NOMBRES_MESES = {
    "01": "Enero",    "02": "Febrero",   "03": "Marzo",
    "04": "Abril",    "05": "Mayo",      "06": "Junio",
    "07": "Julio",    "08": "Agosto",    "09": "Septiembre",
    "10": "Octubre",  "11": "Noviembre", "12": "Diciembre",
}

MENU = """
=============================================
     ANÁLISIS DE DATOS CLIMÁTICOS
=============================================
  1. Cargar datos desde CSV
  2. Mostrar registros
  3. Mostrar estadísticas
  4. Generar estadisticas
  5. Salir
============================================="""


# ==========================================================
# LISTA GLOBAL - almacena los registros cargados del CSV
# ==========================================================

datos_climaticos = []


# ==========================================================
# VALIDACIONES
# ==========================================================


def validar_datos_cargados():
    """
    Verifica que haya registros cargados en memoria.
    Devuelve True si hay datos, False si no.
    Centraliza este chequeo para no repetirlo en cada función.
    """
    if len(datos_climaticos) == 0:
        print("No hay datos cargados. Seleccione la opción 1 primero.")
        return False
    return True


def validar_opcion_menu(opcion):
    """
    Verifica que la opción ingresada esté dentro del rango válido (1-5).
    Devuelve True si es válida, False si no.
    """
    if opcion < 1 or opcion > 5:
        print("Opción inválida. Ingrese un número entre 1 y 5.")
        return False
    return True


# ==========================================================
# UTILIDADES
# ==========================================================


def separador(signo, cantidad):
    """
    Genera una línea de separación repitiendo el signo
    la cantidad de veces indicada.
    Ejemplo: separador("=", 45) devuelve "============...="
    """
    return signo * cantidad


def construir_etiquetas_meses(fechas):
    """
    Recibe la lista de fechas en formato "YYYY-MM-DD" y devuelve:
    - etiquetas:  lista con el número de día de cada fecha (sin cero inicial)
    - inicio_mes: diccionario { índice: "NombreMes" } donde empieza cada mes
    """
    etiquetas  = []
    inicio_mes = {}
    mes_actual = None

    for i, fecha in enumerate(fechas):
        partes = fecha.split("-")
        mes = partes[1]
        dia = str(int(partes[2]))

        if mes != mes_actual:
            mes_actual = mes
            inicio_mes[i] = NOMBRES_MESES[mes]

        etiquetas.append(dia)

    return etiquetas, inicio_mes


def aplicar_formato_eje(ax, etiquetas, inicio_mes, indices):
    """
    Aplica etiquetas de días y líneas verticales con nombre de mes
    a un eje dado. Se reutiliza para ambos gráficos para no repetir lógica.
    """
    ax.set_xticks(indices)
    ax.set_xticklabels(etiquetas, fontsize=7)

    for idx, nombre_mes in inicio_mes.items():
        ax.axvline(x=idx, color="gray", linestyle="--", linewidth=0.8, alpha=0.7)
        ax.text(
            idx + 0.3, ax.get_ylim()[1],
            nombre_mes,
            fontsize=8, color="gray", va="top"
        )


# ==========================================================
# FUNCIONES
# ==========================================================


def crear_csv_ejemplo():
    """
    Crea las carpetas necesarias y el archivo CSV
    con registros de ejemplo si no existe.
    """
    os.makedirs("../datos", exist_ok=True)
    os.makedirs("../resultados", exist_ok=True)

    with open(RUTA_DATOS, "w", newline="", encoding="utf-8") as archivo:
        campos = ["fecha", "temperatura_maxima", "temperatura_minima", "precipitacion"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for registro in DATOS_EJEMPLO:
            escritor.writerow(registro)

    print("Archivo clima.csv creado con datos de ejemplo.")


def cargar_datos():
    """
    Intenta abrir el CSV desde ../datos/clima.csv.
    Si no existe, lo crea con datos de ejemplo antes de leerlo.
    Cada fila se carga como un diccionario dentro de datos_climaticos.
    El clear() evita duplicados si el usuario carga los datos más de una vez.
    """
    datos_climaticos.clear()

    try:
        if not os.path.exists(RUTA_DATOS):
            print("No se encontró clima.csv. Creando archivo con datos de ejemplo...")
            crear_csv_ejemplo()

        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                registro = {
                    "fecha": fila["fecha"],
                    "temperatura_maxima": float(fila["temperatura_maxima"]),
                    "temperatura_minima": float(fila["temperatura_minima"]),
                    "precipitacion": float(fila["precipitacion"]),
                }
                datos_climaticos.append(registro)

        print("Datos cargados correctamente. Registros:", len(datos_climaticos))

    except ValueError:
        print("Error: el archivo tiene datos inválidos en alguna columna numérica.")


def mostrar_datos():
    """
    Recorre datos_climaticos con un for y muestra cada registro.
    """
    if not validar_datos_cargados():
        return

    print("
REGISTROS CLIMÁTICOS")
    print(separador("-", 75))

    for registro in datos_climaticos:
        print(
            "Fecha:", registro["fecha"],
            "| Máx:", registro["temperatura_maxima"], "°C",
            "| Mín:", registro["temperatura_minima"], "°C",
            "| Precip:", registro["precipitacion"], "mm",
        )


def calcular_estadisticas():
    """
    Recorre la lista una sola vez y calcula todas las métricas globales:
    - Temperatura promedio del período: (suma de máximas + suma de mínimas) / (total * 2)
    - Temperatura máxima más alta del período
    - Temperatura mínima más baja del período
    - Promedio de precipitaciones

    Devuelve un diccionario con los resultados, o None si no hay datos.
    """
    if not validar_datos_cargados():
        return None

    suma_maximas = 0.0
    suma_minimas = 0.0
    suma_precip  = 0.0

    maxima_global = datos_climaticos[0]["temperatura_maxima"]
    minima_global = datos_climaticos[0]["temperatura_minima"]

    for registro in datos_climaticos:
        t_max  = registro["temperatura_maxima"]
        t_min  = registro["temperatura_minima"]
        precip = registro["precipitacion"]

        suma_maximas += t_max
        suma_minimas += t_min
        suma_precip  += precip

        if t_max > maxima_global:
            maxima_global = t_max

        if t_min < minima_global:
            minima_global = t_min

    total = len(datos_climaticos)

    return {
        "temp_promedio": round((suma_maximas + suma_minimas) / (total * 2), 2),
        "maxima_global": maxima_global,
        "minima_global": minima_global,
        "precip_promedio": round(suma_precip / total, 2),
    }


def mostrar_estadisticas():
    """
    Llama a calcular_estadisticas() y muestra los resultados por pantalla.
    La validación de datos la delega a calcular_estadisticas().
    """
    estadisticas = calcular_estadisticas()

    if estadisticas is None:
        return

    print("
ESTADÍSTICAS CLIMÁTICAS")
    print(separador("-", 45))
    print("Temperatura promedio:", estadisticas["temp_promedio"],   "°C")
    print("Temperatura máxima:", estadisticas["maxima_global"],   "°C")
    print("Temperatura mínima:", estadisticas["minima_global"],   "°C")
    print("Precipitación promedio:", estadisticas["precip_promedio"], "mm")


def calcular_precipitaciones_por_mes(fechas, precipitaciones):
    """
    Agrupa y suma las precipitaciones por mes.
    Devuelve dos listas paralelas: nombres de mes y sus totales.
    """
    totales_mes = {}

    for i, fecha in enumerate(fechas):
        mes = fecha.split("-")[1]
        nombre_mes = NOMBRES_MESES[mes]

        if nombre_mes not in totales_mes:
            totales_mes[nombre_mes] = 0.0

        totales_mes[nombre_mes] += precipitaciones[i]

    meses   = list(totales_mes.keys())
    totales = [round(totales_mes[m], 1) for m in meses]

    return meses, totales


def generar_grafico():
    """
    Genera tres gráficos y los guarda en ../resultados/:
    - grafico_temperatura.png:              evolución de máximas y mínimas diarias
    - grafico_promedios.png:         promedio diario con línea de promedio global
    - grafico_precipitaciones.png:            suma total de precipitaciones por mes
    """
    if not validar_datos_cargados():
        return

    fechas = []
    maximas = []
    minimas = []
    promedios = []
    precipitaciones = []

    for registro in datos_climaticos:
        fechas.append(registro["fecha"])
        maximas.append(registro["temperatura_maxima"])
        minimas.append(registro["temperatura_minima"])
        precipitaciones.append(registro["precipitacion"])

        promedio_dia = round((registro["temperatura_maxima"] + registro["temperatura_minima"]) / 2, 2)
        promedios.append(promedio_dia)

    indices = list(range(len(fechas)))
    etiquetas, inicio_mes = construir_etiquetas_meses(fechas)

    # ----- Gráfico 1: máximas y mínimas -----
    fig1, ax1 = plt.subplots(figsize=(14, 5))
    ax1.plot(indices, maximas, marker="o", markersize=3, color="tomato", label="Máxima")
    ax1.plot(indices, minimas, marker="o", markersize=3, color="steelblue", label="Mínima")
    ax1.set_title("Evolución de Temperaturas Máximas y Mínimas")
    ax1.set_xlabel("Día")
    ax1.set_ylabel("Temperatura (°C)")
    ax1.legend()
    ax1.grid(True, alpha=0.4)
    plt.tight_layout()
    aplicar_formato_eje(ax1, etiquetas, inicio_mes, indices)
    fig1.savefig(RUTA_GRAFICO)
    plt.show()
    print("Gráfico 1 guardado en:", RUTA_GRAFICO)

    # ----- Gráfico 2: promedio diario -----
    fig2, ax2 = plt.subplots(figsize=(14, 5))
    ax2.plot(indices, promedios, marker="s", markersize=3, color="mediumseagreen", label="Promedio diario")

    promedio_global = round(sum(promedios) / len(promedios), 2)
    ax2.axhline(y=promedio_global, color="gray", linestyle="--", label=f"Promedio global ({promedio_global} °C)")

    ax2.set_title("Promedio de Temperatura por Día")
    ax2.set_xlabel("Día")
    ax2.set_ylabel("Temperatura (°C)")
    ax2.legend()
    ax2.grid(True, alpha=0.4)
    plt.tight_layout()
    aplicar_formato_eje(ax2, etiquetas, inicio_mes, indices)
    fig2.savefig(RUTA_GRAFICO_PROMEDIOS)
    plt.show()
    print("Gráfico 2 guardado en:", RUTA_GRAFICO_PROMEDIOS)

    # ----- Gráfico 3: precipitaciones totales por mes -----
    meses, totales = calcular_precipitaciones_por_mes(fechas, precipitaciones)

    fig3, ax3 = plt.subplots(figsize=(7, 5))
    barras = ax3.bar(meses, totales, color="steelblue", width=0.5)

    for barra, total in zip(barras, totales):
        ax3.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 1.5,
            f"{total} mm",
            ha="center", va="bottom", fontsize=9
        )

    ax3.set_title("Precipitaciones Totales por Mes")
    ax3.set_xlabel("Mes")
    ax3.set_ylabel("Precipitación (mm)")
    ax3.grid(True, axis="y", alpha=0.4)
    plt.tight_layout()
    fig3.savefig(RUTA_GRAFICO_PRECIPITACIONES)
    plt.show()
    print("Gráfico 3 guardado en:", RUTA_GRAFICO_PRECIPITACIONES)


def mostrar_menu():
    """
    Imprime el menú principal.
    """
    print(MENU)


def menu_principal():
    """
    Bucle principal del programa. Usa while para mantenerse
    activo hasta que el usuario elija salir (opción 5).
    """
    opcion = 0

    while opcion != 5:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if not validar_opcion_menu(opcion):
                continue

            if opcion == 1:
                cargar_datos()
            elif opcion == 2:
                mostrar_datos()
            elif opcion == 3:
                mostrar_estadisticas()
            elif opcion == 4:
                generar_grafico()
            elif opcion == 5:
                print("
Saliendo del programa. ¡Hasta luego!")

        except ValueError:
            print("Error: ingrese un número entero.")


# ==========================================================
# PUNTO DE ENTRADA
# ==========================================================

menu_principal()