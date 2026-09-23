# 📊 Proyecto Integrador — Minería de Datos 1

🚀 **[Ver aplicación interactiva en Streamlit](https://pimineriadatos1-kjpk4kvynnmh4hmnjdqcis.streamlit.app/)**

---

## 📌 Descripción

Proyecto desarrollado individualmente como parte de la materia **Minería de Datos 1**.

El proyecto aborda un proceso completo de análisis y procesamiento de datos, desde la inspección y limpieza de un dataset hasta el análisis exploratorio, la reducción de dimensionalidad mediante PCA y la presentación de resultados mediante una aplicación web interactiva desarrollada con **Streamlit**.

El objetivo es transformar datos sin procesar en información útil para identificar patrones y comprender el comportamiento de los usuarios de servicios de streaming.

---

## 🎯 Objetivo

Analizar el dataset `streaming_users_dirty` para identificar patrones en el comportamiento de los usuarios, mejorar la calidad de los datos, reducir la dimensionalidad de las variables y presentar los principales resultados mediante visualizaciones y una aplicación interactiva.

El proyecto sigue las siguientes etapas:

**Datos brutos → Inspección → Limpieza → EDA → PCA → Conclusiones → Aplicación interactiva**

---

## 🛠️ Tecnologías utilizadas

* 🐍 **Python**
* 🐼 **Pandas**
* 🔢 **NumPy**
* 📊 **Matplotlib**
* 📈 **Seaborn**
* 🤖 **Scikit-learn**
* 📓 **Jupyter Notebook**
* 🌐 **Streamlit**
* 🔧 **Git / GitHub**

---

## 📂 Dataset

El proyecto utiliza el archivo [`streaming_users_dirty.json`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json), que contiene información relacionada con el comportamiento de usuarios de servicios de streaming.

Entre las variables analizadas se encuentran características relacionadas con el consumo de contenido y el tipo de suscripción.

El dataset original fue inspeccionado y posteriormente procesado durante las distintas etapas del proyecto.

### 📄 Archivos principales

* 📥 [Dataset original — `streaming_users_dirty.json`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json)
* 📊 [Dataset procesado — `streaming_dataset_limpio.csv`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/processed/streaming_dataset_limpio.csv)

---

## 🧹 Preparación y calidad de los datos

La preparación de los datos fue una etapa fundamental del proyecto.

Durante este proceso se realizaron tareas de inspección, limpieza y transformación para mejorar la calidad del dataset y prepararlo para las etapas posteriores del análisis.

Entre las principales tareas se encuentran:

* Inspección inicial del dataset.
* Identificación y tratamiento de valores faltantes.
* Detección y tratamiento de valores atípicos.
* Corrección de tipos de datos.
* Limpieza y transformación de variables.
* Normalización de variables necesarias para el análisis.
* Validación del dataset procesado.

La trazabilidad de las transformaciones realizadas quedó registrada en el archivo de logs.

📋 **[Ver `pipeline_log.csv`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/logs/pipeline_log.csv)**

### 📓 Notebook de inspección inicial

[Ver `01_inspeccion_inicial.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/01_inspeccion_inicial.ipynb)

### 📓 Notebook de calidad y limpieza

[Ver `02_calidad_y_limpieza.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/02_calidad_y_limpieza.ipynb)

---

## 📈 Análisis exploratorio de datos (EDA)

Se realizó un análisis exploratorio para estudiar la distribución de las variables e identificar posibles relaciones y patrones presentes en los datos.

Se utilizaron diferentes técnicas de análisis y visualización, incluyendo:

* Análisis univariado.
* Análisis bivariado.
* Análisis multivariado.
* Histogramas.
* Diagramas de dispersión.
* Análisis de correlaciones.

📓 **[Ver `03_eda.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/03_eda.ipynb)**

---

## 🔎 Reducción de dimensionalidad — PCA

Se aplicó **PCA (Principal Component Analysis)** como técnica de reducción de dimensionalidad.

El objetivo fue reducir la cantidad de variables utilizadas en el análisis, conservando la mayor cantidad posible de información relevante y facilitando la interpretación visual de los datos.

📓 **[Ver `04_pca.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/04_pca.ipynb)**

---

## 🌐 Aplicación interactiva

Como parte del proyecto se desarrolló una aplicación web utilizando **Streamlit**, que permite explorar de manera interactiva los datos y los resultados obtenidos durante el análisis.

La aplicación está organizada en diferentes secciones:

* 📊 **Dataset**
* 📈 **EDA**
* 🔎 **PCA**
* 📝 **Conclusiones**

### 🚀 [Abrir aplicación interactiva](https://pimineriadatos1-kjpk4kvynnmh4hmnjdqcis.streamlit.app/)

### 📂 Archivos de la aplicación

* 🏠 [`Home.py`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/app/Home.py)
* 📊 [`01_Dataset.py`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/app/pages/01_Dataset.py)
* 📈 [`02_EDA.py`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/app/pages/02_EDA.py)
* 🔎 [`03_PCA.py`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/app/pages/03_PCA.py)
* 📝 [`04_Conclusiones.py`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/app/pages/04_Conclusiones.py)

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
│   │   └── streaming_users_dirty.json
│   │
│   └── processed/
│       └── streaming_dataset_limpio.csv
│
├── logs/
│   └── pipeline_log.csv
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── reports/
│   └── informe_final.pdf
│
├── README.md
└── requirements.txt
```

---

## 📓 Etapas del análisis

| Etapa | Archivo                                                                                                                                  | Descripción                     |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 1️⃣   | [`01_inspeccion_inicial.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/01_inspeccion_inicial.ipynb) | Inspección inicial del dataset  |
| 2️⃣   | [`02_calidad_y_limpieza.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/02_calidad_y_limpieza.ipynb) | Limpieza y preparación de datos |
| 3️⃣   | [`03_eda.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/03_eda.ipynb)                               | Análisis exploratorio de datos  |
| 4️⃣   | [`04_pca.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/04_pca.ipynb)                               | Reducción de dimensionalidad    |
| 5️⃣   | [`05_conclusiones.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/05_conclusiones.ipynb)             | Interpretación y conclusiones   |

---

## 📄 Informe final

El proyecto cuenta también con un informe final en formato PDF.

📑 **[Ver `informe_final.pdf`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/reports/informe_final.pdf)**

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

📦 **[Ver `requirements.txt`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/requirements.txt)**

---

## 📌 Conclusiones

El proyecto permitió aplicar diferentes técnicas de minería de datos para transformar un dataset inicialmente desordenado en información procesada y analizable.

A través de las etapas de limpieza, análisis exploratorio y reducción de dimensionalidad mediante PCA, fue posible estudiar diferentes características del comportamiento de los usuarios y representar los resultados mediante visualizaciones.

Finalmente, la aplicación desarrollada con Streamlit permite presentar los resultados de una manera interactiva y accesible.

📓 **[Ver `05_conclusiones.ipynb`](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/05_conclusiones.ipynb)**

---

## 👤 Autor

**Santiago Bustamante**

Proyecto desarrollado individualmente como parte de la formación en **Ciencia de Datos e Inteligencia Artificial**.

🔗 **[GitHub — SantiagoBusta-dev](https://github.com/SantiagoBusta-dev)**
