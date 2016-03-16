##import sys
##x = open(sys.argv[1],"r")
##y = open(sys.argv[2],"w")
x = open("A.in", 'r')
y = open("A.out", 'w')
vez = x.readline()
vezes = int(vez)
for i in range (1, (vezes+1)):
    linha = x.readline() 
    sem_espaco = linha.split(" ") 
    a = int(sem_espaco[0]) 
    c = int(sem_espaco[1])
    vazia = " "    
    for b in range (0,c): 
        if ((a*b)% c==1):
            vazia +="Caso "+str(i)+": "+str(b)+"\n"
            y.write(vazia)
            break
    else:
        vazia +="Caso "+str(i)+": "+"muito dificil"+"\n"          
        y.write(vazia)
x.close()
y.close()


