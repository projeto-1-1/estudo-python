def remove_caractere(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Checa se uma palavra(agulha) se encontra dentro de outra palavra (palheiro)

    """


TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", "a"),
        "expected": "marcel é um gostos"
    },
    {   "input": ("marcela é uma gostosa", "gostosa"),
        "expected": "marcela é uma "
    },
    {   "input": ("marcela é uma gostosa", "duas"),
        "expected": "marcela é uma gostosa"
    },
    {   "input": ("marcela", "ar"),
        "expected": "mcela"
    },
    {   "input": ("", "uma"),
        "expected": ""
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\..")
    from runner import RootTestCaseManager
    RootTestCaseManager(remove_caractere, TEST_CASES).run()
