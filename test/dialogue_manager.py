"""Módulo para gestionar los diálogos"""
from test.json_reader import read_json_file
from test.json_writer import write_json_file

def add_dialogue(person1_text, person2_text):
    """Añade un nuevo diálogo al archivo JSON."""
    data = read_json_file()
    
    new_dialogue = {
        "person1": person1_text,
        "person2": person2_text
    }
    
    data["dialogues"].append(new_dialogue)
    write_json_file(data)