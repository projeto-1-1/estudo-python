from desafio_1 import codifica, decodifica
CASES = [
    (codifica, codifica.codifica),
    (decodifica, decodifica.decodifica),
]

import sys
sys.path.append(sys.path[0] + r"\\\\.." * 2)
from src.helpers import PackageTestCaseManager

package_test_case = PackageTestCaseManager("desafio_1", CASES)

if __name__ == "__main__":
    package_test_case.run()
