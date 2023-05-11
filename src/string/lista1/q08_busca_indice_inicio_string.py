def busca_indice_inicio_string(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Checa se uma palavra(agulha) se encontra dentro de outra palavra (palheiro)

    @return [int] o indice em que a palavra se inicia
    Case [agulha] não existe dentro [palheiro], retornar -1
    """
    


TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", "uma"),
        "expected": 10
    },
    {   "input": ("marcela é uma gostosa", "uma gostosa"),
        "expected": 10
    },
    {   "input": ("marcela é uma gostosa", "una"),
        "expected": -1
    },
    {   "input": ("marcela é uma gostosa", "duas"),
        "expected": -1
    },
    {   "input": ("marcela", "pica"),
        "expected": -1
    },
    {   "input": ("", "uma"),
        "expected": -1
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(busca_indice_inicio_string, TEST_CASES).run()
