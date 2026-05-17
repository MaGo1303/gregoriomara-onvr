# YOLOv8 Bone Segmentation

## Descripcion

Sistema de segmentacion de huesos en video basado en YOLOv8 (Ultralytics). Entrena un modelo de segmentacion sobre un dataset etiquetado y aplica inferencia para dibujar contornos oseos en tiempo real sobre fotogramas de video. Incluye conversion a formato compatible con WhatsApp.

## Stack Tecnologico

| Tecnologia | Uso |
|-----------|-----|
| **Python 3** | Lenguaje principal |
| **Ultralytics YOLOv8** | Modelo de segmentacion |
| **OpenCV** | Procesamiento de video e imagen |
| **NumPy** | Operaciones matriciales |
| **MoviePy** | Conversion y codificacion de video |

## Scripts

| Script | Funcion |
|--------|---------|
| `train_yolo.py` | Entrena el modelo de segmentacion con el dataset |
| `dibujar_contorno.py` | Aplica el modelo entrenado a un video y dibuja contornos |
| `convertir_whatsapp.py` | Codifica el video final (h264 + aac) para WhatsApp |

## Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Entrenar modelo
python train_yolo.py

# Inferencia sobre video
python dibujar_contorno.py

# Convertir para WhatsApp
python convertir_whatsapp.py
```

## Dataset

El dataset se estructura en las carpetas `train/`, `valid/` y `test/` con imagenes etiquetadas para segmentacion osea. Configuracion en `data.yaml`.

## Requisitos

- Python 3.8+
- GPU recomendada para entrenamiento (CPU funciona para inferencia)
- Webcam o videos de entrada