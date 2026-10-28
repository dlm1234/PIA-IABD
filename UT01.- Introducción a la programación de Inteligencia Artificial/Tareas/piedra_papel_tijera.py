import random

# Definir constantes
PIEDRA = "piedra"
PAPEL = "papel"
TIJERA = "tijera"

# Definir una función que decida quién gana
def decidir_ganador(user_action, computer_action):
    if user_action == computer_action:
        return "Usuario y ordenador eligieron " + user_action + ". ¡Empate!"
    elif user_action == PIEDRA:
        if computer_action == TIJERA:
            return "Piedra rompe tijera. ¡Ganaste!"
        else:
            return "Papel envuelve piedra. ¡Perdiste!"
    elif user_action == PAPEL:
        if computer_action == PIEDRA:
            return "Papel envuelve piedra. ¡Ganaste!"
        else:
            return "Tijera corta papel. ¡Perdiste!"
    elif user_action == TIJERA:
        if computer_action == PAPEL:
            return "Tijera corta papel. ¡Ganaste!"
        else:
            return "Piedra rompe tijera. ¡Perdiste!"
    else:
        return "Acción inválida. Por favor elige piedra, papel o tijera."

# Definir main() → bucle de juego
def main():
    while True:
        user_action = input("Elige una opción: piedra, papel o tijera (CTRL+C para salir): ")
        computer_action = random.choice([PIEDRA, PAPEL, TIJERA])

        print("Elegiste " + user_action + ". El ordenador eligió " + computer_action + ".")
        print(decidir_ganador(user_action, computer_action))

main()


