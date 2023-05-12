def swap_char(string: str, index_a, index_b):
    char_a = string[index_a]
    char_b = string[index_b]
    prev = string[:index_a]
    meio = string[index_a+1:index_b]
    dpois = string[index_b+1:]
    return prev + char_b + meio + char_a + dpois

def decodifica(string):
    """
    @param string: str - a string a ser codigicada

    decodifica a string
    
    @exemplo
    elpmexo  => exemplo
    btataa  => batata
    ptatoo  => potato
    lyey otatop muspi meroe  => lorem ipsum potato yeye
    E8.2$R uotsuc em açagab ass0  => Essa bagaça me custou R$2.80

    @return string decodificada
    """
    

TEST_CASES = [
    {
        "input": ["elpmexo"],
        "expected": "exemplo"
    },
    {   "input": ["btataa"],
        "expected": "batata"
    },
    {   "input": ["ptatoo"],
        "expected": "potato"
    },
    {   "input": ["lyey otatop muspi meroe"],
        "expected": "lorem ipsum potato yeye"
    },
    {   "input": ["E8.2$R uotsuc em açagab ass0"],
        "expected": "Essa bagaça me custou R$2.80"
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(decodifica, TEST_CASES).run()
