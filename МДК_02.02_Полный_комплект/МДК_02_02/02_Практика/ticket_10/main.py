import tempfile
from branch_demo import demonstrate

if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="ticket10_") as directory:
        print(demonstrate(directory))
