import tempfile
from repository_demo import demonstrate

if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="ticket09_") as directory:
        print(demonstrate(directory))
    print("Учебный временный репозиторий удалён автоматически.")
