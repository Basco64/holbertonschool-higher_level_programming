#!/usr/bin/python3

def serialize_and_save_to_file(data, filename):
    """serializes and saves the data"""
    import json
    import os

    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'w') as file:
        json_data = json.dumps(data)  # Renommé ici
        file.write(json_data)


def load_and_deserialize(filename):
    """load and deserialize the data"""
    import json

    with open(filename, 'r') as file:
        data = json.load(file)
    return data
