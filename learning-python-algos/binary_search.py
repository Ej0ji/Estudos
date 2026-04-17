# Biblioteca local com o dicionário de nomes genéricos
from name_dict import *
import time

def buscaBinaria(iniLista, fimLista): # -> int

    inicio = time.time()
    fim = time.time()

    '''
    Algoritmo de busca binária para dicionários que possuem chaves (como índices numéricos - int) e valores (como nomes - strings).

    iniLista -> Parâmetro de entrada para gerar o ínicio da lista do intervalo

    fimLista -> Parâmetro de entrada para gerar o fim da lista do intervalo

    '''

    # Preenchimento da lista com o intervalo gerado a partir dos parâmetros de entrada da função
    intervaloDeIndices = []

    for itensLista in range(iniLista, (fimLista + 1)):
        intervaloDeIndices.append(itensLista)

    # Declaração de variáveis da função
    indicePrincipal = 0 
    indiceMax = max(intervaloDeIndices)
    indiceMin = min(intervaloDeIndices)
    sinal = 0
    contadorDeLoops = 0 

    # Iteração da busca binária - Terminará apenas quando o valor a ser buscado dentro da lista for encontrado, caso ocorra uma exceção será retornado um erro
    while True:
        try:
            # Nome a ser buscado dentro do dicionário de nomes genéricos
            nomeASerBuscado = input("Digite um nome: ")
            # Índice do nome a ser buscado dentro do dicionário (caso o nome inserido não exista dentro do dicionário, a variável receberá o valor 'None')
            indiceASerBuscado = next((chave for chave, valor in dicionarioGenerico.items() if valor == nomeASerBuscado), None)

            # Se o índice do nome a ser buscado não existir, não terá como encontrá-lo dentro do dicionário. Para isso uma exception é criada
            if indiceASerBuscado == None:
                raise Exception("O valor a ser buscado não está presente no intervalo!")

            # Enquanto o indice de busca ('indicePrincipal') não for o mesmo que o indice a ser buscado ('indiceASerBuscado'), o loop para encontrar o indice específico ocorrerá
            while indicePrincipal != indiceASerBuscado:

                contadorDeLoops += 1 # Será usado para verificar, ao final, a quantidade loops que foram necessários para encontrar o índice do nome

                # Materialização da lista temporária que varia conforme o afunilamento do intervalo
                listaTmp = []

                for itensListaTmp in range(indiceMin, (indiceMax + 1)):
                    listaTmp.append(itensListaTmp)
            
                # Bloco de alteração do indice de busca ('indicePrincipal') conforme afunilamento dos intervalos da lista temporária ('listaTmp')
                if indiceMin != 1 and sinal == 0:
                    indicePrincipal = indicePrincipal + int(((max(listaTmp) + 1) - min(listaTmp)) / 2)
                elif indiceMin != 1 and sinal == 1:
                    indicePrincipal = indicePrincipal - int(((max(listaTmp) + 1) - min(listaTmp)) / 2)
                else:
                    indicePrincipal = int(max(listaTmp) / 2)

                # Bloco de verificação de proximidade do indice de busca ('indicePrincipal') com o indice a ser buscado ('indiceASerBuscado')
                if indicePrincipal > indiceASerBuscado:

                    indiceMax = indicePrincipal
                    sinal = 1
                    continue

                if indicePrincipal < indiceASerBuscado:

                    indiceMin = indicePrincipal
                    sinal = 0
                    continue
            
            fim = time.time()

            tempoExec = fim - inicio 

            # Dicionario com o indice correspondente ao nome buscado no dicionário de nomes genéricos ('dicionarioGenerico') e quantidade de loops ocorridos para encontrar o nome
            dadosIndice = {
                    "indice" : indicePrincipal,
                    "loops" : contadorDeLoops,
                    "tempo execução" : tempoExec
            }


            return dadosIndice
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
# Teste unitário da entrada, chamada e saída da função de busca binária
if __name__ == "__main__":

    inicioIntervalo = min(dicionarioGenerico)
    fimIntervalo = max(dicionarioGenerico)
    print(buscaBinaria(inicioIntervalo, fimIntervalo))










