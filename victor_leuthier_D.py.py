##import sys
##abre = open(sys.argv[1],"r")
##sai = open(sys.argv[2],"w")

abre = open("D.in","r")
sai = open("D.out","w")

qtd = abre.readline()
nums = abre.readline()
esp = str(nums)
if (2 <= int(qtd) <= 1000):
    separa = esp.split()
    menor = int(separa[0])
    for i in range (len(separa)):
        if int(separa[i])<menor:
            menor = int(separa[i])
    for a in range (menor,int(qtd)+1):
        if str(a) not in separa:
            result = a 
            falta = str(result)+" "
            sai.write(falta)  
else:
    sai.write("N fora do intervalo")
abre.close()
sai.close()
