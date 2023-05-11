from src.helpers.chalk import chalk

def stringifyValue(value):
    if isinstance(value, str):
        return f"\"{value}\""
    return value

def is_last_index_in_array(index: int, array: list) -> bool:
    return index == (len(array)-1)

def pause(next):
    import sys
    import msvcrt as m
    print(f"Pressione ENTER para executar [{chalk.cyan(next)}]")
    if m.getch() in [b'q', b'\x03']:
        exit(1)
    sys.stdout.write("\033[F")
    print(" "*len(f"Pressione ENTER para executar [{next}]"))
    sys.stdout.write("\033[F")