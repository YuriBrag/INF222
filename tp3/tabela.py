import itertools
from prettytable import PrettyTable
from metodo import main

def gerar_matriz_combinacoes(fatores):
    combinacoes = list(itertools.product([-1, +1], repeat=4))
    matriz = []

    for combinacao in combinacoes:
        linha = list(combinacao) + [i*j for i, j in list(itertools.combinations(combinacao, 2))]+ [i*j*k for i,j,k in list(itertools.combinations(combinacao, 3))] + [i*j*k*z for i,j,k,z in list(itertools.combinations(combinacao, 4))] + [1]
        # matriz.append(str(linha).replace('-1', '-').replace('1','+').replace('[', '').replace(']','').split())
        matriz.append(linha)

    return matriz

# Defina os fatores
# Defina os fatores
fatores = ['M', 'T', 'E', 'Q']
fatores_2 = [f"{f1}{f2}" for f1, f2 in itertools.combinations(fatores, 2)]
fatores_3 = [f"{f1}{f2}{f3}" for f1, f2, f3 in itertools.combinations(fatores, 3)]
fatores_g_labels = fatores + fatores_2 + fatores_3 + ['MTEQ', 'I']

# Gere a matriz de todas as combinações possíveis
matriz_combinacoes = gerar_matriz_combinacoes(fatores)

for linha in matriz_combinacoes:
    teste_res = linha[0: 4]
    teste_res = [0 if i<0 else 1 for i in teste_res]
    main(*teste_res)

# Criar PrettyTable
tabela = PrettyTable(fatores_g_labels)
for linha in matriz_combinacoes:
    tabela.add_row(linha)

# Imprimir a tabela
# print("Matriz de Combinacoes:")
# print(tabela)