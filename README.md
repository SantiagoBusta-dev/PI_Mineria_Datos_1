# 📊 Proyecto Integrador — Minería de Datos 1

## 📌 Descripción

Proyecto desarrollado individualmente como parte de la materia **Minería de Datos 1**.

El proyecto aborda un proceso completo de análisis y procesamiento de datos, desde la inspección y limpieza de un dataset hasta el análisis exploratorio, la reducción de dimensionalidad mediante PCA y la presentación de resultados mediante una aplicación web interactiva desarrollada con **Streamlit**.

El objetivo es transformar datos sin procesar en información útil para identificar patrones y comprender el comportamiento de los usuarios de servicios de streaming.

---

## 🎯 Objetivo

Analizar el dataset `streaming_users_dirty` para identificar patrones en el comportamiento de los usuarios, procesar y mejorar la calidad de los datos, reducir la dimensionalidad de las variables y presentar los principales resultados mediante visualizaciones y una aplicación interactiva.

El proyecto sigue distintas etapas del proceso de minería de datos:

**Datos brutos → Inspección → Limpieza → EDA → PCA → Conclusiones → Aplicación interactiva**

---

## 🛠️ Tecnologías utilizadas

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Jupyter Notebook**
* **Streamlit**
* **Git / GitHub**

---

## 📂 Dataset

El proyecto utiliza el dataset [`streaming_users_dirty.json`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json), que contiene información relacionada con el comportamiento de usuarios de servicios de streaming.

Entre las variables analizadas se encuentran características relacionadas con el consumo de contenido y el tipo de suscripción.

El dataset original fue inspeccionado y posteriormente procesado durante las distintas etapas del proyecto.

📄 **Dataset original:**
[`streaming_users_dirty.json`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json)

📄 **Dataset procesado:**
[`streaming_dataset_limpio.csv`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/processed/streaming_dataset_limpio.csv)

---

## 🧹 Preparación y calidad de los datos

La preparación de los datos fue una etapa fundamental del proyecto.

Durante este proceso se realizaron tareas como:

* Inspección inicial del dataset.
* Identificación y tratamiento de valores faltantes.
* Detección y tratamiento de valores atípicos.
* Corrección de tipos de datos.
* Limpieza y transformación de variables.
* Normalización de variables necesarias para el análisis.
* Validación del dataset procesado.

La trazabilidad de las transformaciones realizadas quedó registrada en el archivo de logs.

📋 **Log del proceso:**
[`pipeline_log.csv`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/logs/pipeline_log.csv)

📓 **Notebook de inspección:**
[`01_RA_Inspeccion_Inicial.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/01_RA_Inspeccion_Inicial.ipynb)

📓 **Notebook de calidad y limpieza:**
[`02_RA_Calidad_y_Limpieza.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/02_RA_Calidad_y_Limpieza.ipynb)

---

## 📈 Análisis exploratorio de datos (EDA)

Se realizó un análisis exploratorio para estudiar la distribución de las variables y detectar posibles relaciones y patrones presentes en los datos.

Se utilizaron diferentes técnicas de visualización, incluyendo:

* Análisis univariado.
* Análisis bivariado.
* Análisis multivariado.
* Histogramas.
* Diagramas de dispersión.
* Análisis de correlaciones.

📓 **Notebook de EDA:**
[`03_RA_EDA.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/03_RA_EDA.ipynb)

---

## 🔎 Reducción de dimensionalidad — PCA

Se aplicó **PCA (Principal Component Analysis)** como técnica de reducción de dimensionalidad.

El objetivo fue reducir la cantidad de variables utilizadas en el análisis, conservando la mayor cantidad posible de información relevante y facilitando la interpretación visual de los datos.

📓 **Notebook de PCA:**
[`04_RA_PCA.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/04_RA_PCA.ipynb)

---

## 🌐 Aplicación interactiva

Como parte del proyecto se desarrolló una aplicación web utilizando **Streamlit**, que permite explorar de manera interactiva los datos y los resultados obtenidos durante el análisis.

🚀 **[Ver aplicación interactiva](https://pimineriadatos1-kjpk4kvynnmh4hmnjdqcis.streamlit.app/)**

La aplicación incluye diferentes secciones para consultar el dataset, explorar los resultados del EDA, visualizar el análisis PCA y consultar las conclusiones.

---

## 👨‍💻 Desarrollo del proyecto

El desarrollo del proyecto fue realizado **individualmente por mí**, incluyendo las diferentes etapas de procesamiento, análisis y presentación de los resultados.

Entre las principales tareas realizadas se encuentran:

* Inspección y comprensión inicial de los datos.
* Limpieza y transformación del dataset.
* Análisis exploratorio de datos.
* Creación de visualizaciones.
* Aplicación de PCA.
* Interpretación de resultados.
* Organización de notebooks y archivos del proyecto.
* Desarrollo de la aplicación interactiva con Streamlit.
* Documentación del proyecto.

---

## 📁 Estructura del repositorio

```text
PI_Mineria_Datos_1/
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│   └── pipeline_log.csv
│
├── notebooks/
│   ├── 01_RA_Inspeccion_Inicial.ipynb
│   ├── 02_RA_Calidad_y_Limpieza.ipynb
│   ├── 03_RA_EDA.ipynb
│   ├── 04_RA_PCA.ipynb
│   └── 05_RA_Conclusiones.ipynb
│
├── reports/
│
├── README.md
└── requirements.txt
```

---

## 💻 Ejecución local

Para ejecutar el proyecto localmente:

### 1. Clonar el repositorio

```bash
git clone https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1.git
```

### 2. Ingresar al proyecto

```bash
cd PI_Mineria_Datos_1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
streamlit run app/Home.py
```

---

## 📓 Notebooks

El proyecto se encuentra organizado en diferentes notebooks que representan las principales etapas del análisis:

| Notebook                         | Etapa                        |
| -------------------------------- | ---------------------------- |
| `01_RA_Inspeccion_Inicial.ipynb` | Inspección inicial           |
| `02_RA_Calidad_y_Limpieza.ipynb` | Calidad y limpieza           |
| `03_RA_EDA.ipynb`                | Análisis exploratorio        |
| `04_RA_PCA.ipynb`                | Reducción de dimensionalidad |
| `05_RA_Conclusiones.ipynb`       | Conclusiones                 |

---

## 📌 Conclusiones

El proyecto permitió aplicar diferentes técnicas de minería de datos para transformar un dataset inicialmente desordenado en información procesada y analizable.

A través de las etapas de limpieza, análisis exploratorio y reducción de dimensionalidad mediante PCA, fue posible estudiar diferentes características del comportamiento de los usuarios y representar los resultados mediante visualizaciones.

Finalmente, la aplicación desarrollada con Streamlit permite presentar los resultados de una manera interactiva y accesible.

📓 **Notebook de conclusiones:**
[`05_RA_Conclusiones.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/05_RA_Conclusiones.ipynb)

---

## 👤 Autor

**Santiago Bustamante**

Proyecto desarrollado individualmente como parte de la formación en **Ciencia de Datos e Inteligencia Artificial**.
