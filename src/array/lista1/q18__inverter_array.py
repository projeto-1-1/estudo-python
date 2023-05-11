def inverter_array(array):
    """
    @param array: list

    Inverte a ordem dos elementos de um array

    @return 
    """
    

TEST_CASES = [
    {
        "input": [[0, 1, 2, 3, 4, 5]],
        "expected": [5, 4, 2, 3, 1]
    },
    {   "input": [[0, 1, 2]],
        "expected": [2, 1, 0]
    },
    {   "input": [[0, 1, 2, 1, 2, 3]],
        "expected": [3, 2, 1, 2, 1, 0]
    },
    {   "input": [[0, 1, 2, 1, 1]],
        "expected": [1, 1, 2, 1, 0]
    },
    {   "input": [[]],
        "expected": []
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(inverter_array, TEST_CASES).run()