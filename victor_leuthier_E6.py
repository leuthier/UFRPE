class Node:
    def __init__(self, data):
        self.data = data
        self.PreviousNode = None
        self.NextNode = None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data
    def getPreviousNode(self):
        return self.PreviousNode
    def setPreviousNode(self,antes):
        self.PreviousNode = antes
    def getNextNode(self):
        return self.NextNode
    def setNextNode(self,prox):
        self.NextNode = prox
  
class List:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
    def isEmpty(self):
        return self.firstNode is None
    def __str__(self):
        if self.isEmpty():
            return
        correntNode = self.firstNode
        string = ""
        while correntNode is not None:
            string += str( correntNode.getData() ) + " "
            correntNode = correntNode.getNextNode()
        return string
    def show(self):
        if self.isEmpty():
            return
        node = self.lastNode
        words = ''
        while node != None:
            words += str(node.getData())
            if node != self.firstNode:
                words += " "
            node = node.getPreviousNode()
        fecha.write(words)
        return
    def search(self,valor):
        if self.isEmpty():
            return
        nodeS = self.firstNode
        while nodeS != None:
            if nodeS.getData() == valor:
                return nodeS
            nodeS= nodeS.getNextNode()
        return None
    def insertAtBegin(self, value):
        newNode = Node(value)  
        if self.isEmpty():  
            self.firstNode = self.lastNode = newNode
        else:
            newNode.setNextNode(self.firstNode)
            newNode.getNextNode().setPreviousNode(newNode)
            self.firstNode = newNode  
    def removePos(self, value):
        if self.isEmpty():
            return None
        nodeDel = self.search(value)
        if nodeDel != None:
            before = nodeDel.getPreviousNode()
            after = nodeDel.getNextNode()
            if before == None and after == None:
                self.firstNode = self.lastNode = None
            elif before == None:
                after.setPreviousNode(None)
                self.firstNode = after
            elif after == None:
                before.setNextNode(None)
                self.lastNode = before
            elif after != None and before != None:
                before.setNextNode(after)
                after.setPreviousNode(before)
                
class Fila(List):
    def __init__(self):
        List.__init__(self)
    def insert(self, value):
        self.insertAtBegin(value)
    def delete(self):
        numero = self.lastNode.getData()
        if numero == None:
            return 
        self.removePos(numero)
        return numero
    
import sys        
abre = open(sys.argv[1],"r")
fecha = open(sys.argv[2],"w")
pessoas = int(abre.readline())
if 1<= pessoas <= 50000:
    fila = abre.readline().strip("\n").split(" ")
    qtTirar = int(abre.readline())
    if 1<= qtTirar  <= 50000 and qtTirar < pessoas:
        remover = abre.readline().strip("\n").split(" ")
        objetoLista = Fila()
        for x in range(pessoas):
            objetoLista.insert(int(fila[x]))
        for a in range(qtTirar):
            objetoLista.removePos(int(remover[a]))
        objetoLista.show()
        abre.close()
        fecha.close()