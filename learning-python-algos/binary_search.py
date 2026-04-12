import time

def buscaBinaria(iniLista, fimLista): # -> int

    # Remova o '#' do time.sleep(), caso queira debuggar a busca binária
    # time.sleep(5)

    # Preenchimento da lista com valores de parâmetros da função
    lista = []

    for itensLista in range(iniLista, (fimLista + 1)):
        lista.append(itensLista)

    # Declaração de variáveis da função
    indicePrincipal = 0
    indiceMax = max(lista)
    indiceMin = min(lista)
    sinal = 0

    # Variável de valor desejado para busca dentro do intervalo definido dentro da lista
    valorASerBuscado = int(input(f"Digite um valor inteiro de {indiceMin} a {indiceMax} para localizar o elemento na lista: "))

    # Iteração da busca binária - Terminará quando o indice da lista coincidir com o valor a ser buscado dentro da lista, isto é, quando a valor a ser buscado dentro da lista for encontrado 
    while indicePrincipal != valorASerBuscado:

        # Materialização da lista temporária que varia conforme o afunilamento do intervalo
        listaTmp = []

        for itensListaTmp in range(indiceMin, (indiceMax + 1)):
            listaTmp.append(itensListaTmp)
    
        # Bloco de modificação do indice principal conforme 
        if indiceMin != 1 and sinal == 0:
            indicePrincipal = indicePrincipal + int(((max(listaTmp) + 1) - min(listaTmp)) / 2)
        elif indiceMin != 1 and sinal == 1:
            indicePrincipal = indicePrincipal - int(((max(listaTmp) + 1) - min(listaTmp)) / 2)
        else:
            indicePrincipal = int(max(listaTmp) / 2)

        if indicePrincipal > valorASerBuscado:

            indiceMax = indicePrincipal
            sinal = 1
            continue
        
        if indicePrincipal < valorASerBuscado:

            indiceMin = indicePrincipal
            sinal = 0
            continue

    return indicePrincipal

# Aprecie o resultado com moderação...
inicioIntervalo = int(input('Escolha um número para ser o ínicio do intervalo: '))
fimIntervalo = int(input('Escolha um número para ser o fim do intervalo: '))
print(buscaBinaria(inicioIntervalo, fimIntervalo))







