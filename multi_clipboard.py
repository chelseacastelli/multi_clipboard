
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
        key = input('Please enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)

    elif command == 'load': 
        print('load')

    elif command == 'list': 
        pass

    else: print('Unknown command')

else:
    print('Please pass exactly one command...(save/load/list)')
