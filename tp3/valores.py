import random

def imprime(vetor):
    for num in vetor:
        print(num, end=" ")
    print()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    meio = len(arr) // 2
    lista_esquerda = arr[:meio]
    lista_direita = arr[meio:]

    # Recursivamente ordena cada metade
    lista_esquerda = merge_sort(lista_esquerda)
    lista_direita = merge_sort(lista_direita)

    # Combina as duas metades ordenadas
    return merge(lista_esquerda, lista_direita)

def merge(lista_esquerda, lista_direita):
    resultado = []
    i = j = 0

    # Combina as duas listas ordenadas
    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] < lista_direita[j]:
            resultado.append(lista_esquerda[i])
            i += 1
        else:
            resultado.append(lista_direita[j])
            j += 1

    # Adiciona os elementos restantes, se houver
    resultado.extend(lista_esquerda[i:])
    resultado.extend(lista_direita[j:])

    return resultado


def random_double():
    return random.random()

def aloca(vetor, semi_ordenado, tamanho, uniformidade):
    vetor.clear()
    if uniformidade and semi_ordenado:
        ini = tamanho // 3
        for i in range(ini):
            vetor.append(-ini - i)
            vetor.append(0)
            vetor.append(ini + i)
        return

    if uniformidade and not semi_ordenado:
        ini = tamanho // 3
        for i in range(ini):
            vetor.append(-random_double())
            vetor.append(0)
            vetor.append(random_double())
        return

    if semi_ordenado:
        for i in range(tamanho):
            vetor.append(i)

        perturbacao = tamanho // (random.randint(1, 1000))
        for i in range(perturbacao):
            indice1 = random.randint(0, tamanho - 1)
            indice2 = random.randint(0, tamanho - 1)
            vetor[indice1], vetor[indice2] = vetor[indice2], vetor[indice1]
        return

    if not semi_ordenado:
        for i in range(tamanho):
            vetor.append(random_double())
        for i in range(tamanho // 2):
            mudar = random.randint(0, tamanho - 1)
            vetor[mudar] = -vetor[mudar]

def DNFS(vetor):
    baixo = 0
    alto = len(vetor) - 1
    i = 0

    while i <= alto:
        if vetor[i] < 0:
            vetor[i], vetor[baixo] = vetor[baixo], vetor[i]
            baixo += 1
            i += 1
        elif vetor[i] > 0:
            vetor[i], vetor[alto] = vetor[alto], vetor[i]
            alto -= 1
        else:
            i += 1
    
    return vetor

def main(metodo, semi_ordenado, tamanho, uniformidade):
    random.seed()
    vetor = []
    # tamanho = 1000000 if tamanho else 2000000        # 1000000 ou 2000000
    tamanho = 5 if tamanho else 10        # 1000000 ou 2000000

    aloca(vetor, semi_ordenado, tamanho, uniformidade)

    if (metodo == 0):
        vetor = DNFS(vetor)
    else:
        vetor = merge_sort(vetor)
        
    imprime(vetor)