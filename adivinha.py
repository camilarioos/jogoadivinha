print("Jogo de Adivinhação")
print("Tente adivinhar o número que estou pensando entre 1 e 100")
import random
numero_secreto = random.randint(1,100)  # Número que o jogador
tentativa = int(input("Digite o seu palpite: "))
if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
elif tentativa < numero_secreto:
    print("O número secreto é maior do que o seu palpite.")
else:
    print("O número secreto é menor do que o seu palpite.")

print("O número secreto era:", numero_secreto)
