"""Módulo para escribir en archivos JSON"""
import json

def write_json_file(data):
    """Escribe datos en el archivo JSON."""
    from constants import JSON_FILE
    
    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)