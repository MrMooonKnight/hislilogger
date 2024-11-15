import os
import json
import time

def process_history():
    # Define the possible history files (excluding generic 'history')
    history_files = [".bash_history", ".zsh_history"]
    history_file = next((os.path.join(os.path.expanduser(""), f) for f in history_files if os.path.exists(os.path.join(os.path.expanduser(""), f))), None)

    if history_file:
        # Extract the basename without the leading dot and print the found message
        history_name = os.path.basename(history_file).lstrip(".")
        print(f"{history_name} found")
        
        # Read commands, reverse the list, and store in JSON format
        with open(history_file, "r", errors='ignore') as file:
            commands = [cmd.strip() for cmd in file][::-1]
        
        # Create output directory and JSON filename
        output_dir = os.path.join("data", f"{history_name.split('_')[0]}_history")
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"{time.strftime('%Y-%m-%d_%H-%M-%S')}_{history_name}.json")
        
        # Write commands to JSON file
        with open(filename, "w") as output_file:
            json.dump({"commands": commands}, output_file, indent=4)
        
        print(f"Commands have been saved to {filename}")
        
        # Show menu after saving the file
        show_menu(filename)
    else:
        print("No history file found")

def show_menu(filename):
    while True:
        print("\nMenu:")
        print("1. Display JSON contents")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_json(filename)
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def display_json(filename):
    # Read and display JSON file contents
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            commands = data.get("commands", [])
            print("\nCommand History:")
            for cmd in commands:
                print(cmd)
    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")

# Run the script
if __name__ == "__main__":
    process_history()