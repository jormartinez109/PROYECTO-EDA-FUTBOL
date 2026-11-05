# Guion de presentación — Football Myths vs Data 

## 1. El problema 

En el fútbol se repiten muchas afirmaciones: que jugar en casa supone una ventaja, que quien más tira suele ganar o que llegar por delante al descanso prácticamente asegura el resultado. Queríamos comprobar hasta qué punto estas ideas aparecen en los datos. No buscamos predecir partidos, sino describir patrones y comprobar qué afirmaciones tienen respaldo histórico.

## 2. Los datos 

Partimos de un conjunto de 238.858 partidos de distintas competiciones. Para que el análisis fuera más homogéneo, seleccionamos las cinco grandes ligas europeas: Premier League, LaLiga, Serie A, Ligue 1 y Bundesliga. La tabla final contiene 45.516 partidos y 22 variables, desde equipos, goles y resultado al descanso hasta Elo, tiros, faltas y tarjetas. Cada fila representa un partido. El periodo va desde julio de 2000 hasta septiembre de 2026.

## 3. Preparación 

Seleccionamos las variables necesarias para responder a nuestras preguntas. Eliminamos 43 registros que no tenían información en Elo o en el marcador al descanso, porque esas variables son necesarias para los análisis planteados. En cambio, mantuvimos los valores ausentes de tiros, faltas y tarjetas: no era correcto inventar esos datos. Por eso, cada análisis estadístico utiliza solo los partidos que tienen disponible la variable correspondiente. También comprobamos que no había duplicados.

## 4. Hallazgo 1: ventaja local 

El 45,59 % de los partidos terminó con victoria local. Las victorias visitantes representaron el 28,54 % y los empates el 25,87 %. La diferencia también aparece en los goles: los equipos locales marcaron 1,53 de media, frente a 1,16 de los visitantes. Esto respalda descriptivamente la existencia de una ventaja local en esta muestra, aunque no significa que jugar en casa sea la causa única del resultado.

## 5. Hallazgo 2: el descanso 
Cuando el equipo local iba ganando al descanso, terminó ganando el 79,3 % de las veces. Cuando iba por delante el visitante, ganó finalmente el 68,1 %. Cuando el partido estaba empatado al descanso, el resultado final estuvo más repartido: 37,7 % terminó en empate y 37,1 % en victoria local. La situación al descanso está asociada con el desenlace, pero no lo determina.

## 6. Hallazgo 3: Elo y rendimiento ofensivo 

La diferencia de Elo y la diferencia de goles presentan una correlación de 0,42, positiva y moderada. Además, entre los partidos que tuvieron un ganador, el equipo con mayor Elo ganó el 66,4 %. En el análisis ofensivo, los equipos locales que ganaron registraron 14,65 tiros y 6,28 tiros a puerta de media; los que perdieron, 12,56 tiros y 4,09 tiros a puerta. Son asociaciones útiles para entender los resultados, no pruebas de causalidad.

## 7. Demostración de la aplicación 

Abrir la app. Cambiar de liga y de temporada para mostrar cómo cambian los indicadores. Entrar en «Ventaja local» y comparar la distribución de resultados entre ligas. Después, abrir «Ataque» para comparar tiros y tiros a puerta; «Descanso» para mostrar la matriz de transición; «Elo» para explorar la relación entre la fuerza relativa y los goles; y «Disciplina» para comparar faltas y tarjetas. Terminar en «Tu intuición»: seleccionar un resultado al descanso y mostrar la frecuencia histórica de los resultados finales.

## 8. Utilidad y siguientes pasos 

El proyecto convierte un conjunto de datos amplio en información comprensible e interactiva. Puede servir como punto de partida para explorar diferencias entre ligas, temporadas y comportamientos de los equipos. Como siguiente paso, ampliaríamos el análisis con pruebas estadísticas y modelos que controlen simultáneamente distintos factores. La idea principal es sencilla: en vez de dar por ciertos los mitos del fútbol, podemos someterlos a contraste con datos.

---

**Recordatorio para la exposición:** hablar de preguntas, resultados y limitaciones. Abrir la app y usar los filtros en directo. No confundir frecuencias históricas con predicciones.
