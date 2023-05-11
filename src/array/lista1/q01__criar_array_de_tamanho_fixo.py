def criar_array_de_tamanho_fixo(tamanho):
    """
    @param tamanho: int - tamanho do array a ser criado

    Cria um array com {tamanho} numero de elementos

    @return um array qualquer com {tamanho} numero de elementos
    """

def checa_se_array_de_tamanho(expected_size):
    from collections.abc import Sequence
    def matcher(result):
        if isinstance(result, Sequence) and len(result) == expected_size:
            return True
        return f"um array de tamanho {expected_size}"
    return matcher

TEST_CASES = [
    {
        "input": [6],
        "expected": checa_se_array_de_tamanho(6)
    },
    {   "input": [10],
        "expected": checa_se_array_de_tamanho(10)
    },
    {   "input": [5],
        "expected": checa_se_array_de_tamanho(5)
    },
    {   "input": [0],
        "expected": []
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(criar_array_de_tamanho_fixo, TEST_CASES).run()