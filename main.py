import json

from json_initializer import initialize_json_if_needed

def main():

      # Inicializa el archivo JSON si no existe
    initialize_json_if_needed()
    
    # Main program loop
    while True:
        print("\n=== Dialogue Management System ===")
        print("1. Add new dialogue")
        print("2. View all dialogues")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == "1":
            person1_text = input("Enter Person 1's message: ")
            person2_text = input("Enter Person 2's message: ")
           # add_dialogue(person1_text, person2_text)
            print("Dialogue saved successfully!")

        elif choice == "2":
            dialogues = read_json_file()
            if dialogues["dialogues"]:
                print("\n=== Diálogos Guardados ===")
                for i, dialogue in enumerate(dialogues["dialogues"], 1):
                    print(f"\nDiálogo {i}:")
                    print(f"Persona 1: {dialogue['person1']}")
                    print(f"Persona 2: {dialogue['person2']}")
            else:
                print("\nNo se encontraron diálogos.")

if __name__ == "__main__":
    main()