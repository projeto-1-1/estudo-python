from typing import List, Any, Tuple
from src.helpers.chalk import chalk
from src.helpers.runner.manager import TestCaseManager
from src.helpers.runner.utils import is_last_index_in_array

class PackageTestCaseManager:
	def __init__(self, package_name, cases: List[Tuple[Any, Any]]):
		self.__name = package_name
		self.__cases = cases

	def __get_module_name(self, module):
		return str(module.__name__).split(".").pop()

	def run(self):
		all_errors = 0
		for (test_case, index) in zip(self.__cases, range(0, len(self.__cases))):
			module, sut = test_case

			manager = TestCaseManager(sut).addMany(module.TEST_CASES)

			name = self.__get_module_name(module)

			print(chalk.cyan(f"Test [{name}]:"))
			errors = manager.run(root = sut.__name__)

			all_errors = all_errors + len(errors)
			if len(errors) == 0:
				print(chalk.green(f">> ok"))
				continue
			print(chalk.cyan(f"Test [{name}]:"))
			errors_name = str(chalk.red(", ")).join([str(chalk.magenta(error.case.id)) for error in errors])
			print(chalk.red(f">> {len(errors)} testes finalizaram com erro, são eles:"), errors_name)

			next_module = self.__get_next_module(index)
			if next_module:
				next = self.__get_module_name(next_module)
				print()
				manager.pause(f"Pressione ENTER para executar [{next}]")

		print()
		if all_errors == 0:
			print(chalk.green("Boaa!! Nenhum erro!!"))
		else:
			print(chalk.red(f"Não foi dessa vez...\nAinda tem [{all_errors}] erros para serem resolvidos"))

	def __get_next_module(self, index):
		if is_last_index_in_array(index, self.__cases):
			return None
		return self.__cases[index+1][0]