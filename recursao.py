def procure_pela_chave_sem_recursao(caixa_principal):
    pilha = [caixa_principal]  # Inicializa a pilha com a caixa principal

    while pilha:
        caixa = pilha.pop()  # Retira a última caixa da pilha

        for item in caixa:
            if item == "chave":
                print("Achei a chave!")
                return
            elif isinstance(item, list):
                # Se o item for uma caixa, coloque-a na pilha para análise posterior
                pilha.append(item)

# Exemplo de uso:
caixa_principal = [
    "caixa",
    "caixa",
    ["chave"],
    "caixa",
    ["outra caixa", ["mais caixas", ["chave"]]]
]

procure_pela_chave_sem_recursao(caixa_principal)


def procure_pela_chave_com_recursao(caixa):
    for item in caixa:
        if item == "chave":
            print("Achei a chave!")
            return
        elif isinstance(item, list):
            # Se o item for uma caixa, faça uma chamada recursiva para procurar dentro dela
            procure_pela_chave_com_recursao(item)

# Exemplo de uso:
caixa_principal = [
    "caixa",
    "caixa",
    ["chave"],
    "caixa",
    ["outra caixa", ["mais caixas", ["chave"]]]
]

procure_pela_chave_com_recursao(caixa_principal)
