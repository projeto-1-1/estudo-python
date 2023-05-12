from gabarito_lista1_secret import (
    q02_concatenar as concatenar_string,
    q03_procura_caractere as procura_caractere,
    q04_pega_fatia_da_palavra as pega_fatia_da_palavra,
    q05_remove_um_caractere as remove_um_caractere,
    q06_busca_indice_caractere as busca_indice_caractere,
    q07_remove_varios_caracteres as remove_varios_caracteres,
    q08_busca_indice_inicio_string as busca_indice_inicio_string,
    q09_procura_string as procura_string,
    q10_busca_indices_string as busca_indices_string,
    q11_insere_caractere_no_indice as insere_caractere_no_indice
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
    (busca_indices_string, busca_indices_string.busca_indices_string),
    (insere_caractere_no_indice, insere_caractere_no_indice.insere_caractere_no_indice)
]

import sys
sys.path.append(sys.path[0] + r"\\\\.." * 2)
from src.helpers import PackageTestCaseManager

package_test_case = PackageTestCaseManager("gabarito_lista1_secret", CASES)

if __name__ == "__main__":
    package_test_case.run()
