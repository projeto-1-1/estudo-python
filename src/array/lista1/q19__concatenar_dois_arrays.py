def concatenar_dois_arrays(array1, array2):
    """
    @param array1: list
    @param array2: list

    Junta 2 arrays

    @return 
    """
    

TEST_CASES = [
    {
        "input": ([0, 1], [2, 3]),
        "expected": [0,1,2,3]
    },
    {   "input": ([0, 1, 2], []),
        "expected": [0, 1, 2]
    },
    {   "input": ([0, 1, 2], [0, 1, 2]),
        "expected": [0, 1, 2, 0, 1, 2]
    },
    {   "input": ([], [0, 1, 2]),
        "expected": [0, 1, 2]
    },
    {   "input": ([], []),
        "expected": []
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(concatenar_dois_arrays, TEST_CASES).run()