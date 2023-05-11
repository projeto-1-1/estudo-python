def criar_sequencia_de_tamanho_n_com_inicio(inicio, n):
    """
    @param inicio: int
    @param n: int

    Gera uma sequencia de tamanho [n]

    INFO: Uma sequencia é um array númerico começando do [inicio], e que cada valor é igual à: valor_anterior + 1

    @return sequencia de tamanho [n], começando em [inicio]
    """
    

TEST_CASES = [
    {
        "input": (0, 6),
        "expected": [0, 1, 2, 3, 4, 5]
    },
    {
        "input": (3, 6),
        "expected": [3, 4, 5, 6, 7, 8]
    },
    {   "input": (0, 3),
        "expected": [0, 1, 2]
    },
    {   "input": (5, 0),
        "expected": []
    },
    {   "input": (0, 0),
        "expected": []
    },
    {   "input": (3, 3),
        "expected": [3, 4, 5]
    },
    {   "input": (2, 10),
        "expected": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    }
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(criar_sequencia_de_tamanho_n_com_inicio, TEST_CASES).run()