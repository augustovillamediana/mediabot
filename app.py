import requests
import sys
import os

def load_config(filename='config.txt'):
    config = {}
    with open(filename) as f:
        for line in f:
            name, value = line.strip().split('=')
            config[name] = value
    return config

def post_note_to_misskey(instance_url, api_token, note_text):
    url = f"{instance_url}/api/notes/create"
    payload = {
        "i": api_token,
        "text": note_text
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Note posted successfully!")
    else:
        print(f"Failed to post note: {response.status_code}, {response.text}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--note':
        print("Usage: startup.sh --note \"This is a test\"")
        return

    note_text = sys.argv[2]
    config = load_config()
    
    instance_url = config['MISSKEY_INSTANCE_URL']
    api_token = config['MISSKEY_API_TOKEN']
    
    post_note_to_misskey(instance_url, api_token, note_text)

if __name__ == "__main__":
    main()
