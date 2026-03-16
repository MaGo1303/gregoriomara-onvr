import cv2
import numpy as np
from ultralytics import YOLO

def process_video():
    print("Cargando modelo...")
    model = YOLO('runs/segment/train/weights/best.pt')

    video_path = 'WhatsApp Video 2026-03-12 at 09.20.13 (2).mp4'
    output_path = 'WhatsApp_contorno.mp4'
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"No se pudo abrir el vídeo: {video_path}")
        return

    # Configurar VideoWriter
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # mp4v para guardarlo como .mp4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print(f"Procesando video {video_path}...")
    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Inferencia
        results = model(frame, verbose=False)
        result = results[0]
        
        # Dibujar solo el contorno de la máscara si hay detecciones de hueso
        if result.masks is not None:
            for mask_xy, conf in zip(result.masks.xy, result.boxes.conf):
                # Convertir los puntos del polígono a enteros
                points = np.array(mask_xy, dtype=np.int32)
                
                # Dibujar contorno morado con grosor 3
                # BGR para morado en OpenCV es aprox (211, 0, 148) o (180, 50, 140)
                color = (255, 50, 150) # Un morado/rosa brillante
                cv2.polylines(frame, [points], isClosed=True, color=color, thickness=3)
                
                # Opcional: Dibujar la etiqueta "bones" cerca del primer punto
                if len(points) > 0:
                    text_x, text_y = points[0]
                    cv2.putText(frame, f"bones", (text_x, text_y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        out.write(frame)
        frame_count += 1
        if frame_count % 50 == 0:
            print(f"Frame {frame_count}/{total_frames} procesado...")

    cap.release()
    out.release()
    print(f"Vídeo guardado con éxito en: {output_path}")

if __name__ == '__main__':
    process_video()
