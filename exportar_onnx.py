from ultralytics import YOLO
import os

def export_to_onnx():
    model_path = 'runs/segment/train/weights/best.pt'
    
    if not os.path.exists(model_path):
        print(f"Error: No se ha encontrado el modelo en {model_path}")
        print("Asegúrate de haber entrenado el modelo antes (train_yolo.py)")
        
        # Opcional: intentar con el modelo preentrenado base si "best.pt" no existe
        model_path = 'yolov8n-seg.pt'
        if os.path.exists(model_path):
            print(f"Intentando exportar el modelo base: {model_path} en su lugar...")
        else:
            return

    print(f"Cargando modelo YOLOv8 desde: {model_path}")
    model = YOLO(model_path)
    
    # Exportar el modelo a formato ONNX
    print("Exportando a formato ONNX para Unity (Unity Sentis/Barracuda u ONNX Runtime)...")
    success = model.export(format='onnx', opset=12) # opset=12 suele ser estable para Unity
    
    print(f"Resultado de la exportación: {success}")
    if success:
        print("¡El modelo .onnx se ha generado correctamente! Puedes importarlo en Unity.")

if __name__ == '__main__':
    export_to_onnx()
