def busca_indice_caractere(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Procura um caractere(agulha) dentro de uma palavra (palheiro) e retorna a posição do primeiro
    encontro desse caractere dentro da palavra

     @return [int]
        - Se [agulha] existe dentro de [palheiro]: 
            retorna o indice do primeiro caractere igual a agulha dentro da palavra
        - Se [agulha] não existe dentro de [palheiro]: -1
    """
    

TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", "a"),
        "expected": 1
    },
    {   "input": ("marcela é uma gostosa", "u"),
        "expected": 10
    },
    {   "input": ("marcela é uma gostosa", "x"),
        "expected": -1
    },
    {   "input": ("marcela", "s"),
        "expected": -1
    },
    {   "input": ("", "a"),
        "expected": -1
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(busca_indice_caractere, TEST_CASES).run()
