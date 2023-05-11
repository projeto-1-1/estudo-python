def remover_elemento_no_indice_do_array(array, indice):
    """
    @param array: list
    @param indice: int

    Remove um elemento de [array] na posicao [indice]

    @return o array sem o elemento
    """
    

TEST_CASES = [
    {   "input": [["chloe", "mimi", "macaquinho", "urso"], 2],
        "expected": ["chloe", "mimi",  "urso"]
    },
    {   "input": [[0, 1, 2, 3, 4, 5], 4],
        "expected": [0, 1, 2, 3,5]
    },
    {   "input": [[0, 1, 2], -2],
        "expected": [0, 1, 2]
    },
    {   "input": [[0, 1, 2, 1, 2, 3], 2],
        "expected": [0, 1, 1, 2, 3]
    },
    {   "input": [[0, 1, 2, 1, 1], 3],
        "expected": [0, 1, 2, 1]
    },
    {   "input": [[], 3],
        "expected": []
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(remover_elemento_no_indice_do_array, TEST_CASES).run()