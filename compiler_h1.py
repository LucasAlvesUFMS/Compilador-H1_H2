from porta_cartao import *

class Calculadora():
    def __init__(self, input_ee):
        if input_ee:
            self.acumulador_Calc = input_ee
        else:
            self.acumulador_Calc = None

    def mudar_acumulador(self, input_ee):
        self.acumulador_Calc =  input_ee

    def soma(self, input_ee):
        return self.acumulador_Calc + input_ee

    def subtracao(self, input_ee):
        return self.acumulador_Calc - input_ee
    
    def divisao(self, input_ee):
        return self.acumulador_Calc/input_ee
    
    def multi(self, input_ee):
        return self.acumulador_Calc*input_ee
    
#Chico 
class Compilador():

    def __init__(self) -> None:
        self.p_cartao =  PortaCartao()
        
    def check_cartao(self, cartao_cod):
        #checa se a sintaxe do cartão esta correto para execução
        if len(cartao_cod) > 3 or len(cartao_cod) < 3:
            return SyntaxError('Cartão maior que 3 algarismos')
        if int(cartao_cod[1:]) > 99 or int(cartao_cod[1:]) < 0:
            return SyntaxError('EE incorreto')
        
    def execute(self):
        qnt_cartao =  int(input())
            

  