from datasets import load_dataset
import os
import shutil

DATASET_NAME = "josearangos/spanish-calls-corpus-Friends"
SAVE_DIRECTORY = "data/audio"

def descargar_dataset(dataset_name, save_directory):
    print(f"Cargando dataset '{dataset_name}' desde Hugging Face...")
    dataset = load_dataset(dataset_name)

    os.makedirs(save_directory, exist_ok=True)

    for index, row in enumerate(dataset["train"]):
        if "audio" in row:
            audio_path = row["audio"]["path"] 
            destination_path = os.path.join(save_directory, f"audio_{index}.mp3")
            
            shutil.copy(audio_path, destination_path)
            print(f"Archivo guardado: {destination_path}")
        else:
            print(f"No se encontró audio en la fila {index + 1}.")

if __name__ == "__main__":
    descargar_dataset(DATASET_NAME, SAVE_DIRECTORY)
