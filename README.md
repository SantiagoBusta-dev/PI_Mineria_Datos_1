Proyecto Integrador de Minería de Datos 1

Información general:

Este repositorio contiene la entrega final del Proyecto Integrador de la materia Minería de Datos 1. El trabajo abarca el ciclo completo de procesamiento de datos, desde los archivos brutos hasta la implementación de una aplicación web interactiva para la visualización de los resultados.

Objetivo:

El objetivo principal de este proyecto es analizar y procesar el dataset de [streaming_users_dirty](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json). Buscando identificar patrones claves en los comportamientos de los usuarios, reducir la complejidad y exponer los hallazgos mediante una interfaz interactiva, facilitando la toma de decisiones mediante evidencia, transformando los datos crudos en información útil.

Dataset:

Este proyecto usa el archivo [streaming_user_dirty.json](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json) el cual incluye variables fundamentales sobre el comportamiento de los usuarios que son el tiempo de reproducción, el tipo de suscripción, etc. EL dataset original cuenta con muchos registros y se puede ver la inspección en [01_inspección_inicial.ipynb](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/01_inspeccion_inicial.ipynb), los cuales fueron procesados para la limpieza, La versión final con todo el análisis está en [streaming_dataset_limpio.csv](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/processed/streaming_dataset_limpio.csv).

Preparación y calidad de datos:

El proceso de limpieza fue fundamental para asegurar la integridad de la información. Se realizaron las siguientes acciones técnicas:Eliminación de valores nulos, tratamiento de valores atípicos y corrección de tipos de datos,normalización de variables clave para el modelado.
La trazabilidad de estas transformaciones quedó documentada en el archivo de [logs](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/logs/pipeline_log.csv). La validación final se encuentra en el notebook [02_calidad_y_limpieza.ipynb](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/02_calidad_y_limpieza.ipynb).

Resumen del análisis exploratorio:

El análisis se centró en identificar correlaciones y distribuciones de las variables principales, detectando patrones de consumo mediante visualizaciones univariado, bivariadas y multivariado. Todos los detalles, incluyendo histogramas y diagramas de dispersión, se encuentran en el notebook [03_eda.ipynb](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/03_eda.ipynb).

Reducción de dimensionalidad:

Para mejorar la eficiencia y eliminar redundancias, se aplicó la técnica de PCA (Análisis de Componentes Principales) en el notebook [04_pca.ipynb](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/04_pca.ipynb). Esto facilitó la interpretación visual de los grupos de usuarios manteniendo la varianza significativa.

Visualización interactiva:

La aplicación web permite interactuar con los resultados procesados de forma intuitiva: [Enlace a la aplicación](https://pimineriadatos1-kjpk4kvynnmh4hmnjdqcis.streamlit.app/).


Cómo ejecutar localmente:

1-Clonar este repositorio: git clone [https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1)
2-Instalar dependencias: pip install -r [requirements.txt](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/requirements.txt)
3-Ejecutar la app: streamlit run [app/Home.py](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/app/Home.py)

[Conclusiones](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/05_conclusiones.ipynb):

El proyecto permitió transformar datos brutos en información estratégica, optimizando la interpretación mediante técnicas de minería y reducción de dimensionalidad. Los resultados proporcionan una base sólida para el análisis del comportamiento de usuarios, cumpliendo con los objetivos propuestos.
