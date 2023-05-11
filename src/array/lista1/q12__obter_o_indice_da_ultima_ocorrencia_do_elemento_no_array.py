def obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array(array, elemento):
    """
    @param array: list
    @param elemento

    Pega o indice da última ocorrencia do [elemento] dentro de [array]

    Se não houver nenhuma ocorrencia, retornar -1

    @return 
    """
    

TEST_CASES = [
    {
        "input": ([0, 1, 2, 3, 4, 5], 3),
        "expected": 3
    },
    {   "input": ([0, 1, 2], 4),
        "expected": -1
    },
    {   "input": ([0, 1, 2, 1, 1, 2, 3], 1),
        "expected": 4
    },
    {   "input": ([0, 1, 2, 1, 1, 2, 3], 2),
        "expected": 5
    },
    {   "input": ([0, 1, 2, 1, 1, 2, 3], 3),
        "expected": 6
    },
    {   "input": ([0, 1, 2, 1, 1], 0),
        "expected": 0
    },
    {   "input": ([], 2),
        "expected": -1
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array, TEST_CASES).run()