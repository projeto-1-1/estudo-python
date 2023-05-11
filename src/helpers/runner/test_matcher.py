from collections.abc import Sequence
from typing import Union


def is_array_like(value):
    return isinstance(value, Sequence)

def is_function(value):
    return callable(value)

def is_primitive(obj):
    return not hasattr(obj, '__dict__')

def compare_primitive(expected, v2) -> bool:
    return expected == v2

def compare_dict(expected, v2):
    raise Exception("Comparing dicts is not implemented")

def compare_array(expected: Sequence, v2) -> bool:
    if not is_array_like(v2):
        return False
    if len(expected) != len(v2):
        return False
    for i in range(0, len(expected)):
        return compare(expected[i], v2[i])
    return True

def compare(expected, v2) -> bool:
    if is_primitive(expected):
        return compare_primitive(expected, v2)
    if is_array_like(expected):
        return compare_array(expected, v2)
    if isinstance(expected, dict):
        return compare_dict(expected, v2)
    raise Exception(f"matcher not implemented for {expected}")

def root_compare(expected, v2) -> Union[str, bool]:
    if is_function(expected):
        return expected(v2) 
    return compare(expected, v2)
    
class TestMatcher:
    def __init__(self, expected):
        self.expected = expected
        self.is_valid = None
        self.message = expected
    
    def compare(self, value) -> Union[str, bool]:
        result = root_compare(self.expected, value)
        self.is_valid = result == True
        if isinstance(result, str):
            self.message = result

        return self.is_valid
        