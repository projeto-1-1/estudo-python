def procura_palavra(palheiro, agulha):
    """
    @param palheiro: str
    @param agulha: str
    
    Checa se uma palavra(agulha) se encontra dentro de outra palavra (palheiro)

    """
    






if __name__ == "__main__":
	def run_test_case(name, input, expected_output):
		output = procura_palavra(*input)
		if output != expected_output:
			print(f"teste #{name} => concat{input}")
			print(f"\tEsperado:  {expected_output}")
			print(f"\tRetornado: {output}")
			print()
			return 1
		print(f"teste #{name} - ok")
		return 0

	results = [
		run_test_case("0", ("marcela é uma gostosa","uma"), True),
		run_test_case("1", ("marcela é uma gostosa","uma gostosa"), True),
		run_test_case("2", ("marcela é uma gostosa","duas"), False),
		run_test_case("3", ("marcela","pica"), False),
		run_test_case("4", ("","uma"), False),
	]

	if(sum(results) == 0):
		print("~ OK")

