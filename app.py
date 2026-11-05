# La app de mi proyecto
# Para verla, en la terminal: streamlit run app.py
# Son los mismos pasos que en app_pisos.py y app_titanic.py. Si te atascas, busca el mismo paso allí.



# Paso 1. La página
# 1.1 Importa streamlit y pandas.
import streamlit as st
import pandas as pd

# 1.2 Pon el nombre de la pestaña del navegador, la página a todo lo ancho y un título que diga de qué va tu proyecto.
st.set_page_config(
    page_title="Football Myths vs Data",
    layout="wide" )

st.title("Football Myths vs Data")
# 1.3 Debajo, una o dos frases con st.write: qué pregunta responde la app y de dónde salen los datos.
st.write(
    "¿Son ciertos algunos de los mitos más conocidos del fútbol? "
    "Analizamos datos de partidos de las cinco grandes ligas europeas "
    "para descubrir qué dicen realmente las estadísticas."
)

# Paso 2. Los datos
# 2.1 La función cargar_datos, con @st.cache_data encima, que lea "datos/datos_limpios.csv" y lo devuelva.
@st.cache_data
def cargar_datos():
    return pd.read_csv("datos_limpios.csv")
#     La limpieza ya está hecha en el cuaderno, así que la función solo lee y devuelve, como en la carta del bar.
# 2.2 Llama a la función y guarda la tabla en una variable con el nombre de tus datos.
df = cargar_datos()


# Paso 3. Los filtros
# 3.1 En la barra de la izquierda (with st.sidebar:), al menos dos filtros:
#     un desplegable o unos botones para una columna de texto, con "Todos" al principio,
#     y una barra para una columna de números.

with st.sidebar:
    st.header("Filtros")

    liga = st.selectbox(
        "Selecciona una liga:",
        ["Todos"] + sorted(df["Liga"].unique().tolist())
    )

    goles = st.slider(
        "Goles del equipo local:",
        min_value=int(df["Goles_local"].min()),
        max_value=int(df["Goles_local"].max()),
        value=(int(df["Goles_local"].min()), int(df["Goles_local"].max()))
    )

# Paso 4. Filtrar
# 4.1 Empieza con filtrados = tu tabla, y después aplica un filtro por cada widget, como en los pisos.
# 4.1 Aplicar filtros
filtrados = df.copy()

if liga != "Todos":
    filtrados = filtrados[filtrados["Liga"] == liga]

filtrados = filtrados[
    (filtrados["Goles_local"] >= goles[0]) &
    (filtrados["Goles_local"] <= goles[1])
]


# Paso 5. Si no queda nada
# 5.1 Si filtrados está vacía, saca un aviso con st.warning y para el programa con st.stop().

if filtrados.empty:
    st.warning("No hay partidos que coincidan con los filtros seleccionados.")
    st.stop()

# Paso 6. Las métricas
# 6.1 Tres métricas en columnas, con los números más importantes para tu pregunta.

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Media de goles locales", round(filtrados["Goles_local"].mean(), 2))

with col2:
    st.metric("Media de goles visitantes", round(filtrados["Goles_visitante"].mean(), 2))

with col3:
    victorias_locales = (filtrados["Resultado_final"] == "H").mean() * 100
    st.metric("% Victorias locales", f"{victorias_locales:.1f}%")

# Paso 7. Las pestañas
# 7.1 Al menos dos pestañas: una con la tabla filtrada y otra con dos gráficos.
# 7.2 Si tus datos tienen latitud y longitud, otra pestaña con el mapa.


tab1, tab2 = st.tabs(["Tabla de partidos", "Gráficos"])

with tab1:
    st.subheader("Partidos filtrados")
    st.dataframe(filtrados)

with tab2:
    st.subheader("Distribución de resultados")

    resultados = filtrados["Resultado_final"].value_counts().reindex(
        ["H", "D", "A"], fill_value=0
    )

    resultados.index = ["Victoria local", "Empate", "Victoria visitante"]

    st.bar_chart(resultados)

    st.subheader("Relación entre tiros y goles locales")

    st.scatter_chart(
        filtrados,
        x="Tiros_local",
        y="Goles_local"
    )

# Paso 8. Una pregunta para el usuario
# 8.1 Una última pestaña con una pregunta, como "¿Cuánto cobrarías por tu piso?" o "¿Te habrías salvado?":
#     el usuario elige algo y la app le contesta con lo que dicen los datos.
# 8.1 Pregunta interactiva
tab3 = st.tabs(["Tu predicción"])[0]

with tab3:
    st.subheader("¡Pon a prueba tu intuición futbolística!")

    respuesta = st.selectbox(
        "¿Qué resultado crees que es más frecuente?",
        ["Victoria local", "Empate", "Victoria visitante"]
    )

    equivalencias = {
        "Victoria local": "H",
        "Empate": "D",
        "Victoria visitante": "A"
    }

    resultado_real = filtrados["Resultado_final"].value_counts(normalize=True) * 100

    porcentaje = resultado_real.get(equivalencias[respuesta], 0)

    st.write(
        f"Según los datos, el {porcentaje:.1f}% de los partidos "
        f"terminaron con el resultado que has elegido."
    )