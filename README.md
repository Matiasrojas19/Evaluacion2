# Evaluacion2 - CUY6142

Proyecto de la Evaluación Parcial N° 2 de Telepresencia y Entornos Innovadores de Colaboración Humana.

## Descripción

`graphhopper_parse-json_1.py` es un programa en Python que consulta la API de GraphHopper Directions y entrega la ruta entre un origen y un destino. Incluye estas mejoras:

- Interacción con el usuario en español.
- Distancia y duración con un máximo de dos decimales.
- Opción de salir escribiendo `s` o `salir`.
- Narrativa del viaje (instrucciones paso a paso) en español.

## Requisitos

- Python 3
- Librería `requests`
- Una API key de GraphHopper (https://www.graphhopper.com)

## Cómo ejecutarlo

1. Abra `graphhopper_parse-json_1.py` y reemplace `TU_API_KEY` por su API key.
2. Ejecute en la terminal: `python3 graphhopper_parse-json_1.py`
3. Ingrese el medio de transporte (auto, bici, a pie), el origen y el destino.
4. Escriba `s` o `salir` para terminar el programa.
