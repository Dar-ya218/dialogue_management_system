import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os
import json

def transcribir_audio(audio_file, model_id="openai/whisper-large-v3-turbo", output_json_path="transcription.json"):
    """
    Transcribe un archivo de audio y guarda las palabras en un archivo JSON.
    """
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print(f"Cargando el modelo {model_id}...")
    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True)
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,       
        tokenizer=processor.tokenizer, 
        feature_extractor=processor.feature_extractor, 
        torch_dtype=torch_dtype, 
        device=device,          
        return_timestamps=True 
    )

    print(f"Transcribiendo el archivo: {audio_file}...")
    result = pipe(audio_file)

    transcription_text = result["text"]
    transcription_data = {
        "audio_file": os.path.basename(audio_file),
        "transcription": transcription_text
    }

    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(transcription_data, json_file, ensure_ascii=False, indent=4)

    print(f"Transcripción guardada en: {output_json_path}")

if __name__ == "__main__":
    audio_file = "/home/dasha/Escritorio/Proyectos/dialogue_management_system/src/download/audio_1.mp3"
    output_json_path = "/home/dasha/Escritorio/Proyectos/dialogue_management_system/src/download/transcription.json"

    transcribir_audio(audio_file, model_id="openai/whisper-large-v3-turbo", output_json_path=output_json_path)
