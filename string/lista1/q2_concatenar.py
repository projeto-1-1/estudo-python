def concatenar_string(string_a, string_b):
    """
    @param a: str
    """


if __name__ == "__main__":

    def run_test_case(name, input, expected_output):
        output = concatenar_string(*input)
        if output != expected_output:
            print(f"teste #{name} => concat{input}")
            print(f"\tEsperado:  {expected_output}")
            print(f"\tRetornado: {output}")
            print()
            return 1
        print(f"teste #{name} - ok")
        return 0

    results = [
        run_test_case("0", ("batata", "-frita"), "batata-frita"),
        run_test_case("1", ("a", "b"), "ab"),
        run_test_case("2", ("a", ""), "a"),
        run_test_case("3", ("", "b"), "b"),
        run_test_case("4", ("R$", "2.80"), "R$2.80"),
    ]

    if sum(results) == 0:
        print("~ OK")
