class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Lista_enlazada:
    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, data):
        self.head = Nodo(data=data, next=self.head)
        #nuevo_nodo = Nodo(data)
        #nuevo_nodo.next = self.head
        #return nuevo_nodo

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la lista enlazada
    def agregar_al_final(self, data):
      #Si la lista no existe, entonces se crea
        if not self.head:
            self.head = Nodo(data=data)
            return
        #recorre toda la lista hasta llegar al final,
        #cuando temporal.next=None
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        #Cuando llega al final de la lista, enlaza el último nodo con
        #el nuevo nodo que se crea
        temporal.next = Nodo(data=data)

    # Método para eleminar nodos
    def delete_node(self, key):
        actual = self.head
        previo = None
        #Se busca el dato a eliminar en la lista
        while actual and actual.data != key:
            previo = actual
            actual = actual.next
        #Si el dato a eliminar es el primero,
        #entonces se reasigna la cabeza de la lista
        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" --> ")
            node = node.next
    
    # Método para agregar un dato en una posición
    def agregar_en_posicion(self, data, pos):
        temp= self.head
        previo=None
        cont=1
        while(temp and cont!= pos):
            previo = temp
            temp=temp.next
            cont=cont+1
        if previo is None:
            self.head= Nodo(data = data, next= self.head)
        else:
            agregar= Nodo(data= data, next=temp)
            previo.next = agregar

    # Método para mover un dato 
    def Mover_dato(self, jugador, posiciones, direccion):
        temporal= self.head
        encontro=0
        pos=0
        while temporal != None:
            pos=pos+1
            if(temporal.data==jugador):
                encontro=1
                break
            temporal=temporal.next
        if(encontro==1):
            self.delete_node(jugador)
            if(direccion==1):
                self.agregar_en_posicion(jugador, pos+posiciones)
                print("El movimiento ha sido realizado. ")
            else:
                self.agregar_en_posicion(jugador, pos-posiciones)
                print("El movimiento ha sido realizado. ")
        else:
            print("El jugador no existe. ")

    # Método para eliminar datos repetidos en una lista
    def eliminar_repetidos(self):
        dato= self.head
        while(dato.next is not None):
            dato2=dato.next
            previo=dato
            while(dato2.next is not None):
                if(dato.data == dato2.data):
                    previo.next=dato2.next
                previo=dato2
                dato2=dato2.next
            dato=dato.next
    
    # Método para eliminar secuencias ascendentes 
    def eliminar_secuencias(self):
        previo=None
        dato=self.head
        while(dato.next is not None):
            if(dato.next.data==dato.data+1):
                previo.next=dato.next.next
                dato=dato.next
            else:
                previo=dato
                dato=dato.next
            

