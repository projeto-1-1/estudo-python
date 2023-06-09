
from src.helpers.chalk import chalk
from src.helpers.runner.utils import stringifyValue
from src.helpers.runner.test_matcher import TestMatcher

class TestCase:
    def __init__(self, id, input, expected_output):
        self.id = f"#{id}"
        self.input = input
        self.expected_output = expected_output
        self.matcher = TestMatcher(expected_output)
        self.received_output = None

    def run(self, sut, verbose: bool, root: str = ''):
        output = sut(*self.input)
        TAB = "  "
        id = self.id #".".join(filter(lambda v: len(v) > 0, [root, str(self.id)]))

        self.received_output = output

        self.matcher.compare(output)

        if not self.matcher.is_valid:
            print(chalk.red(f"teste {id} => {sut.__name__}{self.input}"))
            print(f"{TAB}Esperado:  {stringifyValue(self.matcher.message)}")
            print(f"{TAB}Retornado: {stringifyValue(output)}")
            print()
            return 1
        if verbose:
            print(chalk.green(f"teste {id} - ok"))
        return 0


class TestCaseErrors:
    def __init__(self, test_case: TestCase):
        self.case = test_case
