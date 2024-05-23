C=input("Digita tu caracter, yo describo la naturaleza la naturaleza \t")
X=ord(C)
# if X !=ord(97:122):
#     print("X no es letra del alfabeto")
# if X=ord(97:122):
#     print("X es letra del alfabeto")

if X >=65 and X<= 122 and not(X >=90 and X<= 96):
    print("Resultado es letra del alfabeto")
else:
    print("Resultado no es letra del alfabeto")
