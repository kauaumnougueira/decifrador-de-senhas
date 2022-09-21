import numpy as np

class Decifrar():

    def __init__(self, array_senha):
        self.senha = array_senha

    alfabeto = "abcdefghijklmnopqrstuvwxyz30123456789!@#$%&?"
    alfabetoarray = list(alfabeto) #array alfabeto

    '''
    testar combinações divididas em 8
    ex: abcd1234
    exemplo de testes:
    1-aaaaaaaa
    2-aaaaaaab
    3-aaaaaaac
    ...
    n-aaaaaab? (rodou todos do ultimo)
    depois comparar com a senha do parametro
    '''
    senha_decifrada = []

    def decifrar(self):
        for i in range(43): #1
            for j in range(43): #2
                for k in range(43): #3
                    for l in range(43): #4
                        for m in range(43): #5
                            for n in range(43): #6
                                for o in range(43): #7
                                    for p in range(43): #8.
                                        senha_decifrada = [self.alfabetoarray[i], self.alfabetoarray[j], self.alfabetoarray[k], self.alfabetoarray[l], self.alfabetoarray[m], self.alfabetoarray[n], self.alfabetoarray[o], self.alfabetoarray[p]]
                                        print("senha gerada: ", senha_decifrada)
                                        if np.array_equal(self.senha, senha_decifrada): 
                                            print("achei, a senha é: ", senha_decifrada) 
                                            senhaDecifrada = "".join(senha_decifrada)
                                            return senhaDecifrada
                                            break
