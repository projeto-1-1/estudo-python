def remove_um_caractere(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Checa se um caractere(agulha) se encontra dentro de outra palavra (palheiro), e o remove

    @return str a string [palheiro] sem o caractere [agulha]
    """
    

TEST_CASES = [
    {
        "input": ("abcd", "a"),
        "expected": "bcd"
    },
    {   "input": ("au au diz o cachorro", "u"),
        "expected": "a a diz o cachorro"
    },
    {   "input": ("marcela é uma gostosa", "x"),
        "expected": "marcela é uma gostosa"
    },
    {   "input": ("marcela", "p"),
        "expected": "marcela"
    },
    {   "input": ("", "x"),
        "expected": ""
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(remove_um_caractere, TEST_CASES).run()
