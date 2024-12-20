from datasets import load_dataset
import os
import shutil

DATASET_NAME = "josearangos/spanish-calls-corpus-Friends"
SAVE_DIRECTORY = "escritorio/proyectos/dialogue_management_system/src/download"

def descargar_audio(dataset_name, save_directory, row_index=1):
    """
    Descarga un archivo de audio específico basado en el índice de fila.
    """
    print(f"Cargando dataset '{dataset_name}' desde Hugging Face...")
    dataset = load_dataset(dataset_name)

    os.makedirs(save_directory, exist_ok=True)

    row = dataset["train"][row_index]
    if "audio" in row:
        audio_path = row["audio"]["path"]  
        destination_path = os.path.join(save_directory, f"audio_{row_index}.mp3")
    
        shutil.copy(audio_path, destination_path)
        print(f"Archivo guardado: {destination_path}")
    else:
        print(f"No se encontró audio en la fila {row_index + 1}.")

if __name__ == "__main__":
    descargar_audio(DATASET_NAME, SAVE_DIRECTORY, row_index=1)
