def insere_caractere_no_indice(string, caractere, indice):
    """
    @param string: str - string original
    @param caractere: str - caractere a ser inserido
    @param indice: int - posicao que deve-se inserir o caractere

    Insere um caractere dentro de uma string em uma determinada posição

    @return a string com o caractere já inseridp
    """
    

TEST_CASES = [
    {
        "input": ("12356", "4", 3),
        "expected": "123456"
    },
    {
        "input": ("_____", "a", 1),
        "expected": "_a____"
    },
    {   "input": ("batata", "o", 3),
        "expected": "batoata"
    },
    {   "input": ("marcela é uma gostosa", "x", 10),
        "expected": "marcela é xuma gostosa"
    },
    {   "input": ("a", "p", 0),
        "expected": "pa"
    },
    {   "input": ("a", "p", 1),
        "expected": "ap"
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(insere_caractere_no_indice, TEST_CASES).run()
