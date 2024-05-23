P=input("vive con su padre?, \n")
if P =="si":
    print("Eres el bebe de papi")
else:
    print("Tu papi tiene otro hogar")
    
M=input("vive con su madre?, \n")
if M =="si":
    print("estas viejo, vete de tu casa")
else:
    print("bien, ella necesita vida")
    
if P=="si"and M== "si":
    print("Familia Nuclear")
else:
    print("Monoparental")
