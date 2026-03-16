# YOLOv8 Bone Segmentation Project

Este proyecto entrena y utiliza un modelo de segmentación basado en **YOLOv8** para detectar y dibujar los contornos de los huesos en vídeos.

## Archivos del Proyecto

El repositorio contiene los siguientes scripts principales:

- `train_yolo.py`: Script para entrenar el modelo de segmentación de YOLOv8 usando las imágenes del dataset (configuradas en `data.yaml`).
- `dibujar_contorno.py`: Toma un vídeo de entrada y aplica el modelo previamente entrenado (`runs/segment/train/weights/best.pt`) para detectar huesos fotograma a fotograma, dibujando un contorno de color morado/rosa.
- `convertir_whatsapp.py`: Toma el vídeo de salida de las detecciones y lo codifica usando `h264` y audio `aac` para que sea totalmente compatible si se desea enviar por WhatsApp.

## Requisitos

Asegúrate de tener instalado Python 3 y crear un entorno virtual (opcional pero recomendado). Instala los requisitos con:

```bash
pip install -r requirements.txt
```

*(Esto instalará `ultralytics`, `opencv-python`, `numpy` y `moviepy`)*

## Uso

1. **Entrenamiento**:
   Si necesitas reentrenar el modelo con tu dataset, simplemente ejecuta:
   ```bash
   python train_yolo.py
   ```
   Esto generará una carpeta `runs/` con los pesos del modelo resultante.

2. **Inferencia en vídeo**:
   Asegúrate de tener un vídeo de entrada (por defecto `WhatsApp Video 2026-03-12 at 09.20.13 (2).mp4`) y el modelo entrenado, luego ejecuta:
   ```bash
   python dibujar_contorno.py
   ```
   El vídeo de salida se llamará `WhatsApp_contorno.mp4`.

3. **Conversión para WhatsApp**:
   Si deseas enviar el archivo por WhatsApp y asegurarte de que se reproduzca correctamente, convierte el vídeo procesado usando:
   ```bash
   python convertir_whatsapp.py
   ```
   Generará un vídeo final llamado `WhatsApp_contorno_whatsapp.mp4`.

## Notas para GitHub

Se incluye un archivo `.gitignore` para evitar subir:
- El entorno virtual (`venv/`)
- Los vídeos y audios (`*.mp4`, `*.m4a`) que suelen ser archivos muy pesados.
- Las imágenes del dataset (`train/`, `valid/`, `test/`).
- Los pesos del modelo (`*.pt`) por su peso.

*Si quieres incluir los pesos del modelo en GitHub pese a su tamaño o modificar los archivos que se ignoran, asegúrate de editar el archivo `.gitignore`.*
