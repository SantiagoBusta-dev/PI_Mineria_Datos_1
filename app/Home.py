import streamlit as st

st.set_page_config(page_title="PI: Minería de Datos 1", layout="wide", initial_sidebar_state="expanded")

# Título principal de la Portada
st.title("🎬 Proyecto Integrador: Minería de Datos 1")
st.subheader("Segmentación Estratégica de Usuarios en Plataforma de Streaming")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Presentación del Proyecto")
    st.write(
        "Este software interactivo constituye la entrega final del **Proyecto Integrador** para la materia "
        "Minería de Datos 1. El trabajo aborda el ciclo completo de un proceso de ciencia de datos aplicado a un "
        "caso de negocio real: una plataforma de streaming en Latinoamérica. "
    )
    
with col2:
    st.markdown("### 👤 Datos del Alumno")
    st.info("""
    * **Alumno:** Santiago Bustamante
    """)

st.markdown("---")
st.markdown("### 🗂️ Estructura del Menú Lateral")
st.markdown("""
* **01 Dataset & Calidad:** Inspección del volumen de datos original e informe técnico del procesamiento de limpieza.
* **02 Análisis Exploratorio (EDA):** Visualizaciones univariadas, bivariadas y multivariadas de las métricas de consumo.
* **03 PCA & Segmentación:** Reducción de variables correlacionadas y mapa de dispersión de los perfiles analizados.
* **04 Conclusiones:** Cierre académico con hallazgos, limitaciones operativas y propuestas futuras de negocio.
""")