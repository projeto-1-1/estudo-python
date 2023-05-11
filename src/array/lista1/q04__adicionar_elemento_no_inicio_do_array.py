def adicionar_elemento_no_inicio_do_array(array, elemento):
    """
    @param array: list
    @param elemento

    Insere o elemento no inicio do array

    @return array modificado
    """
    

TEST_CASES = [
    {
        "input": ([0, 1, 2], 2),
        "expected": [2, 0, 1, 2]
    },
    {   "input": ([0, 1, 2], "batata"),
        "expected": ["batata", 0, 1, 2]
    },
    {    "input": ([0, 1, 2], None),
        "expected": [None, 0, 1, 2]
    },
    {   "input": ([], "marcela"),
        "expected": ["marcela"]
    },
    {   "input": ([], ""),
        "expected": [""]
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(adicionar_elemento_no_inicio_do_array, TEST_CASES).run()