class TestCase:
    def __init__(self, id, input, expected_output):
        self.id = id
        self.input = input
        self.expected_output = expected_output

    def run(self, sut, verbose: bool):
        output = sut(*self.input)
        TAB = "  "
        if output != self.expected_output:
            print(f"teste #{self.id} => {sut.__name__}{self.input}")
            print(f"{TAB}Esperado:  {self.expected_output}")
            print(f"{TAB}Retornado: {output}")
            print()
            return 1
        if verbose:
            print(f"teste #{self.id} - ok")
        return 0


class TestCaseManager:
    def __init__(self, sut):
        self.__cases = []
        self.__sut = sut
        self.__index = 0

    def add(self, input, expected_output):
        self.__index = self.__index + 1
        self.__cases.append(TestCase(self.__index, input, expected_output))
        return self
    
    def addMany(self, test_cases):
        for test_case in test_cases:
            self.add(test_case["input"], test_case["expected"])
        return self

    def run(self, verbose: bool = False) -> int:
        errors = 0
        for test_case in self.__cases:
            code = test_case.run(self.__sut, verbose)
            if code == 1:
                errors = errors + 1
        return errors

class RootTestCaseManager:
    def __init__(self, sut, test_cases):
        self.manager = TestCaseManager(sut).addMany(test_cases)

    def run(self):
        errors = self.manager.run(True)
        if errors == 0:
            print("~ OK")
        else:
            print(f"{errors} errors")