def bolha(lista):
  troca = True
  while troca:
    troca = False
    for x in range(len(lista)-1):
      if lista[x][0] < lista[x+1][0]:
        chave = lista[x]
        lista[x] = lista [x+1]
        lista[x+1] = chave
        chave2 = aux[x]
        aux[x] = aux [x+1]
        aux[x+1] = chave2
        troca = True
      else:
        if lista[x][0] == lista[x+1][0] and lista[x][1]<lista[x+1][1]:
          chave = lista[x]
          lista[x] = lista [x+1]
          lista[x+1] = chave
          chave2 = aux[x]
          aux[x] = aux [x+1]
          aux[x+1] = chave2
          troca = True
        else:
          if lista[x][0] == lista[x+1][0] and lista[x][1] == lista[x+1][1] and lista[x][2]<lista[x+1][2]:
            chave = lista[x]
            lista[x] = lista [x+1]
            lista[x+1] = chave
            chave2 = aux[x]
            aux[x] = aux [x+1]
            aux[x+1] = chave2
            troca = True
          else:
            if lista[x][0] == lista[x+1][0] and lista[x][1] == lista[x+1][1] and lista[x][2]==lista[x+1][2] and aux[x]>aux[x+1]:
              chave = lista[x]
              lista[x] = lista [x+1]
              lista[x+1] = chave
              chave2 = aux[x]
              aux[x] = aux [x+1]
              aux[x+1] = chave2
              troca = True
  return lista

import sys
abre = open(sys.argv[1],"r")
sai = open(sys.argv[2],"w")
lista = abre.readline().strip('\n').split(' ')
num_pais = int(lista[0])
mod = int(lista[1])
if 1<= num_pais and num_pais <=100:
    if 1<=mod and mod <=100:
        paises,aux = [],[]
        vencedor = ""
        ouro, prata, bronze = 0,0,0 
        for a in range(num_pais):
            paises.append([ouro,prata,bronze])
            aux.append(a+1)
        for i in range(mod):
          linha  = abre.readline().strip('\n').split(" ")
          print("linha",linha)
          paises[int(linha[0])-1][0] += 1
          paises[int(linha[1])-1][1] += 1
          paises[int(linha[2])-1][2] += 1
        bolha(paises)
        for n in range(len(aux)):
          if aux[n] == aux[-1]:
            vencedor += str(aux[n])
          else:
            vencedor += str(aux[n])
            vencedor += " "
        vencedor += "\n"
        sai.write(vencedor)
        sai.close()
    else:
        sai.write("NUmero de modalidades fora do intervalo")
        sai.close()
else:
    sai.write("Numero de paises fora do intervalo")
    sai.close()
