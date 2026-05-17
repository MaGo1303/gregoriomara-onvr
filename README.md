# YOLOv8 Bone Segmentation

## ðŸ¦´ DescripciÃ³n

Sistema de segmentaciÃ³n de huesos en vÃ­deo basado en **YOLOv8 (Ultralytics)**. Entrena un modelo de segmentaciÃ³n sobre un dataset etiquetado y aplica inferencia para dibujar contornos Ã³seos en tiempo real sobre fotogramas de vÃ­deo. Incluye conversiÃ³n a formato compatible con WhatsApp.

## ðŸš€ Stack TecnolÃ³gico

| TecnologÃ­a | Uso |
|-----------|-----|
| **Python 3** | Lenguaje principal |
| **Ultralytics YOLOv8** | Modelo de segmentaciÃ³n |
| **OpenCV** | Procesamiento de vÃ­deo e imagen |
| **NumPy** | Operaciones matriciales |
| **MoviePy** | ConversiÃ³n y codificaciÃ³n de vÃ­deo |

## ðŸ“ Scripts

| Script | FunciÃ³n |
|--------|---------|
| `train_yolo.py` | Entrena el modelo de segmentaciÃ³n con el dataset |
| `dibujar_contorno.py` | Aplica el modelo entrenado a un vÃ­deo y dibuja contornos |
| `convertir_whatsapp.py` | Codifica el vÃ­deo final (h264 + aac) para WhatsApp |

## ðŸ› ï¸ Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Entrenar modelo
python train_yolo.py

# Inferencia sobre vÃ­deo
python dibujar_contorno.py

# Convertir para WhatsApp
python convertir_whatsapp.py
```

## ðŸ“¦ Dataset

El dataset se estructura en las carpetas `train/`, `valid/` y `test/` con imÃ¡genes etiquetadas para segmentaciÃ³n Ã³sea. ConfiguraciÃ³n en `data.yaml`.

## ðŸ“Œ Aplicaciones

Esta tecnologÃ­a tiene aplicaciÃ³n directa en:
- **Medicina deportiva** â€” anÃ¡lisis de movimiento y biomecÃ¡nica
- **InvestigaciÃ³n anatÃ³mica** â€” estudio de estructuras Ã³seas
- **EducaciÃ³n** â€” visualizaciÃ³n interactiva del sistema esquelÃ©tico

## âš™ï¸ Requisitos

- Python 3.8+
- GPU recomendada para entrenamiento (CPU funciona para inferencia)
- Webcam o vÃ­deos de entrada
