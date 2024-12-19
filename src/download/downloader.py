from datasets import load_dataset
import os
import shutil

def descargar_dataset(dataset_name, save_directory):
    """
    Descarga un dataset completo desde Hugging Face y guarda los archivos localmente.
    """
    # Cargar el dataset
    print(f"Cargando dataset '{dataset_name}' desde Hugging Face...")
    dataset = load_dataset(dataset_name)

    # Mostrar los splits disponibles
    print("Splits disponibles en el dataset:")
    print(dataset)

    # Crear directorio de destino si no existe
    os.makedirs(save_directory, exist_ok=True)

    # Iterar sobre cada fila y guardar los archivos de audio
    for index, row in enumerate(dataset["train"]):  # Cambia "train" si el split es diferente
        if "audio" in row:
            audio_path = row["audio"]["path"]  # Ruta al archivo de audio local
            destination_path = os.path.join(save_directory, f"audio_{index}.mp3")
            
            # Copiar el archivo al directorio de destino
            shutil.copy(audio_path, destination_path)
            print(f"Archivo guardado: {destination_path}")
        else:
            print(f"No se encontró audio en la fila {index + 1}.")

if __name__ == "__main__":
    # Nombre del dataset en Hugging Face
    DATASET_NAME = "josearangos/spanish-calls-corpus-Friends"
    
    # Directorio donde guardar los archivos
    SAVE_DIRECTORY = "data/audio"

     # Crear la carpeta si no existe
    os.makedirs(SAVE_DIRECTORY, exist_ok=True)
    print(f"Guardando archivos en: {os.path.abspath(SAVE_DIRECTORY)}")
    
    # Descargar el dataset
    descargar_dataset(DATASET_NAME, SAVE_DIRECTORY)
