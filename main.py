from random import randint, choice
from sys import exit
from os import system

def main():
    list_elements = ["Пиро", "Гидро", "Анемо", "Электро", "Дендро", "Крио", "Гео"]

    while True:
        system("cls || clear")

        print(f"Элемент: {choice(list_elements)}\n")

        last_chislo = int(input("Введите количество персонажев элемента -> "))

        print(f"Персонаж под номером: {randint(1, last_chislo)}\n")

        question = input("Для продолжения, введите - '1';\nДля выхода - '0';\nВаш выбор -> ")

        if question == "0":
            exit()

if __name__ == "__main__":
    main()