from typing import List
from src.helpers.runner.test_case import TestCase
from src.helpers.runner.test_case_error import TestCaseErrors
from src.helpers.runner.utils import is_last_index_in_array, pause

class TestCaseManager:
    def __init__(self, sut):
        self.__cases = list[TestCase]()
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

    def pause(self, next):
        pause(next)

    def run(self, verbose: bool = False, root: str = "", pausing = False) -> List[TestCaseErrors]:
        errors = []
        for (test_case, index) in zip(self.__cases, range(0, len(self.__cases))):
            code = test_case.run(self.__sut, verbose = verbose, root = root)
            if code == 0:
                continue
            errors.append(TestCaseErrors(test_case))
            if is_last_index_in_array(index, self.__cases):
                 continue
            if pausing:
                next = self.__cases[index+1]
                pause(f"{self.__sut.__name__} - {next.id}")
        return errors
    