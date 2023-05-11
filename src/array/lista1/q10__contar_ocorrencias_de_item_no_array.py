def contar_ocorrencias_de_item_no_array(array, elemento):
    """
    @param array: list
    @param elemento

    Retorna o número vezes que um elemento aparece dentro do array

    @return 
    """
    

TEST_CASES = [
    {
        "input": ([0, 1, 2, 3, 4, 5], 3),
        "expected": 1
    },
    {   "input": ([0, 1, 2], 4),
        "expected": 0
    },
    {   "input": ([0, 1, 2, 1, 1, 2, 3], 1),
        "expected": 3
    },
    {   "input": ([0, 1, 2, 1, 1, 2, 3], 2),
        "expected": 2
    },
    {   "input": ([0, 1, 2, 1, 1, 2, 3], 3),
        "expected": 1
    },
    {   "input": ([0, 1, 2, 1, 1], 0),
        "expected": 1
    },
    {   "input": ([], 2),
        "expected": 0
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(contar_ocorrencias_de_item_no_array, TEST_CASES).run()