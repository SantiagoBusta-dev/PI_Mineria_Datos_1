import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análisis Exploratorio", layout="wide")

st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("---")

try:
    df_eda = pd.read_csv("data/processed/streaming_dataset_limpio.csv")
    
    # ==========================================
    # 1. VISUALIZACIONES UNIVARIADAS
    # ==========================================
    st.markdown("## 📊 1. Análisis Univariado")
    uv1, uv2 = st.columns(2)
    
    with uv1:
        st.markdown("#### Gráfico 1: Distribución de Edades")
        fig1, ax1 = plt.subplots(figsize=(5, 3.5))
        sns.histplot(df_eda['age'], kde=True, color="#2b5c8f", ax=ax1)
        ax1.set_title("Distribución de Edad de los Usuarios")
        st.pyplot(fig1)
        st.info("**Interpretación:** Revela una base demográfica madura y homogéneamente distribuida entre los 18 y los 60 años, indicando que el servicio atrae transversalmente a distintas generaciones sin concentraciones anómalas.")

    with uv2:
        st.markdown("#### Gráfico 2: Distribución del Tiempo de Reproducción")
        fig2, ax2 = plt.subplots(figsize=(5, 3.5))
        sns.histplot(df_eda['monthly_watch_time_mins'], kde=True, color="#d95f02", ax=ax2)
        ax2.set_title("Distribución de Minutos Mensuales")
        st.pyplot(fig2)
        st.info("**Interpretación:** Evidencia un sesgo positivo severo hacia la derecha. La mayoría de los usuarios registran consumos bajos o moderados, mientras que una cola delgada representa a los consumidores intensivos cerca de los 5,000 minutos.")

    st.markdown("---")

    # ==========================================
    # 2. VISUALIZACIONES BIVARIADAS
    # ==========================================
    st.markdown("## 📊 2. Análisis Bivariado")
    bv1, bv2 = st.columns(2)
    
    with bv1:
        st.markdown("#### Gráfico 3: Tiempo de Reproducción por País")
        fig3, ax3 = plt.subplots(figsize=(5, 3.5))
        sns.boxplot(data=df_eda, x='country', y='monthly_watch_time_mins', palette="Set2", ax=ax3)
        ax3.set_title("Consumo Mensual según Región")
        plt.xticks(rotation=45)
        st.pyplot(fig3)
        st.info("**Interpretación:** Las medianas y rangos intercuartílicos de consumo se mantienen estables a lo largo de Latinoamérica, sugiriendo que la nacionalidad de origen por sí sola no determina fluctuaciones macro en el tiempo total de streaming.")

    with bv2:
        st.markdown("#### Gráfico 4: Tickets de Soporte por Plan de Suscripción")
        fig4, ax4 = plt.subplots(figsize=(5, 3.5))
        sns.barplot(data=df_eda, x='subscription_plan', y='customer_support_tickets', estimator=sum, palette="muted", ax=ax4)
        ax4.set_title("Volumen Total de Tickets según Plan")
        st.pyplot(fig4)
        st.info("**Interpretación:** Permite evaluar si los usuarios de planes premium saturan los canales de reclamos con mayor frecuencia en comparación con los planes básicos, ayudando a planificar la asignación de agentes de soporte.")

    st.markdown("---")

    # ==========================================
    # 3. VISUALIZACIÓN MULTIVARIADA
    # ==========================================
    st.markdown("## 📊 3. Análisis Multivariado")
    st.markdown("#### Gráfico 5: Matriz de Correlación de Características Numéricas")
    
    num_cols = df_eda.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    fig5, ax5 = plt.subplots(figsize=(7, 4))
    sns.heatmap(df_eda[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, ax=ax5)
    ax5.set_title("Correlación Lineal entre Variables")
    st.pyplot(fig5)
    st.info("**Interpretación:** La matriz cruza edad, minutos y tickets en simultáneo. Revela la ausencia de correlaciones lineales fuertes entre el volumen de soporte y el tiempo de consumo, justificando la necesidad de aplicar algoritmos no lineales y multidimensionales como PCA para encontrar patrones ocultos.")

except Exception as e:
    st.error(f"⚠️ Error al procesar los gráficos del EDA: {e}")