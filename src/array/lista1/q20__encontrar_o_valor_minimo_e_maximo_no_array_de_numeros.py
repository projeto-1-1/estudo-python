def encontrar_o_valor_minimo_e_maximo_no_array_de_numeros(array):
    """
    @param array: list

    Retorna uma tuple com o valor minimo e o valor maximo dos numeros dentro de um array

    @return (min, max)
    """
    

TEST_CASES = [
    {
        "input": [[0, 1, 2, 3, 4, 5]],
        "expected": (0, 5)
    },
    {   "input": [[0, 1, 2]],
        "expected": (0, 2)
    },
    {   "input": [[0, 1, 2, 1, 2, 3]],
        "expected": (0, 3)
    },
    {   "input": [[0, 1, 3, 1, 1]],
        "expected": (0, 3)
    },
    {   "input": [[3, 2, 1]],
        "expected": (1, 3)
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(encontrar_o_valor_minimo_e_maximo_no_array_de_numeros, TEST_CASES).run()