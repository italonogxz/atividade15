# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
reta1AB = float(input("Digite o valor da primeira reta: "))
reta2BC = float(input("Digite o valor da segunda reta: "))
reta3AC = float(input("Digite o valor da terceira reta: "))
if reta1AB + reta2BC > reta3AC:
    print("Positivo! 👍")
else:
    print("Negativo! 😅")
    