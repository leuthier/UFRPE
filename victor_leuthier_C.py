##import sys
##abre = open(sys.argv[1],"r")
##sai = open(sys.argv[2],"w")
abre = open("C.in","r")
sai = open("C.out","w")
loop = int(abre.readline())

if loop > 2 and loop < 10:
    lista, lista2 = [], []
    coluna, linha, diag, diag2 = [],[],[],[]
    for i in range(loop):
        nums = abre.readline()
        sem_enter = nums.strip("\n")
        lista.append(sem_enter)
        str_num_lista = sem_enter.split(" ")
        lista2.append(str_num_lista)

    diagonal,diagonal2 = 0,0
    x = loop-1
    y = 0
    for b in range(len(lista)):
        soma_col,soma_linha,soma_diag,soma_diag2 = 0,0,0,0
        a = lista[b]
        sem_esp = a.split(" ")        
        soma_diag = int(lista2[b][b])
        diag.append(soma_diag)
        diagonal += diag[b]

        soma_diag2 = int(lista2[b][x]) #x pq pega o loop, como o loop eh 0 e n 1 ~~> loop-1
        diag2.append(soma_diag2)
        diagonal2 += diag2[y] 
        x -= 1
        y += 1 #aumentando o indice da lista
        
        for n in range(len(lista)):
            soma_linha += int(sem_esp[n])
            soma_col += int(lista2[n][b])
                    
        linha.append(soma_linha)
        coluna.append(soma_col)
        
    if diagonal == linha[b] and  diagonal == coluna[b] and diagonal == diagonal2 and linha[b]==coluna[b]:
        sai.write(str(diagonal))
    else:
        sai.write("-1")
else:
    sai.write("Numero de casos testes fora do intervalo permitido.")
abre.close()
sai.close()
