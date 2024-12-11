"""Módulo para leer archivos JSON"""
import json

def read_json_file():
    """Lee y retorna el contenido del archivo JSON."""
    from constants import JSON_FILE
    
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"dialogues": []}