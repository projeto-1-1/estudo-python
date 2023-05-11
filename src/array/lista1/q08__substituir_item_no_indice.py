def substituir_item_no_indice(array, indice, valor):
    """
    @param array: list
    @param indice: int
    @param valor

    Altera o valor de um elemento do array na posicao [indice]
    Se o indice não existir dentro do array, não modificar nada

    @return array modificado
    """
    

TEST_CASES = [
    {
        "input": ([0, 1, 2, 3, 4, 5], 0, "yeye"),
        "expected": ["yeye", 1, 2, 3, 4, 5]
    },
    {   "input": ([0, 1, 2], 2, "totosa"),
        "expected": [0, 1, "totosa"]
    },
    {   "input": (["x"], 100, "y"),
        "expected": ["x"]
    },
    {   "input": ([], 0, "x"),
        "expected": []
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(substituir_item_no_indice, TEST_CASES).run()