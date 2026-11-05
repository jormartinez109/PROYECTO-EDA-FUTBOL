# PROYECTO EDA FUTBOL
# Football Myths vs Data ⚽

**¿Son ciertos los mitos del fútbol?** Un proyecto de análisis estadístico con Python que pone a prueba algunas de las creencias más extendidas sobre el fútbol mediante datos de partidos de las cinco grandes ligas europeas.

## 1. Objetivo del proyecto

El objetivo es analizar estadísticamente partidos de fútbol para comprobar si determinadas creencias tienen respaldo en los datos.

Entre las preguntas que investigamos están:

- ¿Existe una ventaja real por jugar en casa?
- ¿Los equipos que realizan más tiros tienen más posibilidades de ganar?
- ¿Llegar ganando al descanso aumenta las probabilidades de victoria?
- ¿Cometer más faltas y recibir más tarjetas está relacionado con perder?
- ¿El equipo con mayor puntuación Elo suele ganar?

## 2. Los datos

El análisis utiliza el archivo `Matches.csv`, con información de partidos de las cinco grandes ligas europeas:

- Premier League.
- LaLiga.
- Serie A.
- Ligue 1.
- Bundesliga.

**Fuente de los datos:** [Añadir enlace original de descarga].

**Estructura del dataset final:**
- Filas: [Completar con el número de filas después de la limpieza].
- Columnas: 22.
- Cada fila representa un partido de fútbol.

Las variables incluyen información sobre los equipos, goles, resultados al descanso y al final, puntuaciones Elo, tiros, faltas y tarjetas.

## 3. Limpieza y preparación

Antes del análisis se realizaron las siguientes operaciones:

- Selección de las cinco grandes ligas europeas.
- Selección de las 22 variables relevantes para las preguntas del proyecto.
- Eliminación de registros con valores ausentes en las variables Elo y resultados al descanso.
- Conservación de los valores ausentes en tiros, tiros a puerta, faltas y tarjetas, al no disponer de información suficiente para sustituirlos.
- Sustitución de los códigos originales de las ligas por sus nombres completos.
- Comprobación de registros duplicados, sin encontrar duplicados.

## 4. Principales hallazgos

**1. Ventaja de jugar en casa.** Los equipos locales marcaron una media de **1,53 goles por partido**, frente a los 1,16 goles de los visitantes.

**2. Actividad ofensiva.** Los equipos locales realizaron una media de **13,74 tiros por partido**, frente a los 11,04 de los visitantes.

**3. Tiros y goles.** La correlación entre los tiros locales y los goles locales fue de **0,26**, lo que indica una relación lineal positiva, aunque débil.

Estos resultados son descriptivos y no demuestran por sí solos relaciones causales.

## 5. Aplicación interactiva

La aplicación permite explorar los partidos mediante filtros y visualizar diferentes estadísticas.

**Cómo utilizarla:**
1. Seleccionar una liga.
2. Ajustar el intervalo de goles locales.
3. Consultar las métricas y los gráficos.
4. Explorar la tabla de partidos filtrados.
5. Responder a la pregunta interactiva y comparar la elección con los resultados históricos.

**Captura de la aplicación:**

![Captura de Football Myths vs Data](captura_app.png)

**Enlace a la aplicación:** [Añadir enlace si se publica].

Actualmente, la aplicación se ejecuta localmente mediante Streamlit.

## 6. Tecnologías utilizadas

- Python.
- Pandas.
- Matplotlib.
- Streamlit.

## 7. Cómo ejecutar el proyecto

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar las dependencias:

```bash
pip install pandas streamlit matplotlib
```

4. Ejecutar la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá en el navegador.

## 8. Posibles mejoras

- Comparar la ventaja local entre las cinco ligas.
- Estudiar la relación entre tiros a puerta y resultados.
- Analizar cómo influye el resultado al descanso en el resultado final.
- Investigar la relación entre la diferencia de Elo y las victorias inesperadas.
- Incorporar nuevos indicadores y visualizaciones interactivas.
