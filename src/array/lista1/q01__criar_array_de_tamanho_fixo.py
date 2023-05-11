def criar_array_de_tamanho_fixo(tamanho):
    """
    @param tamanho: int - tamanho do array a ser criado

    Cria um array com {tamanho} numero de elementos

    @return um array qualquer com {tamanho} numero de elementos
    """
    

TEST_CASES = [
    {
        "input": (6),
        "expected": lambda arr = []: len(arr) == 6
    },
    {   "input": (10),
        "expected": lambda arr = []: len(arr) == 10
    },
    {   "input": (5),
        "expected": lambda arr = []: len(arr) == 5
    },
    {   "input": (0),
        "expected": []
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(criar_array_de_tamanho_fixo, TEST_CASES).run()