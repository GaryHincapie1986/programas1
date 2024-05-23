# 1. Escriba un programa para encontrar el máximo entre tres números.
A=float(input("Cual es el numero A?, \t"))
B=float(input("Cual es el numnero B?, \t"))
C=float(input("Cual es el numnero C?, \t"))
if A>B and A>C:
    print("A es mayor que B y C")
elif B>A and B>C:
    print("B es Mayor que A y C")
elif C>A and C>B:
    print("C es mayor que A y B")
elif A==B and C==A:
    print("A=B=C")
    
    