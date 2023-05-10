def pega_fatia_da_palavra(palavra, inicio, fim):
    """
    @param palavra: str - palavra a ser cortada
    @param inicio: int - indice de inicio do corte
    
    Retorna uma fatia da palavra

    @return str a fatia da palavra dentro dos indices [inicio] e [fim]
	"""


TEST_CASES = [
    {
        "input": ("marcela é uma gostosa", 0, 7),
        "expected": "marcela"
    },
    {   "input": ("marcela é uma gostosa", 10, 1000),
        "expected": "uma gostosa"
    },
    {   "input": ("marcela é uma gostosa", 5, 9),
        "expected": "la é"
    },
    {   "input": ("marcela", 3, 4),
        "expected": "c"
    },
    {   "input": ("", 0, 1),
        "expected": ""
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\..")
    from runner import RootTestCaseManager
    RootTestCaseManager(pega_fatia_da_palavra, TEST_CASES).run()
