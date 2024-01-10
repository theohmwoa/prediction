import requests

def get_data():
    classes_url = 'https://raw.githubusercontent.com/googlecreativelab/quickdraw-dataset/master/categories.txt'

    response = requests.get(classes_url)

    if response.status_code == 200:
        return response.content.decode('utf-8').splitlines()
    else:
        print(f"Failed to fetch classes list. Status code: {response.status_code}")

classes = get_data()

