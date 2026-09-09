import random

print("Jogo de Adivinhação")
print("Tente adivinhar o número que estou pensando entre 1 e 100")
print("Você tem 7 tentativas para acertar o número secreto.")

numero_secreto = random.randint(1,100)  

contador = 7
acertou = False

while contador > 0:
    print(f'Você tem {contador} tentativas restantes.')
    contador -= 1
    tentativa = int(input("Digite o seu palpite: "))
    if tentativa == numero_secreto:
      print("Parabéns! Você acertou!")
      acertou = True
      break
    elif tentativa < numero_secreto:
      print("O número secreto é maior do que o seu palpite.")
    else:
     print("O número secreto é menor do que o seu palpite.")

if not acertou:
    print("Você perdeu! O número secreto era:", numero_secreto)
else:
    print("Você acertou o número secreto em", 7 - contador + 1, "tentativas!")