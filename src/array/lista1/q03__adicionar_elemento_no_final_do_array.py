def adicionar_elemento_no_final_do_array(array, elemento):
    """
    @param array: list
    @param elemento

    Insere o elemento no final do array

    @return array modificado
    """
    

TEST_CASES = [
    {
        "input": ([0, 1, 2], 2),
        "expected": [0, 1, 2, 2]
    },
    {   "input": ([0, 1, 2], "batata"),
        "expected": [0, 1, 2, "batata"]
    },
    {    "input": ([0, 1, 2], None),
        "expected": [0, 1, 2, None]
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
    RootTestCaseManager(adicionar_elemento_no_final_do_array, TEST_CASES).run()