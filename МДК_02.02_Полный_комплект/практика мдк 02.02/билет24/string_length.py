def length(value):
  
    if not isinstance(value, str):
        raise TypeError(f"ожидалась строка, получено {type(value).__name__}")
    return len(value)

def length_stripped(value):

    if not isinstance(value, str):
        raise TypeError(f"ожидалась строка, получено {type(value).__name__}")
    return len(value.strip())