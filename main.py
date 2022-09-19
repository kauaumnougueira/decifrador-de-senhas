from neuronio.Tratamento import *

senha = ""
print("-----------------------------------")
print("-Digite sua senha de 8 caracteres: ")
print("-----------------------------------")

def pega_senha():
    senha = input(">")
    tratamento = Tratamento(senha)

pega_senha()