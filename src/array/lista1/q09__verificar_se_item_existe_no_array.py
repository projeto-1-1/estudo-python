def verificar_se_item_existe_no_array(array, elemento):
    """
    @param array: list
    @param elemento

    Checa se um elemento existe dentro do array, se sim, retorna True, do contrário, False

    @return True se o elemento existe dentro do array, do contrário, False
    """
    

TEST_CASES = [
    {   "input": ([0, 1, 2, 3, 4, 5], 4),
        "expected": True
    },
    {   "input": ([0, 1, 2, 3, 4, 5], "batata"),
        "expected": False
    },
    {   "input": ([0, 1, 2, "batata", 4, 5], "batata"),
        "expected": True
    },
    {   "input": (["chloe", "urso", "mimi"], "marcela"),
        "expected": False
    },
    {   "input": (["array", "de","cachorros"], "chloe"),
        "expected": False
    },
    {   "input": (["array", "de", "cachorros", "+", "chloe"], "chloe"),
        "expected": True
    },
    {   "input": ([], "qualquer coisa"),
        "expected": False
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(verificar_se_item_existe_no_array, TEST_CASES).run()