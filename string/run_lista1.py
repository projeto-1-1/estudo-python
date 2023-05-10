from lista1 import (
    q1_imprimie_characteres,
    q2_concatenar,
    q3_procura_palavra,
    q4_remove_um_character,
)
from runner import TestCaseManager

if __name__ == "__main__":
    CASES = [
        (q3_procura_palavra, q3_procura_palavra.procura_palavra),
        (q4_remove_um_character, q4_remove_um_character.remove_caractere),
    ]

    all_errors = 0
    for (module, sut) in CASES:
        manager = TestCaseManager(sut).addMany(module.TEST_CASES)
        errors = manager.run()
        all_errors = all_errors + errors
        if errors == 0:
            print(f"Test [{sut.__name__}]: ok")
        else:
            print(f"Test [{sut.__name__}]: {errors} errors")

    print(f"Total: {all_errors} errors")
