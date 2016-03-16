def bolha(lista):
    troca = True
    while troca:
        troca = False
        for x in range(len(lista)-1):
            if lista[x] < lista[x+1]:
                chave = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = chave
                troca = True
    return lista

import sys
abre = open(sys.argv[1],"r")
fecha = open(sys.argv[2],"w")
pessoas = int(abre.readline())
bolos = int (abre.readline())
if 1<= pessoas <= 10000 and 1<= bolos <= 10000:
    tamanho = abre.readline().split(" ")
    tudo, aux, maior, metade = 0,0,0,0
    lista = []
    for i in range (len(tamanho)):
        tamanho[i] = int(tamanho[i])
        if tamanho[i] > maior:
            maior = tamanho[i]
    bolha(tamanho)
    for a in range(1,maior+1):
        lista.append(a)
    esquerda = 0
    direita = len(lista)-1
    meio = int(esquerda+direita/2)
    metade = lista[meio]
    while esquerda < direita:
        for x in range (len(tamanho)):
            if metade <= tamanho[x]:
                tudo += int(tamanho[x]/metade)
            else:
                break
        if tudo < pessoas:
            direita = meio - 1
            meio = int((esquerda+direita)/2)
            metade = lista[meio]
        elif metade > aux:
                aux = metade
                string = str(aux)+"\n"
                esquerda = meio + 1
                meio = int((direita+esquerda)/2)
                metade = lista[meio]
        tudo = 0
abre.close()
fecha.write(string)
fecha.close()
