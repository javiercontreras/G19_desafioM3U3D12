import sys

input_data = sys.argv
tc_sol_peruano = float(sys.argv[1])
tc_peso_argentino = float(sys.argv[2])
tc_dolar_americano = float(sys.argv[3])
pesos_chilenos = float(sys.argv[4])


print(f"Los {pesos_chilenos} pesos equivalen a: \n{pesos_chilenos*tc_sol_peruano} Soles\n{pesos_chilenos*tc_peso_argentino} Pesos Argentinos\n{pesos_chilenos*tc_dolar_americano}  Dólares")