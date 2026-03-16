from moviepy import VideoFileClip

def convert_for_whatsapp():
    print("Convirtiendo vídeo para WhatsApp...")
    input_video = 'WhatsApp_contorno.mp4'
    output_video = 'WhatsApp_contorno_whatsapp.mp4'
    
    # Cargar el vídeo
    clip = VideoFileClip(input_video)
    
    # WhatsApp requiere codec h264 y audio aac para asegurar compatibilidad
    # bajamos un poco la calidad (bitrate) para que no ocupe demasiado
    clip.write_videofile(
        output_video, 
        codec='libx264', 
        audio_codec='aac', 
        temp_audiofile='temp-audio.m4a', 
        remove_temp=True,
        fps=clip.fps,
        logger=None # Desactiva el log de progreso para que sea más limpio en consola
    )
    
    print(f"¡Vídeo convertido con éxito! Guardado en: {output_video}")

if __name__ == '__main__':
    convert_for_whatsapp()
