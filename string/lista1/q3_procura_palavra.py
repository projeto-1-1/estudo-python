def procura_palavra(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Checa se uma palavra(agulha) se encontra dentro de outra palavra (palheiro)

    """


TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", "uma"),
        "expected": True
    },
    {   "input": ("marcela é uma gostosa", "uma gostosa"),
        "expected": True
    },
    {   "input": ("marcela é uma gostosa", "duas"),
        "expected": False
    },
    {   "input": ("marcela", "pica"),
        "expected": False
    },
    {   "input": ("", "uma"),
        "expected": False
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\..")
    from runner import RootTestCaseManager
    RootTestCaseManager(procura_palavra, TEST_CASES).run()
