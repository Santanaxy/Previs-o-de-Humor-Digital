nome = input("NOME DO USÚARIO: ")

energia = int(input("DIGITE SEU NIVEL DE ENERGIA: "))
              
if energia <= 19: 
    print("EXAUSTO")
if energia >= 20 and energia >= 39:
    print("CANSADO")
if energia >= 40 and energia >= 59: 
    print("Neutro")
if energia  >=60 and energia <= 79:
    print("ANIMADO")
if energia <= 80 and energia <= 100:
    print("EUFÓRICO")
else: 
    print("ENERGIA INVÁLIDA") 