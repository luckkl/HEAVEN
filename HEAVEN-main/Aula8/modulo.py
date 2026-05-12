import os

def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b

def divisão(a, b):         
    return a/b


def Limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")