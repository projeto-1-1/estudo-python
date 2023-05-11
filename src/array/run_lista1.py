from lista1 import (
    q01__criar_array_de_tamanho_fixo as criar_array_de_tamanho_fixo,
    q02__obter_tamanho_do_array as obter_tamanho_do_array,
    q03__adicionar_elemento_no_final_do_array as adicionar_elemento_no_final_do_array,
    q04__adicionar_elemento_no_inicio_do_array as adicionar_elemento_no_inicio_do_array,
    q05__criar_sequencia_de_tamanho_n as criar_sequencia_de_tamanho_n,
    q06__criar_sequencia_de_tamanho_n_com_inicio as criar_sequencia_de_tamanho_n_com_inicio,
    q07__criar_sequencia_de_tamanho_n_com_inicio_e_passo as criar_sequencia_de_tamanho_n_com_inicio_e_passo,
    q08__substituir_item_no_indice as substituir_item_no_indice,
    q09__verificar_se_item_existe_no_array as verificar_se_item_existe_no_array,
    q10__contar_ocorrencias_de_item_no_array as contar_ocorrencias_de_item_no_array,
    q11__obter_o_indice_da_primeira_ocorrencia_do_elemento_no_array as obter_o_indice_da_primeira_ocorrencia_do_elemento_no_array,
    q12__obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array as obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array,
    q13__remover_elemento_no_indice_do_array as remover_elemento_no_indice_do_array,
    q14__remover_a_primeira_ocorrencia_do_elemento_do_array as remover_a_primeira_ocorrencia_do_elemento_do_array,
    q15__remover_todas_as_ocorrencias_do_elemento_do_array  as remover_todas_as_ocorrencias_do_elemento_do_array,
    q16__remover_todas_as_ocorrencias_de_muitos_elementos_do_array as remover_todas_as_ocorrencias_de_muitos_elementos_do_array,
    q17__contar_ocorrencias_de_todos_os_elementos_no_array  as contar_ocorrencias_de_todos_os_elementos_no_array,
    q18__inverter_array as inverter_array,
    q19__concatenar_dois_arrays as concatenar_dois_arrays,
    q20__encontrar_o_valor_minimo_e_maximo_no_array_de_numeros as encontrar_o_valor_minimo_e_maximo_no_array_de_numeros,
)

CASES = [
    (criar_array_de_tamanho_fixo, criar_array_de_tamanho_fixo.criar_array_de_tamanho_fixo),
    (obter_tamanho_do_array, obter_tamanho_do_array.obter_tamanho_do_array),
    (adicionar_elemento_no_final_do_array, adicionar_elemento_no_final_do_array.adicionar_elemento_no_final_do_array),
    (adicionar_elemento_no_inicio_do_array, adicionar_elemento_no_inicio_do_array.adicionar_elemento_no_inicio_do_array),
    (criar_sequencia_de_tamanho_n, criar_sequencia_de_tamanho_n.criar_sequencia_de_tamanho_n),
    (criar_sequencia_de_tamanho_n_com_inicio, criar_sequencia_de_tamanho_n_com_inicio.criar_sequencia_de_tamanho_n_com_inicio),
    (criar_sequencia_de_tamanho_n_com_inicio_e_passo, criar_sequencia_de_tamanho_n_com_inicio_e_passo.criar_sequencia_de_tamanho_n_com_inicio_e_passo),
    (substituir_item_no_indice, substituir_item_no_indice.substituir_item_no_indice),
    (verificar_se_item_existe_no_array, verificar_se_item_existe_no_array.verificar_se_item_existe_no_array),
    (contar_ocorrencias_de_item_no_array, contar_ocorrencias_de_item_no_array.contar_ocorrencias_de_item_no_array),
    (obter_o_indice_da_primeira_ocorrencia_do_elemento_no_array, obter_o_indice_da_primeira_ocorrencia_do_elemento_no_array.obter_o_indice_da_primeira_ocorrencia_do_elemento_no_array),
    (obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array, obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array.obter_o_indice_da_ultima_ocorrencia_do_elemento_no_array),
    (remover_elemento_no_indice_do_array, remover_elemento_no_indice_do_array.remover_elemento_no_indice_do_array),
    (remover_a_primeira_ocorrencia_do_elemento_do_array, remover_a_primeira_ocorrencia_do_elemento_do_array.remover_a_primeira_ocorrencia_do_elemento_do_array),
    (remover_todas_as_ocorrencias_do_elemento_do_array, remover_todas_as_ocorrencias_do_elemento_do_array.remover_todas_as_ocorrencias_do_elemento_do_array),
    (remover_todas_as_ocorrencias_de_muitos_elementos_do_array, remover_todas_as_ocorrencias_de_muitos_elementos_do_array.remover_todas_as_ocorrencias_de_muitos_elementos_do_array),
    (contar_ocorrencias_de_todos_os_elementos_no_array, contar_ocorrencias_de_todos_os_elementos_no_array.contar_ocorrencias_de_todos_os_elementos_no_array),
    (inverter_array, inverter_array.inverter_array),
    (concatenar_dois_arrays, concatenar_dois_arrays.concatenar_dois_arrays),
    (encontrar_o_valor_minimo_e_maximo_no_array_de_numeros, encontrar_o_valor_minimo_e_maximo_no_array_de_numeros.encontrar_o_valor_minimo_e_maximo_no_array_de_numeros),
]

import sys
sys.path.append(sys.path[0] + r"\\\\.." * 2)
from src.helpers import PackageTestCaseManager

package_test_case = PackageTestCaseManager("lista1", CASES)

if __name__ == "__main__":
    package_test_case.run()
