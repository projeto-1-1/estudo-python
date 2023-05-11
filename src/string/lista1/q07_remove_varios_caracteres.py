def remove_varios_caracteres(palheiro, agulhas):
    """
    @param palheiro: str
    @param agulha: List[str]

    Checa varios caracteres (agulhas) se encontra dentro de outra palavra (palheiro), e os remove

    @return str a string [palheiro] sem o caractere [agulha]
    """
    

TEST_CASES = [
    {
        "input": ("abcd", ["a"]),
        "expected": "bcd"
    },
    {   "input": ("au au diz o cachorro",[ "u", "o"]),
        "expected": "a a diz  cachrr"
    },
    {   "input": ("marcela é uma gostosa", ["a", "x", "y", "z"]),
        "expected": "mrcel é um gostos"
    },
    {   "input": ("marcela", ["p", "x"]),
        "expected": "marcela"
    },
    {   "input": ("", ["x"]),
        "expected": ""
    },
    {   "input": ("batata", []),
        "expected": "batata"
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(remove_varios_caracteres, TEST_CASES).run()
