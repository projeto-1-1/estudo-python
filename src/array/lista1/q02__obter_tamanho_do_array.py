def obter_tamanho_do_array(array):
    """
    @param array: list

    Retorna o tamanho do array

    @return o tamanho do array
    """
    

TEST_CASES = [
    {
        "input": [[0, 1, 2, 3, 4, 5]],
        "expected": 6
    },
    {   "input": [[0, 1, 2]],
        "expected": 3
    },
    {   "input": [[0, 1, 2, 1, 2, 3]],
        "expected": 6
    },
    {   "input": [[0, 1, 2, 1, 1]],
        "expected": 5
    },
    {   "input": [[]],
        "expected": 0
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(obter_tamanho_do_array, TEST_CASES).run()