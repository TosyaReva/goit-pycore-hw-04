import pprint
from pathlib import Path

def get_cats_info(path: str) -> list[dict]:
    path_to_file = Path(__file__).parent / path
    cats = []

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                id,name,age = line.split(",")
                
                cats.append({"id": id, 'name': name, "age": age})
    except FileNotFoundError:
        print(f"File {path} not found")
    except Exception as error:
        print(error)

    return cats
    

cats_info = get_cats_info("assets/cats_file.txt")
pprint.pprint(cats_info)
