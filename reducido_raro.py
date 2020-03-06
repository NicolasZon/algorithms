import numpy as np
from sympy import *

def reducir_sistema():

    sistema_correcto="NO"

    while not(sistema_correcto=="SI"):
        n=input("Número de ecuaciones: ",)
        m=input("Número de variables: ")
        n, m=int(n), int(m)

        sistema_ampliado=np.matrix(np.zeros((n,m+1)))

        print("Ingrese los coeficientes:")
        for i in range(0,n):
            for j in range(0,m):
                print("Ecuación %s, variable %s: " %((i+1),(j+1)))
                sistema_ampliado[i,j]=input()

        print("Ingrese los resultados:")
        for i in range(0,n):
            print("Ecuación %s, " % (i+1))
            sistema_ampliado[i,m]=input()

        print(sistema_ampliado)
        sistema_correcto=input("Si el sistema es correcto escriba: SI ")

    sistema_ampliado=Matrix(sistema_ampliado)
    reducido=sistema_ampliado.rref()
    print(reducido)

reducir_sistema()
