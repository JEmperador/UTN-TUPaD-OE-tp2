# UTN-TUPaD-OE-tp2

Análisis de datos climáticos de Rosario, Argentina (enero–marzo 2024).  
Trabajo Práctico N°2 — Organización Empresarial — TUP UTN

---

## Integrantes

| Nombre            |
| ----------------- |
| Emperador, Javier |
| Navas, Adalberto  |

## Enlaces

| Recurso               | Link                                                                                                |
| --------------------- | --------------------------------------------------------------------------------------------------- |
| Tablero Jira          | [Ver proyecto en Jira](https://jemperador.atlassian.net/jira/software/projects/PROYECTOOE/boards/1) |
| Informe Final         | [Ver PDF](https://drive.google.com/file/d/1cK-50aQ6f5KmK7FZSsG-SzG396YMk_Sf/view?usp=sharing)                                                                                         |
| Evidencia del proceso | [Ver capturas](./capturas)                                                                          |

---

## Requisitos

- Python 3.x
- matplotlib

```bash
pip install matplotlib
```

---

## Estructura del repositorio

```
UTN-TUPaD-OE-tp2/
├── capturas/
│   └── GitHub/                 # Acciones relacionadas a GitHub
│   └── Jira/                   # Acciones relacionadas a Jira
│       └── PROYECTOOE-5/            # Acciones realizadas para la tarjeta PROYECTOOE-5 (relacionada a P1)
│       └── PROYECTOOE-6/            # Acciones realizadas para la tarjeta PROYECTOOE-6 (relacionada a P2)
│       └── PROYECTOOE-7/            # Acciones realizadas para la tarjeta PROYECTOOE-7 (relacionada a P3)
│
├── datos/
│   └── clima.csv               # Dataset con registros diarios de temperatura y precipitaciones
│
├── scripts/
│   └── analisis_datos.py       # Script principal
│
├── resultados/
│   ├── grafico_temperatura.png      # Evolución de máximas y mínimas diarias
│   ├── grafico_promedios.png        # Promedio diario con línea de promedio global
│   └── grafico_precipitaciones.png  # Precipitaciones totales por mes
│
├── README.md
└── .gitignore
```

---

## Cómo ejecutar

El script debe correrse desde dentro de la carpeta `scripts/`:

```bash
cd scripts
python3 escenario_a_datos_climatico.py
```

> Si `datos/clima.csv` no existe, el programa lo genera automáticamente con datos de ejemplo.

---

## Dataset

El archivo `datos/clima.csv` contiene registros diarios con las columnas:

| Columna              | Tipo   | Descripción                          |
| -------------------- | ------ | ------------------------------------ |
| `fecha`              | string | Formato YYYY-MM-DD                   |
| `temperatura_maxima` | float  | Temperatura máxima del día (°C)      |
| `temperatura_minima` | float  | Temperatura mínima del día (°C)      |
| `precipitacion`      | float  | Precipitación acumulada del día (mm) |

---

## Funcionalidades

El programa presenta un menú interactivo con las siguientes opciones:

| Opción | Descripción                                                             |
| ------ | ----------------------------------------------------------------------- |
| 1      | Cargar datos desde CSV                                                  |
| 2      | Mostrar registros                                                       |
| 3      | Mostrar estadísticas (promedio, máxima, mínima, precipitación promedio) |
| 4      | Generar los tres gráficos y guardarlos en `/resultados`                 |
| 5      | Salir                                                                   |

---
