# Função que implementa a busca binária
def pesquisa_binaria(lista, numero):
    baixo = 0                     # Início da lista
    alto = len(lista) - 1         # Final da lista
    contador = 0                  # Contador de tentativas

    while baixo <= alto:
        contador += 1
        meio = (baixo + alto) // 2         # Encontra o índice do meio da lista
        chute = lista[meio]                # Número que está no meio

        if chute == numero:
            return chute, contador         # Número encontrado
        elif chute > numero:
            alto = meio - 1                # Atualiza o limite superior
        else:
            baixo = meio + 1               # Atualiza o limite inferior

    return None, contador                  # Número não encontrado

# Entrada do usuário: tamanho da lista
tamanho_lista = int(input("Digite o tamanho da lista: "))
print(f"\nO tamanho da lista é: {tamanho_lista}\n")

# Explicações para o usuário
print("Vou descobrir o número que você está pensando.")
print("E contar quantas tentativas precisei para adivinhar.\n")

# Entrada do número escolhido (deve estar dentro da lista)
numero_escolhido = int(input(f"Digite um número entre 1 e {tamanho_lista}: "))

# Criação da lista de 1 até o tamanho escolhido
minha_lista = list(range(1, tamanho_lista + 1))

# Chama a função de busca binária
chute, contador = pesquisa_binaria(minha_lista, numero_escolhido)

# Mostra o resultado da busca
if chute is not None:
    print(f"\nO número escolhido foi {chute}.")
    print(f"Precisei de {contador} tentativa(s) para encontrar.")
else:
    print("Não encontrei o número na lista.")
