
from pathlib import Path
import json

__all__ = ["test1", "test1_b", "load_data"]

# Créer des chemins vers les bases de données
BACKEND = Path(__file__).parent.parent.parent
DATA = BACKEND / "data"
USERS_DATA = DATA / "users.json"

def load_data(tablename):
    if tablename == "users":
        with USERS_DATA.open() as f:
            data_dico = json.load(f) 
    return data_dico
    

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