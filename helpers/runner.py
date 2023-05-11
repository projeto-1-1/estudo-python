from collections.abc import Sequence
from typing import List
from helpers.chalk import chalk

def compare(v1, v2, depth = 0):
    if v1 is None:
        return v2 is None
    if isinstance(v1, str):
        return v1 == v2
    if isinstance(v1, Sequence):
        if not isinstance(v2, Sequence):
            return False
        if len(v1) != len(v2):
            return False
        for i in range(0, len(v1)):
            return compare(v1[i], v2[i], depth + 1)
        return True
    return v1 == v2

def stringifyValue(value):
    if isinstance(value, str):
        return f"\"{value}\""
    return value

class TestCase:
    def __init__(self, id, input, expected_output):
        self.id = f"#{id}"
        self.input = input
        self.expected_output = expected_output
        self.received_output = None

    def run(self, sut, verbose: bool, root: str = ''):
        output = sut(*self.input)
        TAB = "  "
        id = self.id #".".join(filter(lambda v: len(v) > 0, [root, str(self.id)]))

        self.received_output = output

        if not compare(output,self.expected_output):
            print(chalk.red(f"teste {id} => {sut.__name__}{self.input}"))
            print(f"{TAB}Esperado:  {stringifyValue(self.expected_output)}")
            print(f"{TAB}Retornado: {stringifyValue(output)}")
            print()
            return 1
        if verbose:
            print(chalk.green(f"teste {id} - ok"))
        return 0

class TestCaseErrors:
    def __init__(self, test_case: TestCase):
        self.case = test_case

class TestCaseManager:
    def __init__(self, sut):
        self.__cases = list[TestCase]()
        self.__sut = sut
        self.__index = 0
        self.__prematureFinish = False

    def add(self, input, expected_output):
        self.__index = self.__index + 1
        self.__cases.append(TestCase(self.__index, input, expected_output))
        return self
    
    def addMany(self, test_cases):
        for test_case in test_cases:
            self.add(test_case["input"], test_case["expected"])
        return self

    def pause(self, next):
        import sys
        import msvcrt as m
        print(f"Pressione ENTER para executar [{chalk.cyan(next)}]")
        if m.getch() in [b'q', b'\x03']:
            exit(1)
        sys.stdout.write("\033[F")
        print(" "*len(f"Pressione ENTER para executar [{next}]"))
        sys.stdout.write("\033[F")


    def run(self, verbose: bool = False, root: str = "", pausing = False) -> List[TestCaseErrors]:
        errors = []
        for (test_case, index) in zip(self.__cases, range(0, len(self.__cases))):
            if self.__prematureFinish:
                exit(1)
            code = test_case.run(self.__sut, verbose = verbose, root = root)
            if code == 1:
                errors.append(TestCaseErrors(test_case))

                if pausing and index != (len(self.__cases) - 1):
                    next = self.__cases[index+1]
                    self.pause(f"{self.__sut.__name__} - {next.id}")
        return errors
    


class RootTestCaseManager:
    def __init__(self, sut, test_cases):
        self.manager = TestCaseManager(sut).addMany(test_cases)

    def run(self, pausing = True):
        errors = self.manager.run(verbose = True, pausing = pausing)
        errors_count = len(errors)
        if errors_count == 0:
            print(chalk.green("~ OK"))
        else:
            errors_name = str(chalk.red(", ", False)).join([str(chalk.magenta(error.case.id, False)) for error in errors])
            print(chalk.red(f"Os seguintes testes finalizaram com errors:"), errors_name)
            print(f"{errors_count} errors")