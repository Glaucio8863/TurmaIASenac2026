import random

print ("Role seus dados!")

lados = 0
numrol = 0
total = 0
dadrols = 0
modif = 0

while True:
    try:
        lados = int(input("Escolha quantos lados seus dados tem entre 2 e 100: "))
        numrol = int(input("Escolha quantos dados vão ser rolados: "))
        modif = int(input("Escolha um modificador: "))
        
        if lados > 100 or lados <2:
            print ("Não temos dados desse tamanho!")
           
            break
    
    except ValueError:
        print ("Não é um número!")
        break


    while dadrols != numrol:

        rolagem = random.randint (1,lados) + modif
        print (rolagem)
        total = total + rolagem
        dadrols = dadrols + 1
    
    print ("Sua rolagem foi ",total)
    break