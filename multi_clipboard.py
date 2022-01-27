
import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

# Write JSON file
def save_data(filepath, data):
    # Override file is it already exists, otherwise create it
    with open(filepath, "w") as f:
        # Dump json data to f (file)
        json.dump(data, f)


# Read JSON file
def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == 'save': 
        key = input('Please enter a key to save: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data saved.\n')

    elif command == 'load': 
        key = input("Please enter key to load: ")

        if key in data:
            clipboard.copy(data[key])
            print('Data copied.\n')
        else:
            print('That key doesn\'t exist\n')

    elif command == 'list':
        for key, value in data.items():
            print(f'{key}: {value}')

    else: print('Unknown command\n')

else:
    print('Please pass exactly one command...(save/load/list)')


