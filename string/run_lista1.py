from lista1 import (
    q02_concatenar as concatenar_string,
    q03_procura_caractere as procura_caractere,
    q04_pega_fatia_da_palavra as pega_fatia_da_palavra,
    q05_remove_um_caractere as remove_um_caractere,
    q06_busca_indice_caractere as busca_indice_caractere,
    q07_remove_varios_caracteres as remove_varios_caracteres,
    q08_busca_indice_inicio_string as busca_indice_inicio_string,
    q09_procura_string as procura_string,
    q10_busca_indices_string as busca_indices_string
)
CASES = [
    (concatenar_string, concatenar_string.concatenar_string),
    (procura_caractere, procura_caractere.procura_caractere),
    (pega_fatia_da_palavra, pega_fatia_da_palavra.pega_fatia_da_palavra),
    (remove_um_caractere, remove_um_caractere.remove_um_caractere),
    (busca_indice_caractere, busca_indice_caractere.busca_indice_caractere),
    (remove_varios_caracteres, remove_varios_caracteres.remove_varios_caracteres),
    (busca_indice_inicio_string, busca_indice_inicio_string.busca_indice_inicio_string),
    (procura_string, procura_string.procura_string),
    (busca_indices_string, busca_indices_string.busca_indices_string)
]

import sys
sys.path.append(sys.path[0] + r"\\\\..")
from helpers import TestCaseManager, chalk

if __name__ == "__main__":
    def get_name(module):
        return str(module.__name__).split(".").pop()

    all_errors = 0
    for (test_case, index) in zip(CASES, range(0, len(CASES))):
        module, sut = test_case

        manager = TestCaseManager(sut).addMany(module.TEST_CASES)

        name = get_name(module)

        print(chalk.cyan(f"Test [{name}]:"))
        errors = manager.run(root = sut.__name__)

        all_errors = all_errors + len(errors)
        if len(errors) == 0:
            print(chalk.green(f">> ok"))
            continue
        print(chalk.cyan(f"Test [{name}]:"))
        errors_name = str(chalk.red(", ")).join([str(chalk.magenta(error.case.id)) for error in errors])
        print(chalk.red(f">> {len(errors)} testes finalizaram com erro, são eles:"), errors_name)

        if index != (len(CASES) - 1):
            next = get_name(CASES[index+1][0])
            print()
            manager.pause(f"Pressione ENTER para executar [{next}]")

    print()
    if all_errors == 0:
        print(chalk.green("Boaa!! Nenhum erro!!"))
    else:
        print(chalk.red(f"Não foi dessa vez...\nAinda tem [{all_errors}] erros para serem resolvidos"))
