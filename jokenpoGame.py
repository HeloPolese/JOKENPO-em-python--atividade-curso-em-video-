import random
from time import sleep
user = int(input("Digite:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA  "))
options = ["PEDRA", "PAPEL", "TESOURA"]
computador = random.choice(options)

print("\nEscolha do computador: {}".format(computador) )
print("Escolha do user: {}".format(options[user]) )

print("\nJO")
sleep(1)
print("KEN")
sleep(1) #sleep é tipo uma pausa antes da msg
print("PO!\n")

if user == 0 and computador == "PEDRA":
    print("EMPATE")
elif user == 0 and computador == "TESOURA":
    print("PARÁBENS USER! VOCÊ GANHOU!")
elif user == 0 and computador == "PAPEL":
    print("VOCÊ PERDEU!")

elif user == 1 and computador == "PAPEL":
    print("EMPATE!")
elif user == 1 and computador == "PEDRA":
    print("PARÁBENS USER! VOCÊ GANHOU!")
elif user == 1 and computador ==  "TESOURA":
    print("VOCÊ PERDEU!")

elif user == 2 and computador == "TESOURA":
    print("EMPATE!")
elif user == 2 and computador ==  "PAPEL":
    print("PARÁBENS USER! VOCÊ GANHOU!")
elif user == 2 and computador == "PEDRA":
    print("VOCÊ PERDEU!")
else:
    print("DIGITE UM NÚMERO DE 0 A 2!")

