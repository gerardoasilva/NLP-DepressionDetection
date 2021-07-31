# Modelo para Detección de Depresión

##### **Equipo 4**

- A01136536 Gerardo Silva
- A00822830 Donaldo Salazar
- A01039863 Víctor Villarreal
- A01338143 Ricardo Ramirez


Según la Organización Mundial de la Salud la [depresión](https://www.who.int/es/news-room/fact-sheets/detail/depression) es considerada una enfermedad muy frecuente en el mundo, se estima que esta afecta a más de 300 millones de personas. Se puede presentar de diferentes maneras y puede convertirse en un problema de salud serio, causando sufrimiento y alterando todo tipo de actividades de quien la padece. Muchas veces, esta enfermedad terimna en suicidio.

Con el propósito de aportar al desarrollo de nuevas herramientas de Inteligencia Artificial que ayuden a identificar a tiempo este tipo de enfermedades en la sociedad, se desarrolló el presente proyecto; el cual tiene como objetivo implementar un modelo multimodal de Procesamiento de Lenguaje Nautral así como de imágenes para predecir si una publicación de la red social Instagram muestra indicios de depresión o no. El proyecto está inspirado en los siguientes papes:
1. https://arxiv.org/abs/1804.07000
2. https://arxiv.org/abs/1912.01131


## Ejecución

En este repositorio se proporcionan todos los archivos necesarios para reproducir el experimento en el ambiente. Existen dos Jupyter Notebooks, el primero '[InstagramScraper.ipynb](./InstagramScraper.ipynb)' sirve para generar la base de datos y el segundo '[DepressionDetection.ipynb](./DepressionDetection.ipynb)' en donde se crea el modelo de clasificación. El resto de los archivos son utilizados y/o generados por los mismos Notebooks.

Dentro de cada Notebook se proporciona una breve explicación de lo que se hace así como el detalle de cada sección de código y lo que hace.

Para correr el proyecto en Google Colab se debe cargar los dos Notebooks con todos los demás archivos que aquí se presentan, principalmente [requirements.txt](./requirements.txt)


## Funcionalidad

El proyecto está dividido en dos partes fundamentales: 

* La primera consiste en generar una base de datos multimodal que no solo tenga los textos, sino también las imágenes de las publicaciones que hacen los usuarios de alguna red social. En este caso, se eligió Instagram como la fuente de los datos. Sin embargo, esta plataforma no cuenta con una API, por lo que se implementaron técnicas de Web Scraping utilizando la herramienta Selenium para así poder generar la base de datos.

* La segunda parte consiste en llevar a cabo un Early-Fusion de los datos de tal manera que, previo a ser clasificados, se combinan los vectores de embedding de los textos con los vectores de features de sus respectivas imágenes, generando un nuevo bloque de fusión listo para ser procesado por nuestro modelo clasificador implementado con la API de Keras.

## Poster Académico

Pendiente


## Notas

