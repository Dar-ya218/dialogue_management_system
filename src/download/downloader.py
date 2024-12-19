import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os

def transcribir_audio(audio_file, model_id="openai/whisper-large-v3-turbo"):
    """
    Transcribe un archivo de audio usando el modelo Whisper large-v3-turbo.
    """
    # Configuración del dispositivo (CPU o GPU)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # Cargar el modelo y el procesador
    print(f"Cargando el modelo {model_id}...")
    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True)
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)

    # Configurar el pipeline para transcripción
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
    )

    # Transcribir el archivo de audio
    print(f"Transcribiendo el archivo: {audio_file}...")
    result = pipe(audio_file)

    # Retornar la transcripción
    return result["text"]

if __name__ == "__main__":
    # Ruta relativa al archivo de audio dentro de la carpeta "download"
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio donde está transcriber.py
    audio_file = os.path.join(script_dir, "audio_1.mp3")  # Ruta relativa al archivo en la misma carpeta

    # Verificar si el archivo existe en la ubicación esperada
    if not os.path.exists(audio_file):
        print(f"Error: No se encontró el archivo de audio '{audio_file}' en el directorio esperado.")
    else:
        # Transcribir el audio
        transcripcion = transcribir_audio(audio_file)
        print("\nTranscripción:")
        print(transcripcion)
