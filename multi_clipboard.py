
import sys
import clipboard
import json

def save_items(filepath, data):
    # Override file is it already exists, otherwise create it
    with open(filepath, "w") as f:
        # Dump json data to f (file)
        json.dump(data, f)

save_items("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == 'save': print('save')
    elif command == 'load': print('load')
    elif command == 'list': print('list')
    else: print('Unknown command')

else:
    print('Please pass exactly one command...(save/load/list)')
