class No:
	def __init__(self,valor=None):
		self.valor=valor
		self.prox=None
		self.ant=None
	def getValor(self):
		return self.valor
	def setValor(self,valor):
		self.valor = valor
	def getProximo(self):
		return self.prox
	def setProximo(self,prox):
		self.prox=prox
	def getAnterior(self):
		return self.ant
	def setAnterior(self,ant):
		self.ant=ant
class Lista:
	def __init__(self):
		self.inicio=None
		self.fim=None
	def estavazio(self):
		return((self.inicio==None) and (self.fim==None))
	def inserir(self,valor):
		novono = No(valor)
		if self.estavazio():
			self.inicio=novono
			self.fim=novono
		else:
			novono.setProximo(self.inicio)
			self.inicio.setAnterior(novono)
			self.inicio=novono
	def buscar(self,valor):
		if self.estavazio():
			return None
		prim = self.inicio
		if prim.getValor()==None:
			return
		while(prim!=None):
			if prim.getValor() == valor:
				return prim
			prim = prim.getProximo()
		return None
	def excluir(self,valor):
		if self.estavazio():
			return None
		busca = self.buscar(valor)
		noanterior = busca.getAnterior()
		noprox = busca.getProximo()
		if noanterior == None and noprox == None:
			self.inicio = None
			self.fim = None
		elif noanterior == None:
			noprox.setAnterior(None)
			self.inicio = noprox
		elif noprox == None:
			noanterior.setProximo(None)
			self.fim = noanterior
		else:
			noanterior.setProximo(noproximo)
			noproximo.setAnterior(noanterior)

class pilha(Lista):
	def __init__(self):
		Lista.__init__(self)
	def empilhar(self,valor):
		self.inserir(valor)
	def desempilhar(self):
		elemento = self.inicio.getValor()
		self.excluir(elemento)
		return elemento


import sys
abre = open(sys.argv[1],"r")
fecha = open(sys.argv[2],"w")
tudo = abre.read().split("\n")
words = ""
qtLinha = int(tudo[0])
for a in range(1,qtLinha+1):
    tudo[a] = list(tudo[a])
    duracell = pilha()
    for b in range(len(tudo[a])):
        if tudo[a][b] == "(" or tudo[a][b] == "[" or tudo[a][b] == "{":
            duracell.empilhar(tudo[a][b])
        else:
            if duracell.estavazio():
                if tudo[a][b] == ")" or tudo[a][b] == "}" or tudo[a][b] == "]": 
                    duracell.empilhar(tudo[a][b])
                    words += "N\n"
                    break
            remover = duracell.desempilhar()
            if tudo[a][b] == "}" and remover == "{":
                    continue
            elif tudo[a][b] == "]" and remover == "[":
                    continue
            elif tudo[a][b] == ")" and remover == "(":
                    continue
            else:
                    duracell.empilhar(tudo[a][b])
                    words += "N\n"
                    break   
    if duracell.estavazio():
        words += "S\n"
    else:
        remover1 = duracell.desempilhar()
        if remover1 == "(" or remover1 == "[" or remover1 == "{":
            words += "N\n"      
                    
fecha.write(words+"\n")
abre.close()
fecha.close()



