import numpy as np

alfabeto = "abcdefghijklmnopqrstuvwxy0123456789!@#$%&?"
list(alfabeto) #array alfabeto

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
senha = "a???????"
list(senha)
senha_decifrada = []

um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
sete = 0
oito = -1


def decifrar(senha):
    for i in range(294):
        oito += 1 #sempre adciona um ao utimo elemtno da senha
        if(i == 42): #ja tiver passado pelos 42
            sete += 1 
        if(i == 84):
            seis += 1
        if(i == 126):
            cinco += 1
        if(i == 168):
            quatro += 1
        if(i == 210):
            tres += 1
        if(i == 252):
            dois += 1
        if(i == 294):
            um += 1
            
        senha_decifrada = alfabeto[um], alfabeto[dois], alfabeto[tres], alfabeto[quatro], alfabeto[cinco], alfabeto[seis], alfabeto[sete], alfabeto[oito]
        np.array_equal(senha, senha_decifrada) #compara as senhas