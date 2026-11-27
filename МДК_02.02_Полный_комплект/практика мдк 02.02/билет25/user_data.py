def make_user(name, age):
  
    if not isinstance(name, str) or not name.strip():
        raise ValueError("имя должно быть непустой строкой")
    if isinstance(age, bool) or not isinstance(age, int):
        raise ValueError("возраст должен быть целым числом")
    if not (0 <= age <= 120):
        raise ValueError("возраст должен быть от 0 до 120")

    return {"name": name.strip(), "age": age}