secret_number = 777

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

number = int(input("digite o seu palpite: "))

while number != secret_number:
    print("Ha ha! Você está preso no meu circuito!", number)

print("Outside the loop.", number)
 