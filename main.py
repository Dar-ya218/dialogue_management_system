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

if __name__ == "__main__":
    main()