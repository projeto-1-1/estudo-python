def criar_sequencia_de_tamanho_n(n):
    """
    @param n: int

    Gera uma sequencia de tamanho [n]

    INFO: Uma sequencia é um array númerico começando do 0, e que cada valor é igual à: valor_anterior + 1

    @return sequencia de tamanho [n]
    """
    

TEST_CASES = [
    {
        "input": [6],
        "expected": [0, 1, 2, 3, 4, 5]
    },
    {   "input": [3],
        "expected": [0, 1, 2]
    },
    {   "input": [0],
        "expected": []
    },
    {   "input": [10],
        "expected": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(criar_sequencia_de_tamanho_n, TEST_CASES).run()