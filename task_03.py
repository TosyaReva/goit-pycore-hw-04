import sys
from pathlib import Path
from colorama import Fore, Style


def rec_folders(path_original: Path, padding = ""):
    try:
        for path in path_original.iterdir():
            if path.exists():
                if path.is_file():
                    print(Fore.GREEN + padding + path.name)
                else:
                    print(Fore.CYAN + padding +  path.name + "/")
                    rec_folders(path, padding + "    ")
    except Exception as error:
        print(error)
         

def main(): 

    if len(sys.argv) < 2:
            print(Fore.YELLOW + "Please write path")
            return
    
    path = Path(sys.argv[1])

    if not path.exists():
         print(Fore.RED + "Path is not existed")
         return
    elif not path.is_dir():
         print(Fore.RED + "Path is not a folder")
         return
    
    print(Fore.LIGHTMAGENTA_EX + path.name + "/")
    rec_folders(path, "    ")
    print(Style.RESET_ALL)

if __name__ == "__main__":
     main()
