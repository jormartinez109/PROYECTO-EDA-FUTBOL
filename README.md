# Football Myths vs Data ⚽

**¿Cuánto hay de realidad en algunos de los mitos más repetidos del fútbol?**

Proyecto de análisis exploratorio de datos (EDA) con Python que estudia **45.516 partidos** de las cinco grandes ligas europeas y presenta los resultados en una aplicación interactiva con Streamlit.

> El objetivo es describir patrones históricos y contrastar creencias futbolísticas. Los resultados no demuestran causalidad ni predicen partidos futuros.

## Aplicación interactiva

La aplicación permite filtrar por liga, temporada y periodo. Incluye seis apartados:

1. **Ventaja local:** distribución de resultados y goles medios de locales y visitantes.
2. **Ataque:** tiros, tiros a puerta y relación con los goles.
3. **Descanso:** relación entre el resultado al descanso y el resultado final.
4. **Elo:** relación entre diferencia Elo y diferencia de goles.
5. **Disciplina:** faltas y tarjetas según el resultado.
6. **Tu intuición:** explora las frecuencias históricas del resultado final según la situación al descanso.

**Estado del despliegue:** el proyecto está preparado para Streamlit Community Cloud. La publicación pública requiere completar el alta y el despliegue desde la cuenta propietaria. Consulta [DEPLOY.md](DEPLOY.md).

## Preguntas del proyecto

- ¿Existe una ventaja descriptiva por jugar en casa?
- ¿Los equipos que realizan más tiros y tiros a puerta consiguen mejores resultados?
- ¿Qué relación hay entre el resultado al descanso y el resultado final?
- ¿El equipo con mayor puntuación Elo suele imponerse?
- ¿Cómo varían las faltas y las tarjetas según el resultado?

## Datos y procedencia

El archivo original `Matches.csv` forma parte de [Club Football Match Data](https://github.com/xgabora/Club-Football-Match-Data). Según el repositorio, los resultados y estadísticas proceden de [Football-Data.co.uk](https://www.football-data.co.uk/) y las puntuaciones Elo de [ClubElo](http://clubelo.com/).

- Archivo original: **238.858 partidos y 48 columnas**.
- Ligas seleccionadas: Premier League, LaLiga, Serie A, Ligue 1 y Bundesliga.
- Registros de esas cinco ligas antes de la limpieza final: **45.559**.
- Dataset final: **45.516 filas y 22 columnas**.
- Periodo: **28/07/2000 – 03/09/2026**.
- Cada fila representa un partido.

### Variables

| Grupo | Variables |
|---|---|
| Identificación | `Liga`, `Fecha`, `Equipo_local`, `Equipo_visitante` |
| Elo | `Elo_local`, `Elo_visitante` |
| Resultado | `Goles_local`, `Goles_visitante`, `Resultado_final` |
| Descanso | `Goles_descanso_local`, `Goles_descanso_visitante`, `Resultado_descanso` |
| Ataque | `Tiros_local`, `Tiros_visitante`, `Tiros_a_puerta_local`, `Tiros_a_puerta_visitante` |
| Disciplina | `Faltas_local`, `Faltas_visitante`, `Amarillas_local`, `Amarillas_visitante`, `Rojas_local`, `Rojas_visitante` |

Los resultados `H`, `D` y `A` representan victoria local, empate y victoria visitante, respectivamente.

## Limpieza y preparación

1. Se seleccionaron las cinco grandes ligas y las 22 variables relacionadas con las preguntas.
2. Se eliminaron **43 registros** con valores ausentes en Elo o en los datos del descanso necesarios para el análisis.
3. Se conservaron los valores ausentes de tiros, tiros a puerta, faltas y tarjetas. No se imputaron valores sin justificación; cada análisis utiliza los datos disponibles para la variable correspondiente.
4. Se sustituyeron los códigos de liga por sus nombres completos.
5. Se comprobó que el dataset final no contiene filas duplicadas.

Los valores ausentes que se mantienen son: 4.911 en cada columna de tiros, 5.717 en cada columna de tiros a puerta, 5.668 en cada columna de faltas, 4.897 en amarillas locales, 4.896 en amarillas visitantes y 4.896 en cada columna de rojas.

## Resultados principales

### 1. Ventaja local

- Victoria local: **45,59 %**.
- Empate: **25,87 %**.
- Victoria visitante: **28,54 %**.
- Goles medios: **1,53** para el equipo local y **1,16** para el visitante.

### 2. Resultado al descanso

- Si el local iba ganando al descanso, acabó ganando el **79,3 %** de las veces.
- Si el visitante iba ganando al descanso, acabó ganando el **68,1 %**.
- Si había empate al descanso, el **37,7 %** acabó en empate y el **37,1 %** en victoria local.

### 3. Elo y diferencia de goles

La correlación entre la diferencia Elo (local menos visitante) y la diferencia de goles fue **0,42**, una asociación positiva moderada. En los partidos con ganador, el equipo con mayor Elo ganó el **66,4 %**. Los empates se excluyen de este último cálculo.

### 4. Producción ofensiva

En partidos ganados por el equipo local, este realizó una media de **14,65 tiros** y **6,28 tiros a puerta**. En los empates, las medias fueron 13,46 y 4,68; en las derrotas locales, 12,56 y 4,09. Las medias usan solo los partidos con el dato disponible.

## Cómo ejecutar el proyecto

Requisitos: Python 3.10 o superior.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

En Windows, activa el entorno con:

```powershell
.venv\\Scripts\\activate
```

La aplicación necesita que `app.py`, `datos_limpios.csv` y `requirements.txt` estén en la raíz del repositorio. El cuaderno `eda.ipynb` conserva el proceso de análisis exploratorio.

## Presentación

El guion de exposición de 8–10 minutos está en [guion_presentacion.md](guion_presentacion.md). La presentación PowerPoint y el paquete completo de trabajo se entregan también como archivos descargables fuera del repositorio.

## Tecnologías

- Python
- pandas y NumPy
- Plotly
- Streamlit

## Limitaciones

- La disponibilidad de tiros, faltas y tarjetas varía según liga y temporada.
- Los tamaños muestrales pueden cambiar entre análisis por los valores ausentes.
- Los análisis son descriptivos y no controlan todos los factores que influyen en el resultado.
- Una correlación o frecuencia observada no implica causalidad.
- La variable de resultado al descanso no equivale a conocer el minuto exacto en que se marcó el primer gol.

## Fuentes y atribución

- [Club Football Match Data](https://github.com/xgabora/Club-Football-Match-Data)
- [Football-Data.co.uk](https://www.football-data.co.uk/)
- [ClubElo](http://clubelo.com/)

Consulta las condiciones de reutilización y licencia en las fuentes originales.
