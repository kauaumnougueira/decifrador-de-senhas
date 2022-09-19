#tratar a senha enviada
from neuronio.Decifrar import *


class Tratamento():

    def __init__(self, senha):
        if type(senha) is list:
            print("safe é array")
        else:
            print("n é array")
            self.senha = senha
            self.array_senha = list(self.senha)
            if len(self.array_senha) == 8:
                decifrar = Decifrar(self.array_senha)
                print(self.array_senha)
                decifrar.decifrar()
            else:
                print("Senha em formato errado, favor corrigir")
            