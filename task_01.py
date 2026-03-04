from pathlib import Path

def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            total = 0

            if len(lines) != 0:
                for line in lines:
                    _, money = line.strip().split(",")
                    total += int(money)

            average = total / len(lines)
            return (total, average)
    except FileNotFoundError:
        print(f"File {path} not found")
    except Exception as error:
        print(error)
    
    return (0, 0.0)

total, average = total_salary("assets/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
