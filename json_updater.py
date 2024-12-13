"""Módulo para actualizar archivos JSON"""
from json_reader import read_json_file
from json_writer import write_json_file

def update_json_file(dialogue_id, updated_data):
    """Actualiza un diálogo específico en el archivo JSON."""
    data = read_json_file()
    if 0 <= dialogue_id < len(data["dialogues"]):
        data["dialogues"][dialogue_id] = updated_data
        write_json_file(data)
        return True
    return False