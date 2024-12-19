from datasets import load_dataset, Audio
from transformers import pipeline
import json
import os

def transcribir_audios(dataset_name, output_json):
    """
    Transcribe audios de un dataset y guarda las transcripciones en un archivo JSON.
    """
    # Cargar el dataset y convertir audios a un formato procesable
    print(f"Cargando dataset '{dataset_name}' desde Hugging Face...")
    dataset = load_dataset(dataset_name, split="train")
    dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))  # Normalizar a 16 kHz

    # Cargar el modelo de transcripción Whisper
    print("Cargando el modelo de transcripción Whisper...")
    transcriptor = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-base",
        return_timestamps=True
    )

    # Lista para almacenar las transcripciones
    transcripciones = []

    # Iterar sobre cada archivo de audio
    for index, row in enumerate(dataset):
        audio_path = row["audio"]["path"]
        print(f"Procesando archivo {index + 1}/{len(dataset)}: {audio_path}")

        try:
            # Transcribir el audio
            result = transcriptor(audio_path, generate_kwargs={"language": "<|es|>"})
            texto = result["text"]

            # Guardar la transcripción en la lista
            transcripciones.append({
                "audio_file": os.path.basename(audio_path),
                "transcription": texto
            })
        except Exception as e:
            # Manejar errores durante la transcripción
            print(f"Error al transcribir {audio_path}: {e}")
            transcripciones.append({
                "audio_file": os.path.basename(audio_path),
                "transcription": None,
                "error": str(e)
            })

    # Guardar las transcripciones en un archivo JSON
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(transcripciones, json_file, ensure_ascii=False, indent=4)
    print(f"Transcripciones guardadas en: {output_json}")

if __name__ == "__main__":
    # Parámetros del dataset y archivo de salida
    DATASET_NAME = "josearangos/spanish-calls-corpus-Friends"
    OUTPUT_JSON = "transcripciones.json"

    # Transcribir los audios y guardar los resultados
    transcribir_audios(DATASET_NAME, OUTPUT_JSON)