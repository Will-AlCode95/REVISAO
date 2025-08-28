print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

acerto = 777

while True:  #condição começa como True
    numero = int(input("Digite o seu palpite: "))
    if numero == acerto:
        break  # sai do loop se ele digitar: 777
    print(f"Ha ha! Você está preso no meu circuito!")   #esse print esta dentro do loop

print("Muito bem, trouxa! Você está livre agora.") #saiu do loop(condição while se torna false) e executou o print
