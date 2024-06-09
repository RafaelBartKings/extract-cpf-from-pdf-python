import json

def save_cpfs_to_json(cpfs, json_path):
    with open(json_path, 'w') as json_file:
        json.dump(cpfs, json_file, indent=4)
