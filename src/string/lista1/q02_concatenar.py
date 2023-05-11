def concatenar_string(string_a, string_b):
    """
    @param string_a: str
    @param string_b: str

    Junta 2 strings

    @return str as string concatenadas
    """

TEST_CASES = [
    {
        "input": ("batata", "-frita"),
        "expected": "batata-frita"
    },
    {   "input": ("a", "b"),
        "expected": "ab"
    },
    {   "input": ("a", ""),
        "expected": "a"
    },
    {   "input": ("", "b"),
        "expected": "b"
    },
    {   "input": ("R$", "2.80"),
        "expected": "R$2.80"
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(concatenar_string, TEST_CASES).run()