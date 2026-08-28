qsa=0
r=0
maxq=0
a=0
g=0

r=int(input("Insira r: "))
maxq=int(input("Insira MaxQ: "))
a=int(input("Insira a: "))
r=int(input("Insira r: "))
g=int(input("Insira g: "))
      
qsa=qsa+a*(r+g*maxq-qsa)

print("QSA atual é", qsa)