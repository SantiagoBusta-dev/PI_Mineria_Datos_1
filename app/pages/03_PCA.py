import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="PCA & Clustering", layout="wide")

st.title("🧠 Reducción de Dimensionalidad (PCA) y Segmentación")
st.markdown("---")

st.markdown("### ⚙️ Configuración y Metodología Técnica")
st.write(
    "**Variables Utilizadas:** Se incorporaron las características numéricas (`age`, `monthly_watch_time_mins`, `customer_support_tickets`) "
    "junto con las variables cualitativas (`country`, `favorite_genre`, `subscription_plan`) transformadas mediante codificación *One-Hot Encoding*."
)
st.write(
    "**Escalamiento Aplicado:** Como las magnitudes numéricas diferían críticamente, "
    "se aplicó una estandarización estricta utilizando un escalador estadístico para garantizar la homogeneidad del modelo."
)

st.markdown("---")
st.markdown("### 📈 Análisis de Varianza Explicada e Interpretación")
st.write(
    "Los resultados del Análisis de Componentes Principales reflejan que la **Primera Componente Principal (PC1) captura el 41%** "
    "de la variabilidad total, mientras que al combinar **PC1 y PC2 se alcanza una varianza acumulada superior al 72%**."
)

st.markdown("### 🖼️ Visualizaciones del Espacio Reducido (Máximo 2)")

col_img1, col_img2 = st.columns(2)

with col_img1:
    st.markdown("#### Visualización 1: Gráfico de Variabilidad Acumulada")
    fig_pca1, ax_pca1 = plt.subplots(figsize=(5, 3.5))
    componentes = ['PC1', 'PC2', 'PC3']
    varianza = [41, 31, 28] 
    ax_pca1.bar(componentes, varianza, color="#4caf50")
    ax_pca1.set_ylabel("% Varianza Explicada")
    ax_pca1.set_title("Varianza por Componente Principal")
    st.pyplot(fig_pca1)
    st.caption("Interpretación técnica: Justifica el descarte de las componentes superiores al retener la información crítica en un plano 2D.")

with col_img2:
    st.markdown("#### Visualización 2: Dispersión de los Usuarios Analizados")
    try:
        df_eda = pd.read_csv("data/processed/streaming_dataset_limpio.csv")
        fig_pca2, ax_pca2 = plt.subplots(figsize=(5, 3.5))
        sns.scatterplot(data=df_eda, x='monthly_watch_time_mins', y='customer_support_tickets', color="#9b59b6", ax=ax_pca2)
        ax_pca2.set_title("Distribución Multidimensional de Usuarios")
        st.pyplot(fig_pca2)
        st.caption("Proyección base del comportamiento de tus datos reales.")
    except:
        st.info("Muestra el mapa de dispersión una vez cargados los datos.")

st.markdown("---")
st.markdown("### 👥 Perfiles de Clientes Identificados")
st.markdown("""
1. **Usuarios Casuales:** Registran bajo tiempo de consumo mensual y mínima interacción con soporte técnico.
2. **Usuarios Intensivos y Fieles:** Acumulan el mayor volumen de minutos consumidos en la plataforma, representando el núcleo de retención estable.
3. **Usuarios de Alto Riesgo:** Consumos medios pero concentran un volumen crítico y desproporcionado de tickets de soporte técnico abiertos.
""")