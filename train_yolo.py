from ultralytics import YOLO

def main():
    # Load a pretrained YOLOv8 segmentation model
    model = YOLO('yolov8n-seg.pt')
    
    # Train the model with the dataset configuration
    print("Starting YOLOv8 segmentation training...")
    # Using 50 epochs and imgsz 640 as a good default for the dataset
    results = model.train(
        data='data.yaml',
        epochs=50,
        imgsz=640
    )
    
    print("Training finished!")
    
if __name__ == '__main__':
    main()
