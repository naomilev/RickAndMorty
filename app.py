from flask import Flask, jsonify
import requests
import re

app = Flask(__name__)

def get_all_characters():
    characters = []
    page = 1
    while True:
        response = requests.get(f"https://rickandmortyapi.com/api/character?page={page}")
        data = response.json()
        characters.extend(data['results'])
        if data['info']['next'] is None:
            break
        page += 1
    return characters

def filter_characters(characters):
    earth_pattern = re.compile(r'^Earth', re.IGNORECASE)
    return [
        character for character in characters
        if character['species'] == 'Human' and
        character['status'] == 'Alive' and
        earth_pattern.match(character['origin']['name'])
    ]

def extract_info(characters):
    return [
        {
            'Name': character['name'],
            'Location': character['location']['name'],
            'Image': character['image']
        }
        for character in characters
    ]

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "healthy"}), 200

@app.route('/characters')
def get_characters():
    all_characters = get_all_characters()
    filtered_characters = filter_characters(all_characters)
    character_info = extract_info(filtered_characters)
    return jsonify(character_info), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
