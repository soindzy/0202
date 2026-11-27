from safe_access import get_element

if __name__ == "__main__":
    values = [10, 20, 30]
    for index in [1, 3, -1]:
        try:
            print(f"{values}, индекс {index} -> {get_element(values, index)}")
        except (TypeError, IndexError) as error:
            print(f"Индекс {index} -> Ошибка: {error}")
