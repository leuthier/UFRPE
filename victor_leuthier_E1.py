import sys
abre = open("1.txt","r")
fecha = open("1A.txt","w")
loop = int(abre.readline())
if 1 <= loop <= 1000: 
    anterior,total,dif = 0,0,0
    for x in range (loop):
        line = abre.readline()
        line = line.strip("\n")
        a = int(line)
        if 0<= a <=10000:
            if (a >= anterior):
                total += 10
            else: 
                dif = a+10 - anterior 
                total += dif 
            anterior = a + 10  
        else:
            fecha.write("Tempo fora do intervalo")
    fecha.write(str(total)+"\n")
    print(total)
else:
    fecha.write("Quantidade de pessoas fora do intervalo")
abre.close()
fecha.close()
    
