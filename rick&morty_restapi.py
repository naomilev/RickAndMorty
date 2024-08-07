import requests
import csv

def fetch_characters():
    url = "https://rickandmortyapi.com/api/character/"
    characters = []
    page = 1
    
    while True:
        print(f"Fetching page {page}...")
        response = requests.get(f"{url}?page={page}")
        data = response.json()
        
        if 'results' not in data:
            print("No 'results' key found in the response.")
            break
        
        print(f"Page {page} results: {len(data['results'])} characters found.")
        
        for character in data['results']:
            # Debugging information
            print(f"Processing character: {character['name']}")
            
            if (character['species'] == "Human" and
                character['status'] == "Alive" and
                character['origin']['name'] == "Earth"):
                
                characters.append({
                    "Name": character['name'],
                    "Location": character['location']['name'],
                    "Image": character['image']
                })
            else:
                print(f"Character {character['name']} does not meet the criteria.")
        
        if data['info']['next'] is None:
            print("No more pages available.")
            break
        
        page += 1
    
    return characters

def write_to_csv(characters):
    with open('rick_and_morty_characters.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Location", "Image"])
        writer.writeheader()
        writer.writerows(characters)
    print(f"Results written to rick_and_morty_characters.csv.")

def main():
    characters = fetch_characters()
    
    if not characters:
        print("No characters found that meet the criteria.")
    else:
        write_to_csv(characters)
        print(f"Found {len(characters)} characters.")

if __name__ == "__main__":
    main()
