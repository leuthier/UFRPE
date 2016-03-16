def bolha(lista):
    troca = True
    while troca:
        troca = False
        for x in range(len(lista)-1):
            if lista[x] > lista[x+1]:
                chave = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = chave
                troca = True
    return lista
import sys
abre = open(sys.argv[1],"r")
sai = open(sys.argv[2],"w")
lista=abre.readline().strip('\n').split(' ')
carros = int(lista[0])
voltas = int(lista[1])
if 3 <= carros and carros <=100 and 1<= voltas and voltas <= 100:
    pilotos,tempo,aux = [],[],[]
    vencedor = ""
    for i in range(carros):
        nums = abre.readline().strip('\n').split(' ')
        soma = 0
        pilotos.append(nums)
        for a in range(voltas):
            numero = nums[a]
            eta = int(numero)
            soma += eta 
        tempo.append(soma)
    for x in range(len(tempo)):
        aux.append(tempo[x])
    bolha(aux)
    for y in range(3):
        if aux[y] in tempo:
            corredor = tempo.index(aux[y])
            corredor += 1
            vencedor += str(corredor)+"\n"
    sai.write(vencedor)
    sai.close()               
else:
    sai.write("Intervalo nao permitido")
    sai.close()
