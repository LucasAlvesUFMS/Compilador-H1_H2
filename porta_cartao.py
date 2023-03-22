#A implentação do porta catões pode ser entendida como uma 
#Linked List -  Queue -  Lista de Tuples
class Cartao:
    #Seja o cartão 701
    def __init__(self,cod_cartao,valor = None, next = None) -> None:
                
        self.id_gaveta =  int(cod_cartao[1:]) #ID gaveta  =  01
        self.instrucao =  int(cod_cartao[0]) #Instrução  =  7 
        self.valor  = valor #O valor inserido pelo usuario 
        self.next =  next
    
class PortaCartao:
    def __init__(self) -> None:
        self.head = None

    def check_IDGaveta(self,cod_cartao):
        if(self.head):
            current = self.head
            while(current):
                if current.id_gaveta ==  int(cod_cartao[1:]):
                     print('Gaveta já em uso')
                     break
                current = current.next
        else:
            pass

    def inserir(self, cod_cartao, valor  = None):
        self.check_IDGaveta(cod_cartao)

        if cod_cartao [0] == 7:
            valor =  int(input())
        
        novoCartao = Cartao(cod_cartao,valor)

        if(self.head):
            current =  self.head
            while(current.next):
                current = current.next
            current.next =  novoCartao
        else:
            self.head =  novoCartao
