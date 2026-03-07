import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)


def print_directory_structure(path, indent=""):
    try:
        for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Немає доступу до директорії: {path}{Style.RESET_ALL}")


def main():
    if len(sys.argv) != 2:
        print("Використання: python task3.py /шлях/до/директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print("Помилка: вказаний шлях не існує.")
        return

    if not path.is_dir():
        print("Помилка: вказаний шлях не є директорією.")
        return

    print(f"{Fore.YELLOW}{path.name}{Style.RESET_ALL}")
    print_directory_structure(path)


if __name__ == "__main__":
    main()
