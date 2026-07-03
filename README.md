Proyecto Integrador de Minería de Datos 1

Información general:

Este repositorio contiene la entrega final del Proyecto Integrador de la materia Minería de Datos 1. El trabajo abarca el ciclo completo de procesamiento de datos, desde los archivos brutos hasta la implementación de una aplicación web interactiva para la visualización de los resultados.

Objetivo:

El objetivo principal de este proyecto es analizar y procesar el dataset de [streaming_users_dirty](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json). Buscando identificar patrones claves en los comportamientos de los usuarios, reducir la complejidad y exponer los hallazgos mediante una interfaz interactiva, facilitando la toma de decisiones mediante evidencia, transformando los datos crudos en información útil.

Dataset:

Este proyecto usa el archivo [streaming_user_dirty.json](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/raw/streaming_users_dirty.json) el cual incluye variables fundamentales sobre el comportamiento de los usuarios que son el tiempo de reproducción, el tipo de suscripción, etc. EL dataset original cuenta con muchos registros, los cuales fueron procesados para la limpieza, La versión final con todo el análisis está en [streaming_dataset_limpio.csv](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/data/processed/streaming_dataset_limpio.csv).

Resumen del análisis exploratorio:

El análisis se centró en identificar correlaciones y distribuciones de las variables principales, detectando patrones de consumo mediante visualizaciones univariado, bivariadas y multivariado. Todos los detalles, incluyendo histogramas y diagramas de dispersión, se encuentran en el notebook [03_eda.ipynb](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/03_eda.ipynb).

Reducción de dimensionalidad:

Para mejorar la eficiencia y eliminar redundancias, se aplicó la técnica de PCA (Análisis de Componentes Principales) en el notebook [04_pca.ipynb](https://github.com/SantiagoBusta-dev/PI_Mineria_Datos_1/blob/main/notebooks/04_pca.ipynb). Esto facilitó la interpretación visual de los grupos de usuarios manteniendo la varianza significativa.


