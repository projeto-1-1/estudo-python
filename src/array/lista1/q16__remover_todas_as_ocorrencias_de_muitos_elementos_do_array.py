def remover_todas_as_ocorrencias_de_muitos_elementos_do_array(array, elementos):
    """
    @param array: list
    @param elementos: list

    Remove as ocorrencias de varios elementos de dentro do [array]

    @return o array sem os elementos
    """
    

TEST_CASES = [
    {   "input": (["a", "b", "c", "d"], ["c"]),
        "expected": ["a", "b",  "d"]
    },
    {   "input": (["a", "b", "c", "d"], ["c", "d"]),
        "expected": ["a", "b"]
    },
    {   "input": (["a", "a"], ["a"]),
        "expected": []
    },
    {   "input": (["a", "a", "a", "b", "b", "b", "c"], ["a", "b"]),
        "expected": ["c"]
    },
    {   "input": (["chloe", "mimi", "macaquinho", "urso", "chloe"], ["macaquinho"]),
        "expected": ["chloe", "mimi",  "urso", "chloe"]
    },
    {   "input": (["chloe", "mimi", "macaquinho", "urso", "chloe"], ["chloe", "macaquinho"]),
        "expected": ["mimi", "urso"]
    },
    {   "input": (["chloe", "mimi", "macaquinho", "urso", "chloe"], ["chloe", "chipamzé"]),
        "expected": [ "mimi", "macaquinho", "urso" ]
    },
    {   "input": ([], [3]),
        "expected": []
    },
    {   "input": ([0, 1, 2, 3, 4, 5], [4, 5]),
        "expected": [0, 1, 2, 3]
    },
    {   "input": ([0, 1, 2], [0 , 1, 2]),
        "expected": []
    },
    {   "input": ([0, 1, 2, 1, 2, 3], [2,3]),
        "expected": [0, 1, 1]
    },
    {   "input": ([0, 1, 2, 1, 1], [1,2]),
        "expected": [0]
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(remover_todas_as_ocorrencias_de_muitos_elementos_do_array, TEST_CASES).run()