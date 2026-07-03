import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset & Calidad", layout="wide")

st.title("📊 Descripción del Dataset y Calidad de Datos")
st.markdown("---")

st.markdown("### 🔍 Resumen General de Calidad")
st.write(
    "El conjunto de datos inicial presentaba 8,160 registros distribuidos en variables demográficas y de consumo. "
    "A través de una inspección documentada, se detectaron duplicados estructurales, formatos corruptos de fechas, "
    "valores faltantes e inconsistencias categóricas extremas (como 26 formas distintas de registrar países)."
)

st.markdown("### 📋 Registro de Transformaciones (Log ETL)")
try:
    log_df = pd.read_csv("logs/pipeline_log.csv")
    st.dataframe(log_df, use_container_width=True, hide_index=True)
    st.caption("Traza oficial extraída de logs/pipeline_log.csv")
except FileNotFoundError:
    st.warning("⚠️ El archivo 'logs/pipeline_log.csv' no fue encontrado.")

st.markdown("---")
st.markdown("### 👁️ Vista Previa de los Datos Reales")

col_raw, col_proc = st.columns(2)

with col_raw:
    st.markdown("#### Dataset Original (Antes de la Limpieza)")
    try:
        df = pd.read_json('data/raw/streaming_users_dirty.json')
        st.dataframe(df.head(10), use_container_width=True)
        st.caption(f"Registros iniciales leídos: {df.shape[0]} filas.")
    except Exception as e:
        st.error(f"No se pudo cargar el archivo original JSON: {e}")

with col_proc:
    st.markdown("#### Dataset Procesado (Final Limpio)")
    try:
        df_eda = pd.read_csv("data/processed/streaming_dataset_limpio.csv")
        st.dataframe(df_eda.head(10), use_container_width=True)
        st.caption(f"Registros depurados listos para análisis: {df_eda.shape[0]} filas.")
    except Exception as e:
        st.error(f"No se pudo cargar el archivo limpio CSV: {e}")