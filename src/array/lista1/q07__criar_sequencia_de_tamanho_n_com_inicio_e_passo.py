def criar_sequencia_de_tamanho_n_com_inicio_e_passo(inicio, n, passo):
    """
    @param inicio: int
    @param n: int
    @param passo: int

    Gera uma sequencia de tamanho [n]

    INFO: Uma sequencia é um array númerico começando do [inicio], e que cada valor é igual à: valor_anterior + [passo]

    @return sequencia de tamanho [n], começando em [inicio], e com passo de [passo]
    """
    

TEST_CASES = [
    {
        "input": (0, 5, 1),
        "expected": [0, 1, 2, 3, 4]
    },
    {
        "input": (0, 5, 2),
        "expected": [0, 2, 4, 6, 8]
    },
    {
        "input": (0, 5, 5),
        "expected": [0, 5, 10, 15, 20]
    },
    {
        "input": (3, 5, 2),
        "expected": [3, 5, 7, 9, 11]
    },
    {
        "input": (0, 6, 1),
        "expected": [0, 1, 2, 3, 4, 5]
    },
    {
        "input": (0, 6, 0),
        "expected": [0, 0, 0, 0, 0, 0]
    },
    {
        "input": (5, 6, 0),
        "expected": [5, 5, 5, 5, 5, 5]
    },
    {
        "input": (3, 6, 2),
        "expected": [3, 4, 5, 6, 7, 8]
    }
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(criar_sequencia_de_tamanho_n_com_inicio_e_passo, TEST_CASES).run()