from typing import List
from src.helpers.runner.manager import TestCaseManager
from src.helpers.chalk import chalk

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