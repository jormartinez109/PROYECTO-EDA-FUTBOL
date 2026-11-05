from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


# -----------------------------------------------------------------------------
# Configuracion general
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Football Myths vs Data",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    [data-testid="stMetric"] {
        background: rgba(128, 128, 128, 0.08);
        border: 1px solid rgba(128, 128, 128, 0.18);
        padding: 14px 16px;
        border-radius: 12px;
    }
    .eyebrow {font-size: .82rem; letter-spacing: .12em; text-transform: uppercase; opacity: .7;}
    </style>
    """,
    unsafe_allow_html=True,
)

RESULTADOS = {
    "H": "Victoria local",
    "D": "Empate",
    "A": "Victoria visitante",
}
ORDEN_RESULTADOS = ["H", "D", "A"]


# -----------------------------------------------------------------------------
# Carga de datos
# -----------------------------------------------------------------------------
@st.cache_data
def cargar_datos():
    ruta = Path(__file__).resolve().parent / "datos_limpios.csv"
    datos = pd.read_csv(ruta, parse_dates=["Fecha"])

    anio = datos["Fecha"].dt.year
    datos["Temporada"] = np.where(
        datos["Fecha"].dt.month >= 7,
        anio.astype(str) + "/" + (anio + 1).astype(str),
        (anio - 1).astype(str) + "/" + anio.astype(str),
    )
    datos["Diferencia_Elo"] = datos["Elo_local"] - datos["Elo_visitante"]
    datos["Diferencia_goles"] = datos["Goles_local"] - datos["Goles_visitante"]
    return datos


df = cargar_datos()


# -----------------------------------------------------------------------------
# Cabecera
# -----------------------------------------------------------------------------
st.markdown('<p class="eyebrow">Análisis estadístico del fútbol</p>', unsafe_allow_html=True)
st.title("Football Myths vs Data")
st.write(
    "¿Cuánto hay de realidad en algunos de los mitos más repetidos del fútbol? "
    "Explora 45.516 partidos de las cinco grandes ligas europeas y contrasta "
    "tu intuición con los datos."
)
st.caption(
    "Resultados históricos y asociaciones estadísticas: describen patrones, "
    "no demuestran causalidad ni predicen un partido concreto."
)


# -----------------------------------------------------------------------------
# Filtros
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("Explora los partidos")

    ligas_disponibles = sorted(df["Liga"].dropna().unique().tolist())
    ligas = st.multiselect("Ligas", ligas_disponibles, default=ligas_disponibles)

    temporadas = sorted(df["Temporada"].dropna().unique().tolist())
    temporadas_sel = st.multiselect("Temporadas", temporadas, default=temporadas)

    fecha_min = df["Fecha"].min().date()
    fecha_max = df["Fecha"].max().date()
    periodo = st.date_input(
        "Periodo",
        value=(fecha_min, fecha_max),
        min_value=fecha_min,
        max_value=fecha_max,
    )
    st.caption("Los filtros se aplican conjuntamente a todas las pestañas.")

filtrados = df[
    df["Liga"].isin(ligas) & df["Temporada"].isin(temporadas_sel)
].copy()

if isinstance(periodo, (tuple, list)) and len(periodo) == 2:
    inicio, fin = periodo
    filtrados = filtrados[
        (filtrados["Fecha"].dt.date >= inicio)
        & (filtrados["Fecha"].dt.date <= fin)
    ]
elif periodo:
    filtrados = filtrados[filtrados["Fecha"].dt.date == periodo]

if filtrados.empty:
    st.warning("No hay partidos que coincidan con los filtros seleccionados.")
    st.stop()


# -----------------------------------------------------------------------------
# Indicadores generales
# -----------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Partidos analizados", f"{len(filtrados):,}".replace(",", "."))
with col2:
    pct_local = filtrados["Resultado_final"].eq("H").mean() * 100
    st.metric("Victorias locales", f"{pct_local:.1f}%")
with col3:
    media_goles = (
        filtrados["Goles_local"] + filtrados["Goles_visitante"]
    ).mean()
    st.metric("Goles por partido", f"{media_goles:.2f}")
with col4:
    diferencia_media = filtrados["Diferencia_goles"].mean()
    st.metric("Diferencia media de goles", f"{diferencia_media:+.2f}")


# -----------------------------------------------------------------------------
# Pestañas
# -----------------------------------------------------------------------------
(
    tab_resumen,
    tab_ataque,
    tab_descanso,
    tab_elo,
    tab_disciplina,
    tab_pregunta,
) = st.tabs(
    [
        "🏠 Ventaja local",
        "🎯 Ataque",
        "⏱️ Descanso",
        "📊 Elo",
        "🟨 Disciplina",
        "💡 Tu intuición",
    ]
)


with tab_resumen:
    st.subheader("¿Existe ventaja por jugar en casa?")
    st.write(
        "Comparamos cómo terminan los partidos y si el patrón cambia entre ligas."
    )

    dist = (
        filtrados.groupby(["Liga", "Resultado_final"])
        .size()
        .rename("Partidos")
        .reset_index()
    )
    totales = dist.groupby("Liga")["Partidos"].transform("sum")
    dist["Porcentaje"] = dist["Partidos"] / totales * 100
    dist["Resultado"] = dist["Resultado_final"].map(RESULTADOS)

    fig = px.bar(
        dist,
        x="Liga",
        y="Porcentaje",
        color="Resultado",
        barmode="stack",
        category_orders={
            "Resultado": [RESULTADOS[x] for x in ORDEN_RESULTADOS]
        },
        labels={
            "Porcentaje": "% de partidos",
            "Liga": "Liga",
            "Resultado": "Resultado",
        },
        title="Distribución de resultados por liga",
    )
    fig.update_layout(legend_title_text="Resultado", yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

    goles_lados = pd.DataFrame(
        {
            "Equipo": ["Local", "Visitante"],
            "Goles medios": [
                filtrados["Goles_local"].mean(),
                filtrados["Goles_visitante"].mean(),
            ],
        }
    )
    fig2 = px.bar(
        goles_lados,
        x="Equipo",
        y="Goles medios",
        text_auto=".2f",
        title="Media de goles por equipo",
        labels={"Goles medios": "Goles por partido"},
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.info(
        "La ventaja local se observa en los resultados históricos; "
        "no implica que jugar en casa garantice ganar."
    )


with tab_ataque:
    st.subheader("¿Más tiros significan más goles?")
    st.write("Comparamos la producción ofensiva según el resultado final.")

    columnas_tiros = [
        "Tiros_local",
        "Tiros_visitante",
        "Tiros_a_puerta_local",
        "Tiros_a_puerta_visitante",
    ]
    tiros_medios = (
        filtrados.groupby("Resultado_final")[columnas_tiros]
        .mean()
        .reindex(ORDEN_RESULTADOS)
    )
    tiros_medios.index = [RESULTADOS[x] for x in tiros_medios.index]
    tiros_medios = tiros_medios.rename(
        columns={
            "Tiros_local": "Tiros local",
            "Tiros_visitante": "Tiros visitante",
            "Tiros_a_puerta_local": "A puerta local",
            "Tiros_a_puerta_visitante": "A puerta visitante",
        }
    )

    fig = px.bar(
        tiros_medios.reset_index(names="Resultado"),
        x="Resultado",
        y=["Tiros local", "Tiros visitante"],
        barmode="group",
        title="Tiros medios según el resultado final",
        labels={"value": "Tiros por partido", "variable": "Equipo"},
    )
    st.plotly_chart(fig, use_container_width=True)

    validos = filtrados.dropna(
        subset=["Tiros_a_puerta_local", "Goles_local"]
    )
    if len(validos) > 6000:
        validos = validos.sample(6000, random_state=42)

    if len(validos) >= 2:
        corr = filtrados["Tiros_a_puerta_local"].corr(
            filtrados["Goles_local"]
        )
        st.metric(
            "Correlación entre tiros a puerta locales y goles locales",
            f"{corr:.2f}",
        )
        fig2 = px.scatter(
            validos,
            x="Tiros_a_puerta_local",
            y="Goles_local",
            color="Resultado_final",
            color_discrete_sequence=px.colors.qualitative.Set2,
            opacity=0.55,
            labels={
                "Tiros_a_puerta_local": "Tiros a puerta del equipo local",
                "Goles_local": "Goles del equipo local",
                "Resultado_final": "Resultado final",
            },
            title=(
                "Tiros a puerta y goles locales "
                "(muestra de hasta 6.000 partidos)"
            ),
        )
        fig2.update_traces(marker={"size": 6})
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning(
            "No hay suficientes observaciones completas para calcular esta relación."
        )

    st.caption(
        "Los promedios de cada estadística utilizan únicamente los partidos "
        "con ese dato disponible."
    )


with tab_descanso:
    st.subheader("¿Qué ocurre después del descanso?")
    st.write(
        "La tabla muestra el resultado final según el marcador que había "
        "al descanso. Cada fila suma el 100 %."
    )

    transicion = (
        pd.crosstab(
            filtrados["Resultado_descanso"],
            filtrados["Resultado_final"],
            normalize="index",
        )
        .reindex(
            index=ORDEN_RESULTADOS,
            columns=ORDEN_RESULTADOS,
            fill_value=0,
        )
        * 100
    )
    transicion.index = [RESULTADOS[x] for x in transicion.index]
    transicion.columns = [RESULTADOS[x] for x in transicion.columns]

    fig = px.imshow(
        transicion,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale="Blues",
        labels={
            "x": "Resultado final",
            "y": "Resultado al descanso",
            "color": "%",
        },
        title="Del resultado al descanso al resultado final (%)",
    )
    st.plotly_chart(fig, use_container_width=True)

    n_descanso = (
        filtrados["Resultado_descanso"]
        .value_counts()
        .reindex(ORDEN_RESULTADOS, fill_value=0)
    )
    st.caption(
        "Partidos por situación al descanso: "
        + " · ".join(
            f"{RESULTADOS[k]}: {n_descanso[k]:,}".replace(",", ".")
            for k in ORDEN_RESULTADOS
        )
    )


with tab_elo:
    st.subheader("¿El equipo con mayor Elo suele imponerse?")
    st.write(
        "Elo aproxima la fuerza relativa de los equipos. Aquí comparamos "
        "la diferencia Elo con la diferencia de goles."
    )

    elo_corr = filtrados["Diferencia_Elo"].corr(
        filtrados["Diferencia_goles"]
    )
    col_a, col_b = st.columns(2)

    with col_a:
        st.metric(
            "Correlación Elo - diferencia de goles",
            f"{elo_corr:.2f}",
        )

    with col_b:
        decisivos = filtrados[
            filtrados["Resultado_final"].isin(["H", "A"])
        ].copy()
        if len(decisivos):
            favorito_gana = (
                (
                    (decisivos["Diferencia_Elo"] > 0)
                    & (decisivos["Resultado_final"] == "H")
                )
                | (
                    (decisivos["Diferencia_Elo"] < 0)
                    & (decisivos["Resultado_final"] == "A")
                )
            )
            pct_favorito = favorito_gana.mean() * 100
            st.metric(
                "Gana el equipo con mayor Elo",
                f"{pct_favorito:.1f}%",
                help=(
                    "Solo partidos con victoria local o visitante; "
                    "se excluyen los empates."
                ),
            )
        else:
            st.metric("Gana el equipo con mayor Elo", "Sin datos")

    muestra_elo = filtrados[
        ["Diferencia_Elo", "Diferencia_goles", "Resultado_final"]
    ].dropna()
    if len(muestra_elo) > 6000:
        muestra_elo = muestra_elo.sample(6000, random_state=42)

    fig = px.scatter(
        muestra_elo,
        x="Diferencia_Elo",
        y="Diferencia_goles",
        color="Resultado_final",
        opacity=0.5,
        labels={
            "Diferencia_Elo": "Elo local − Elo visitante",
            "Diferencia_goles": "Goles local − goles visitante",
            "Resultado_final": "Resultado final",
        },
        title="Diferencia de Elo y diferencia de goles",
    )
    fig.add_hline(y=0, line_dash="dot", opacity=0.5)
    fig.add_vline(x=0, line_dash="dot", opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Una asociación positiva no demuestra que el Elo cause el resultado. "
        "Los empates no se incluyen en el porcentaje de victorias del equipo "
        "con mayor Elo."
    )


with tab_disciplina:
    st.subheader("¿Cómo se relaciona la disciplina con el resultado?")
    st.write(
        "Comparamos faltas y tarjetas medias de los equipos locales y "
        "visitantes según el resultado final."
    )

    disciplina_cols = [
        "Faltas_local",
        "Faltas_visitante",
        "Amarillas_local",
        "Amarillas_visitante",
        "Rojas_local",
        "Rojas_visitante",
    ]
    disciplina = (
        filtrados.groupby("Resultado_final")[disciplina_cols]
        .mean()
        .reindex(ORDEN_RESULTADOS)
    )
    disciplina.index = [RESULTADOS[x] for x in disciplina.index]
    disciplina = disciplina.rename(
        columns={
            "Faltas_local": "Faltas local",
            "Faltas_visitante": "Faltas visitante",
            "Amarillas_local": "Amarillas local",
            "Amarillas_visitante": "Amarillas visitante",
            "Rojas_local": "Rojas local",
            "Rojas_visitante": "Rojas visitante",
        }
    )

    fig = px.bar(
        disciplina.reset_index(names="Resultado"),
        x="Resultado",
        y=["Amarillas local", "Amarillas visitante"],
        barmode="group",
        title="Tarjetas amarillas medias por partido",
        labels={"value": "Tarjetas por partido", "variable": "Equipo"},
    )
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        disciplina.reset_index(names="Resultado"),
        x="Resultado",
        y=["Faltas local", "Faltas visitante"],
        barmode="group",
        title="Faltas medias por partido",
        labels={"value": "Faltas por partido", "variable": "Equipo"},
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.caption(
        "Las medias se calculan con los registros disponibles para cada "
        "variable; los valores ausentes no se sustituyen."
    )


with tab_pregunta:
    st.subheader("¿Qué dice el histórico sobre tu intuición?")
    st.write(
        "Elige cómo iba el partido al descanso y observa cómo terminó "
        "ese tipo de encuentro en los datos seleccionados."
    )

    situacion = st.selectbox(
        "¿Qué resultado había al descanso?",
        options=ORDEN_RESULTADOS,
        format_func=lambda x: RESULTADOS[x],
    )
    historico = filtrados[
        filtrados["Resultado_descanso"] == situacion
    ]

    if historico.empty:
        st.warning(
            "No hay partidos para esa situación al descanso "
            "con los filtros actuales."
        )
    else:
        porcentajes = (
            historico["Resultado_final"]
            .value_counts(normalize=True)
            .reindex(ORDEN_RESULTADOS, fill_value=0)
            * 100
        )
        salida = pd.DataFrame(
            {
                "Resultado final": [
                    RESULTADOS[x] for x in ORDEN_RESULTADOS
                ],
                "Porcentaje": porcentajes.values,
            }
        )
        fig = px.bar(
            salida,
            x="Resultado final",
            y="Porcentaje",
            text_auto=".1f",
            title=(
                "Resultado final cuando al descanso había: "
                f"{RESULTADOS[situacion].lower()}"
            ),
            labels={"Porcentaje": "% de partidos"},
        )
        fig.update_layout(yaxis_range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)

        mas_frecuente = porcentajes.idxmax()
        st.success(
            f"En {len(historico):,} partidos comparables, el resultado "
            f"final más frecuente fue {RESULTADOS[mas_frecuente].lower()} "
            f"({porcentajes[mas_frecuente]:.1f}%).".replace(",", ".")
        )
        st.caption(
            "Es una frecuencia histórica condicionada por el marcador "
            "al descanso, no una predicción de un encuentro futuro."
        )


# -----------------------------------------------------------------------------
# Fuente y metodologia
# -----------------------------------------------------------------------------
st.divider()
st.caption(
    "Fuente: Club Football Match Data (Football-Data.co.uk y ClubElo). "
    "Análisis descriptivo elaborado para Football Myths vs Data. "
    "Las estadísticas con datos ausentes utilizan solo observaciones disponibles."
)
