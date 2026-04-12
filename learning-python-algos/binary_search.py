import time


    # Remova o '#' do time.sleep(), caso queira debuggar a busca binária
    # time.sleep(5)

def buscaBinaria(iniLista, fimLista): # -> int

    '''
    Algoritmo de busca binária possui complexidade de execução O(log2n)
    '''

    # Preenchimento da lista com valores de parâmetros da função
    lista = []

    for itensLista in range(iniLista, (fimLista + 1)):
        lista.append(itensLista)

    # Declaração de variáveis da função
    indicePrincipal = 0
    indiceMax = max(lista)
    indiceMin = min(lista)
    sinal = 0
    contadorDeLoops = 0

    # Iteração da busca binária - Terminará quando o valor a ser buscado dentro da lista for encontrado, caso ocorra uma exceção será retornado um erro descritivo
    while True:
        try:

             # Variável de valor desejado para busca dentro do intervalo definido dentro da lista
            valorASerBuscado = int(input(f"Digite um valor inteiro de {indiceMin} a {indiceMax} para localizar o elemento na lista: "))

            if valorASerBuscado not in lista:
                raise Exception("O valor a ser buscado não está presente no intervalo!")

            while indicePrincipal != valorASerBuscado:

                contadorDeLoops += 1

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

            meuDicionario = {
                    "indice" : indicePrincipal,
                    "loops" : contadorDeLoops
            }

            return meuDicionario
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        

# Aprecie o resultado com moderação...
inicioIntervalo = int(input('Escolha um número para ser o ínicio do intervalo: '))
fimIntervalo = int(input('Escolha um número para ser o fim do intervalo: '))
print(buscaBinaria(inicioIntervalo, fimIntervalo))







