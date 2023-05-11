def busca_indices_string(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str

    Remove varias strings(agulha) de dentro de outra palavra (palheiro)

    @return (int, int) os indices de inicio e fim da agulha dentro da palavra.
    Se [agulha] não existir dentro [palheiro], retornar None
    """
    

TEST_CASES = [
   {
       "input": ("abcdefg", "bc"),
       "expected": [1, 2]
   },
   {
       "input": ("marcela é uma gostosa", "uma"),
       "expected": [10, 12]
   },
    {   "input": ("marcela é uma gostosa", "uma gostosa"),
        "expected": [10, 20]
    },
   {   "input": ("marcela é uma gostosa", "duas"),
       "expected": None
   },
   {   "input": ("marcela", "pica"),
       "expected": None
   },
    {   "input": ("potato_x", "_x"),
        "expected": [6,7]
    },
   {   "input": ("x_potato", "x_"),
       "expected": [0, 1]
   },
    {   "input": ("potato_x", "x"),
        "expected": [7,7]
    },
   {   "input": ("x_potato", "x"),
       "expected": [0,0]
   },
   {   "input": ("", "uma"),
       "expected": None
   },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\..\\\\..")
    from helpers.runner import RootTestCaseManager
    RootTestCaseManager(busca_indices_string, TEST_CASES).run()
