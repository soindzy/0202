from pathlib import Path
from helper import greeting

if __name__ == "__main__":
    print(greeting())
    print(Path(__file__).with_name(".gitignore").read_text(encoding="utf-8"))
