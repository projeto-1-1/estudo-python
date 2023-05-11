def procura_caractere(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Checa se uma caractere(agulha) se encontra dentro de outra palavra (palheiro)

    @return bool
        - True se [agulha] existe dentro de [palheiro]
        - False se [agulha] nao existe dentro de [palheiro]
    """


TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", "a"),
        "expected": True
    },
    {   "input": ("marcela é uma gostosa", "u"),
        "expected": True
    },
    {   "input": ("marcela é uma gostosa", "x"),
        "expected": False
    },
    {   "input": ("marcela", "s"),
        "expected": False
    },
    {   "input": ("x_batata", "x"),
        "expected": True
    },
    {   "input": ("batata_x", "x"),
        "expected": True
    },
    {   "input": ("", "a"),
        "expected": False
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(procura_caractere, TEST_CASES).run()
