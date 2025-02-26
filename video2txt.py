import moviepy.editor as mp
import whisper
import os

def extract_audio(video_path, output_audio_path):
    """Extrae el audio de un video y lo guarda como archivo .wav"""
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')

def transcribe_audio(audio_path):
    """Transcribe el audio a texto usando Whisper."""
    model = whisper.load_model("base")  # Puedes cambiar el modelo a 'small', 'medium', 'large' según la calidad deseada
    result = model.transcribe(audio_path)
    return result["text"]

def save_transcription(text, output_text_path):
    """Guarda la transcripción en un archivo de texto."""
    with open(output_text_path, "w", encoding="utf-8") as file:
        file.write(text)

def process_video(video_path):
    """Procesa un video extrayendo el audio y transcribiéndolo a texto."""
    audio_path = "temp_audio.wav"
    text_path = "transcription.txt"
    
    print("Extrayendo audio...")
    extract_audio(video_path, audio_path)
    
    print("Transcribiendo audio...")
    transcription = transcribe_audio(audio_path)
    
    print("Guardando transcripción...")
    save_transcription(transcription, text_path)
    
    print(f"Transcripción guardada en {text_path}")
    
    # Opcional: Eliminar el archivo de audio temporal
    os.remove(audio_path)
    
    return text_path

# Uso
txt_file = process_video("video.mp4")  # Cambia "video.mp4" por el nombre de tu archivo

