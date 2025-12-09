import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Tablero de Inteligencia de Negocios", layout="wide")

st.title("📊 Tablero Interactivo – Inteligencia de Negocios")
st.caption("Universidad Panamericana · Campus CDMX")

# -----------------------------------------------------------
# CARGA DE DATOS
# -----------------------------------------------------------
@st.cache_data
def load_data():
    url="UBER dataset.xlsx"
    all_sheets = pd.read_excel(url, sheet_name=None)
    return all_sheets['Switchbacks']
df = load_data()
# -----------------------------------------------------------
# PESTAÑAS PRINCIPALES
# -----------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📈 Documentación General", "🔍 Datos", "📊 Gráficas"])

# -----------------------------------------------------------
# TAB 1: Info
# -----------------------------------------------------------
with tab1:
    st.markdown("""## 🧠 Tablero Interactivo de Inteligencia de Negocios
    
    ## Universidad Panamericana – Campus Ciudad de México
    <img src="https://posgrados-panamericana.up.edu.mx/hs-fs/hubfs/logo%20posgrados%20con%20espacio.png?width=137&name=logo%20posgrados%20con%20espacio.png" width=150>
    
    Este repositorio contiene un tablero interactivo de Inteligencia de Negocios diseñado para convertir datos crudos en información clara, visual y accionable.
    El proyecto aplica técnicas de análisis, modelado y visualización para apoyar la toma de decisiones dentro de un contexto empresarial.
    
    ## 🎯 Objetivos del Proyecto
    
    Construir un flujo de datos (ETL) ordenado y confiable.
    
    Desarrollar visualizaciones dinámicas que faciliten la identificación de tendencias, patrones y anomalías.
    
    Proveer una herramienta intuitiva para la toma de decisiones basada en datos.
    
    Implementar buenas prácticas de BI aprendidas en la Universidad Panamericana.
    
    ## 📊 Características del Tablero
    
    Filtros interactivos, segmentaciones y vista detallada (drill-down).
    
    KPIs organizados por áreas (operaciones, ventas, finanzas, inventarios, etc.).
    
    Comparativas históricas y análisis por categoría.
    
    Navegación clara y diseño limpio.
    
    ## 🛠️ Tecnologías Utilizadas
    
    Lenguajes / ETL: Python (pandas, numpy), SQL.
    
    Visualización: Streamlit (ajusta según tu caso).
    
    Análisis: EDA, clustering, modelos supervisados (si aplica).
    
    ## 🧱 Estructura del Repositorio
    ```bash
    /data
      ├── raw/            # Datos originales
      ├── processed/      # Datos limpios y transformados
    /src
      ├── etl/            # Scripts de extracción y transformación
      ├── models/         # Modelos analíticos o predictivos
    /dashboard
      ├── powerbi/        # Archivo del tablero (.pbix) o equivalente
    /docs
      ├── readme.md       # Documentación adicional
    ```
    
    ## 📚 Metodología
    
    La información fue recopilada, limpiada, modelada y visualizada siguiendo principios de Business Intelligence.
    El tablero ofrece una visión clara y enfocada en la toma de decisiones estratégicas.
    
    ## 👤 Autor
    Jesús Arturo Jiménez Miranda
    Estudiante de Ingeniería Industrial
    Universidad Panamericana – Campus Ciudad de México""")

# -----------------------------------------------------------
# TAB 2: Comparaciones
# -----------------------------------------------------------
with tab2:
    st.subheader("Dataset del ejercicio")

    st.write("Selecciona el rango de observaciones que deseas visualizar:")

    # Slider de rango equivalente a IntRangeSlider de ipywidgets
    start, end = st.slider(
        "Rango de filas:",
        min_value=0,
        max_value=len(df),
        value=(0, len(df)),   # valor inicial: toda la tabla
        step=1
    )

    # Mostrar sección del dataframe
    st.dataframe(df.iloc[start:end])

# -----------------------------------------------------------
# TAB 3: Resumen e Insights
# -----------------------------------------------------------
with tab3:
    st.subheader("Visualizaciones")

    st.write("Hola Mundo")
