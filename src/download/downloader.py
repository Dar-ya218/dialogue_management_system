import requests
import os

def descargar_archivo(dataset_user, dataset_name, file_name, save_directory):
    """
    Descarga un archivo específico desde un dataset de Hugging Face y lo guarda localmente.
    """
    # Construcción de la URL para Hugging Face
    url = f"https://huggingface.co/datasets/{dataset_user}/{dataset_name}/resolve/main/{file_name}"
    save_path = os.path.join(save_directory, file_name)  # Ruta local donde se guardará el archivo

    try:
        print(f"Descargando desde: {url}")
        response = requests.get(url, stream=True)  # Solicitud GET con stream (para archivos grandes)
        if response.status_code == 200:
            # Guardar el archivo localmente
            with open(save_path, "wb") as archivo:
                for chunk in response.iter_content(chunk_size=1024):  # Descargar en partes de 1024 bytes
                    archivo.write(chunk)
            print(f"Archivo descargado exitosamente en: {save_path}")
        else:
            print(f"Error al descargar el archivo. Código: {response.status_code}")
    except Exception as e:
        print(f"Error durante la descarga: {e}")

if __name__ == "__main__":
    # Parámetros del dataset y archivo a descargar
    DATASET_USER = "josearangos"  # Usuario del dataset en Hugging Face
    DATASET_NAME = "spanish-calls-corpus-Friends"  # Nombre del dataset
    FILE_NAME = "sample_audio.mp3"  # Nombre del archivo específico dentro del dataset 
    
    # Directorio donde guardar el archivo
    SAVE_DIRECTORY = "data/audio"  # Carpeta local donde guardar el archivo
    os.makedirs(SAVE_DIRECTORY, exist_ok=True)  # Crear la carpeta si no existe

    # Llamar a la función para descargar el archivo
    descargar_archivo(DATASET_USER, DATASET_NAME, FILE_NAME, SAVE_DIRECTORY)
