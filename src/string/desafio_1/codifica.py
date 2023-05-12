def swap_char(string: str, index_a, index_b):
    char_a = string[index_a]
    char_b = string[index_b]
    prev = string[:index_a]
    meio = string[index_a+1:index_b]
    dpois = string[index_b+1:]
    return prev + char_b + meio + char_a + dpois

def codifica(string):
    """
    @param string: str - a string a ser codigicada

    Codifica a string
    
    @exemplo
    exemplo  => elpmexo
    batata  => btataa
    potato  => ptatoo
    lorem ipsum potato yeye  => lyey otatop muspi meroe
    Essa bagaça me custou R$2.80  => E8.2$R uotsuc em açagab ass0

    @return string codificada
    """
    

    

TEST_CASES = [
    {
        "input": ["exemplo"],
        "expected": "elpmexo"
    },
    {   "input": ["batata"],
        "expected": "btataa"
    },
    {   "input": ["potato"],
        "expected": "ptatoo"
    },
    {   "input": ["lorem ipsum potato yeye"],
        "expected": "lyey otatop muspi meroe"
    },
    {   "input": ["Essa bagaça me custou R$2.80"],
        "expected": "E8.2$R uotsuc em açagab ass0"
    },
]

if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + r"\\\\.." * 3)
    from src.helpers.runner import RootTestCaseManager
    RootTestCaseManager(codifica, TEST_CASES).run()