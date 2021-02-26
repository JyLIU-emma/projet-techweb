
from pathlib import Path
import json

__all__ = ["test1", "test1_b", "load_data", "dict_to_json"]

# Créer des chemins vers les bases de données
BACKEND = Path(__file__).parent.parent.parent
DATA = BACKEND / "data"
USERS_DATA = DATA / "users.json"
ADMINS_DATA = DATA / "admins.json"

def load_data(tablename):
    if tablename == "users":
        with USERS_DATA.open() as f:
            data_dico = json.load(f)
    elif tablename == "admins":
        with ADMINS_DATA.open() as f:
            if f.read() == '':
                data_dico = {}
            else:
                data_dico = json.load(f)
    return data_dico

def dict_to_json(dico, filename):
    json_str = json.dumps(dico, indent=4)
    if filename == "admins":
        filepath = ADMINS_DATA
    else:
        filepath = DATA / f"{filename}.json"

    with filepath.open(mode="w") as jsonfile:
        jsonfile.write(json_str)

    

def test1():
    print("Print all the users in the browser")

def test1_b():
    print("this is test1_b in utils.py")


def main():
    users_dico = load_data("users")
    for key in users_dico:
        print(key)

if __name__ == "__main__":
    main()