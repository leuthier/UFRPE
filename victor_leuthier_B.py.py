##import sys
##abre = open(sys.argv[1], "r")
##sai = open(sys.argv[2], "w")
abre = open("B.txt", "r")
sai = open("B2.txt", "w")

quad1 = abre.readline()
quad2 = abre.readline() 
lista_a = quad1.split(" ")
lista_b = quad2.split(" ")

a_x0, a_x1 = int(lista_a[0]), int(lista_a[2])
a_y0, a_y1 = int(lista_a[1]), int(lista_a[3])
b_x0, b_x1 = int(lista_b[0]), int(lista_b[2])
b_y0, b_y1 = int(lista_b[1]), int(lista_b[3])

alt_a = a_y1 - a_y0
alt_b = b_y1 - b_y0
larg_a = a_x1 - a_x0
larg_b = b_x1 - b_x0

verifica1 = b_x0 + larg_b
verifica2 = b_y0 + alt_b
verifica3 = a_x0 + larg_a
verifica4 = a_y0 + alt_a
if a_x0 > verifica1 :
    result = "0"
elif a_y0 > verifica2:
    result = "0"
elif b_x0 > verifica3 :
    result = "0"
elif b_y0 > verifica4:
    result = "0"
else:
    result = "1"

sai.write(result)
sai.close()
abre.close()
