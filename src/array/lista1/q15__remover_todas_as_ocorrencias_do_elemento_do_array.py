def remover_todas_as_ocorrencias_do_elemento_do_array(array, elemento):
    """
    @param array: list
    @param elemento

    Remove todas as ocorrencias de um elemento de [array]

    @return o array sem o elemento
    """
    

TEST_CASES = [
    {   "input": (["a", "b", "c", "d"], "c"),
        "expected": ["a", "b",  "d"]
    },
    {   "input": (["a", "a"], "a"),
        "expected": []
    },
    {   "input": (["chloe", "mimi", "macaquinho", "urso", "chloe"], "macaquinho"),
        "expected": ["chloe", "mimi",  "urso", "chloe"]
    },
    {   "input": (["chloe", "mimi", "macaquinho", "urso", "chloe"], "chloe"),
        "expected": ["mimi", "macaquinho", "urso"]
    },
    {   "input": (["chloe", "mimi", "macaquinho", "urso", "chloe"], "chipamzé"),
        "expected": ["chloe", "mimi", "macaquinho", "urso", "chloe"]
    },
    {   "input": ([], 3),
        "expected": []
    },
    {   "input": ([0, 1, 2, 3, 4, 5], 4),
        "expected": [0, 1, 2, 3,5]
    },
    {   "input": ([0, 1, 2], 1),
        "expected": [0, 2]
    },
    {   "input": ([0, 1, 2, 1, 2, 3], 2),
        "expected": [0, 1, 1,  3]
    },
    {   "input": ([0, 1, 2, 1, 1], 1),
        "expected": [0, 2]
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(remover_todas_as_ocorrencias_do_elemento_do_array, TEST_CASES).run()