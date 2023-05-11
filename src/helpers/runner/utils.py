from collections.abc import Sequence
from src.helpers.chalk import chalk

def compare(v1, v2, depth = 0):
    if v1 is None:
        return v2 is None
    if isinstance(v1, str):
        return v1 == v2
    if isinstance(v1, Sequence):
        if not isinstance(v2, Sequence):
            return False
        if len(v1) != len(v2):
            return False
        for i in range(0, len(v1)):
            return compare(v1[i], v2[i], depth + 1)
        return True
    return v1 == v2

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