def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    _, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line}")
                    continue

        average = total / count if count > 0 else 0
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except OSError:
        print("Помилка при роботі з файлом.")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
