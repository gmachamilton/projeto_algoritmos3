class Node:
    def __init__(self, valor = None,chave = None, lista = [None]*10):
        self.__valor = valor
        self.__chave = chave
        self.__lista = lista
        def get_lista(self):
            return self.__lista
        def set_lista(self, lista):
            self.__lista = lista
        def get_valor(self):
            return self.__valor
        def set_valor(self, valor):
            self.__valor = valor
        def get_chave(self):
            return self.__chave
        def set_chave(self, chave):
            self.__chave= chave

class Indice:
    def __init__(self):
        self.__raiz = Node()
    def inserir(self, chave, valor):
        atual = self.__raiz
        for x in chave:
            atual.get_lista[int(x)]
            if atual.get_lista[x] == Node():
                    atual.get_lista[int(x)] = Node(x, valor)
                    atual = atual.get_lista[int(x)]
            else:
                atual = atual.get_lista[int(x)]               
        atual.valor = valor        
                
     return
    
    #def __getitem__:
    #def __setitem__:    
    #def pesquisar(self, key):  
