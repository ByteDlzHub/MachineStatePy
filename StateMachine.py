import StateBase
Node : str = "PRIMARY_NODE"
#PRIMARY_NODE es el father de los demas nodos a partir de el se crea lo demas

DefaultState = Node
ActualState=None

#Estructura de Grafo Dirigido
class Machine:
    def __init__(self, DefaultState) -> None:
        pass

#Clase Nodo     
#Cada Nodo puede conectar con infinitas Aristas o existir por si solo
class NODE(Machine):
    def __init__(self,DefaultState,vex) -> None:
        Machine.__init__(self, DefaultState)
        self.vex = vex
    
    def initialize_Node(self):
        pass

    def autodelete_Node(self):
        #Si se elimina un NODO debe eliminarlas Aristas que lo conectan tambien 
        pass 

#Clase Arista
#Cada Arista debe conectar con 2 Nodos como minimo 
class EDGE(NODE):   
    #Definir si las ctn=Conexiones existen
    def __init__(self,origin,vex) -> None:
        NODE.__init__(self,DefaultState,vex)
        self.origin = origin

# newclass = NODE("Deafult", (0,1))
# newclassEdge = EDGE(newclass, newclass.vex)
# print(newclassEdge)