def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line}")
                    continue

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except OSError:
        print("Помилка при роботі з файлом.")
        return []


if __name__ == "__main__":
    cats = get_cats_info("cats_file.txt")
    print(cats) 
