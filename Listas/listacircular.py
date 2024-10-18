import random

from listaenlazada import Lista_enlazada

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class Lista_Circular(object):

    def __init__(self):
        self.head = None

    def is_empty(self):

        return self.head is None

    def length(self):

      cur = self.head
      count = 0
      while cur is not None:
          count += 1
                  # Si el siguiente nodo del nodo actual es el nodo principal, significa que este nodo es el nodo de cola
                  # Si no, mueva el puntero hacia atrás
          if cur.next == self.head:
              break
          else:
              cur = cur.next
      return count

    def imprimir(self):

      if self.is_empty():
          return
      cur = self.head
      print(cur.data)
      while cur.next != self.head:
          cur = cur.next
          print(cur.data, end = "-->")


    def add_first(self, data):

      node = Node(data)
      if self.is_empty():
          self.head = node
          node.next = self.head
      else:
          cur = self.head
                  # Mueva el puntero al nodo de cola
          while cur.next is not self.head:
              cur = cur.next
                  # El nodo de cola apunta al nuevo nodo
          cur.next = node
                  # El nuevo nodo apunta al nodo principal original
          node.next = self.head
                  # Luego dele el título del nodo principal al nuevo nodo
          self.head = node


    def add_last(self, data):

      node = Node(data)
      if self.is_empty():
          self.head = node
          node.next = self.head
      else:
          cur = self.head
                  # Mueve el puntero al final
          while cur.next is not self.head:
              cur = cur.next
                  # El nodo de cola apunta al nuevo nodo
          cur.next = node
                  # El nuevo nodo apunta al nodo principal
          node.next = self.head


    def insert_node(self, index, data):

      node = Node(data)
      if index < 0 or index > self.length():
          print ("Posición de inserción incorrecta")
          return False
      elif index == 0:
          self.add_first(data)
      elif index == self.length:
          self.add_last()
      else:
          cur = self.head
          pre = None # pre es el nodo anterior del nodo señalado por el puntero actual
          count = 0
                  # Mueva el puntero a la posición para insertar
          while count < index:
              pre = cur
              cur = cur.next
              count += 1
          pre.next = node
          node.next = cur

    def remove_node(self, data):

      if self.is_empty():
          return
          # Si el nodo que se va a eliminar es el nodo principal
      elif data == self.head.data:
          cur = self.head
          while cur.next != self.head:
              cur = cur.next
          cur.next = self.head.next
          self.head = self.head.next
      else:
          cur = self.head
          pre = None
                  # Mover a la posición del nodo que se va a eliminar
          while cur.data != data:
              pre = cur
              cur = cur.next
                  # Apunte el nodo precursor del nodo que se va a eliminar al nodo posterior, de modo que se omita el nodo central
          pre.next = cur.next


    def remove2_node(self, data):

      if self.is_empty():
          return
          # Si el nodo que se va a eliminar es el nodo principal
      elif data == self.head.data:
          cur = self.head
          while cur.next != self.head:
              cur = cur.next
          cur.next = self.head.next
          self.head = self.head.next
      else:
        cur = self.head
        pre = None
        while cur.data != data:
            pre = cur
            cur = cur.next
        #pre.next = cur.next
        pre.next = pre.next.next

#Creamos la lista de premios
premios=Lista_Circular()
premios.add_last("lanza de nuevo")
premios.add_last("100mil pesos")
premios.add_last("un viaje")
premios.add_last("un carro")
premios.add_last("una moto")
premios.add_last("un celular")
premios.add_last("1millon de pesos")
premios.add_last("eliminado del juego")
premios.add_last("un computador")
premios.add_last("una tablet")
premios.imprimir()
print("\n")

def juego(premios):
    jugador1=input("Ingrese el nombre del jugador 1: ")
    jugador2=input("Ingrese el nombre del jugador 2: ")
    jugador3=input("Ingrese el nombre del jugador 3: ")
    jugadores=Lista_enlazada()
    jugadores.agregar_al_final(jugador1)
    jugadores.agregar_al_final(jugador2)
    jugadores.agregar_al_final(jugador3)
    jugador=jugadores.head
    posicion=premios.head
    while(jugador is not None):
        print("Turno de ", jugador)
        print("1 - lanzar la ruleta.")
        print("2- salir")
        n=int(input())
        if(n==1):
            dado= random.randint(1,6)
            for i in range(dado):
                posicion=posicion.next
            if(posicion.data=="eliminado del juego"):
                print(jugador, "ha sido eliminado del juego.")
                jugador=jugador.next
            else:
                if(posicion.data=="lanza de nuevo"):
                    print(jugador, "debe lanzar de nuevo.")
                else:
                    print(jugador, "ha ganado ", posicion)
                    jugador=jugador.next
        else:
            print("El turno de", jugador," ha sido saltado.")
        
juego(premios)

