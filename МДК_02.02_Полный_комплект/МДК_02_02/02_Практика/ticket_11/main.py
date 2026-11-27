import tempfile
from conflict_demo import demonstrate

if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="ticket11_") as directory:
        result = demonstrate(directory)
        print("Конфликт до исправления:")
        print(result["conflict"])
        print("Согласованный результат:")
        print(result["result"])
        print(f"Рабочий каталог чист: {result['clean']}")
