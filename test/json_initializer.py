import os

from test.constants import JSON_FILE
from test.json_writer import write_json_file


def initialize_json_if_needed():
    # Comprueba si el archivo existe
    if not os.path.exists(JSON_FILE):
        # Si NO existe, crea la estructura inicial
        initial_data = {
            "dialogues": []
        }
        # Llama a write_json_file para crear físicamente el archivo
        write_json_file(initial_data)
