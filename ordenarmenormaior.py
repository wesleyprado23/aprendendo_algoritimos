import random

# Função que ordena uma lista em ordem crescente (sem modificar a original)
def ordena_crescente(array):                                                    
    array_ordenado = []  # Lista onde os elementos serão armazenados em ordem

    # Continua até que todos os elementos da lista original sejam removidos
    while len(array) > 0:
        menor = array[0]   # Assume que o primeiro elemento é o menor
        indice = 0         # Salva o índice do menor valor encontrado

        # Percorre o restante da lista procurando por um valor menor
        for i in range(1, len(array)):                                              
            if array[i] < menor:  # Se encontrar um valor menor
                menor = array[i]
                indice = i        # Atualiza o índice do menor valor

        # Adiciona o menor valor encontrado à lista ordenada
        array_ordenado.append(menor)

        # Remove o menor valor da lista original (ou melhor, da cópia)
        array.pop(indice)

    return array_ordenado  # Retorna a lista ordenada
                                                       
# Cria uma lista com 10 números aleatórios entre 1 e 100                       
array = [random.randint(1, 100) for _ in range(10)]

# Faz uma cópia da lista original para não modificá-la na ordenação
lista_temporaria = array[:]

# Exibe a lista original e a lista ordenada
print(array)                                                                    
print(ordena_crescente(lista_temporaria)) 
