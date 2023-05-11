def procura_string(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Checa se uma string(agulha) se encontra dentro de outra string (palheiro)

    @return bool
        - True se [agulha] existe dentro de [palheiro]
        - False se [agulha] nao existe dentro de [palheiro]
    """
    


TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", "uma"),
        "expected": True
    },
    {   "input": ("marcela é uma gostosa", "tosa"),
        "expected": True
    },
    {   "input": ("marcela é uma gostosa", "duas"),
        "expected": False
    },
    {   "input": ("marcela é uma gostosa", "gostosura"),
        "expected": False
    },
    {   "input": ("marcela", "pica"),
        "expected": False
    },
    {   "input": ("potato_x", "_x"),
        "expected": True
    },
    {   "input": ("x_potato", "x_"),
        "expected": True
    },
    {   "input": ("potato_x", "x"),
        "expected": True
    },
    {   "input": ("x_potato", "x"),
        "expected": True
    },
    {   "input": ("", "uma"),
        "expected": False
    }
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\..")
    from runner import RootTestCaseManager
    RootTestCaseManager(procura_string, TEST_CASES).run()
