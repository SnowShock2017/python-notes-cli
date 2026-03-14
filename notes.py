import json
import sys

FILE = "notes.json"

def load_notes():
    try: 
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
    
    
def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)
        
        
def add_note(note):
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Notes added!")
    
    
def list_notes():
    notes = load_notes()
    
    if not notes:
        print("No notes found.")
        return 
    
    for i , note in enumerate(notes):
        print(f"{i}: {note}")

def delete_note(index):
    notes = load_notes()
    
    try:
        removed = notes.pop(index)
        save_notes(notes)
        print(f"Deleted: {removed}")
        
    except:
        print("Invalid index")
        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ")
        print("python notes.py add 'note text'")
        print("python notes.py list")
        print("python notes.py delete index")
        sys.exit()
        
    command = sys.argv[1]

    if command == "add":
        add_note(sys.argv[2])

    elif command == "list":
        list_notes()

    elif command == "delete":
        delete_note(int(sys.argv[2]))
        
        