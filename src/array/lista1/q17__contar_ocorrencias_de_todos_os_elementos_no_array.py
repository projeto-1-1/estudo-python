def contar_ocorrencias_de_todos_os_elementos_no_array(array, elementos):
     """
    @param array: list
    @param elementos

    Retorna o número vezes que um elemento aparece dentro do array

    @return 
    """
    

TEST_CASES = [
    {   "input": [["chloe", "mimi", "mimi", "chloe", "urso"], ["chloe"]],
        "expected": [2]
    },
    {   "input": [["chloe", "mimi", "mimi", "chloe", "urso"], ["urso"]],
        "expected": [1]
    },
    {   "input": [["chloe", "mimi", "mimi", "chloe", "urso"], ["chloe", "urso"]],
        "expected": [2, 1]
    },
    {   "input": [[0, 1, 2, 3, 4, 5], [3]],
        "expected": [1]
    },
    {   "input": [[0, 1, 2], [4, 2]],
        "expected": [0, 1]
    },
    {   "input": [[0, 1, 2, 1, 1, 2, 3], [1, 2]],
        "expected": [3, 2]
    },
    {   "input": [[0, 1, 2, 1, 1, 2, 3], [2, 1]],
        "expected": [2, 3]
    },
    {   "input": [[0, 1, 2, 1, 1, 2, 3], [3, 0]],
        "expected": [1, 1]
    },
    {   "input": [[0, 1, 2, 1, 1], [0]],
        "expected": [1]
    },
    {   "input": [[], [2]],
        "expected": [0]
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(contar_ocorrencias_de_todos_os_elementos_no_array, TEST_CASES).run()