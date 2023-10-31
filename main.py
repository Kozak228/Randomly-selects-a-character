from os import listdir
from random import choice

from Parser_data import Parser_data
from Create_and_remove_forders import proverka_or_create_dir

def main():
    # pars_data = Parser_data('https://paimon.moe/characters')
    #
    # pars_data.pars_data()

    path_dir = proverka_or_create_dir()

    path_dir_element = proverka_or_create_dir(path_dir, 'element', '')

    list_element_img = listdir(path_dir_element)

    random_element = choice(list_element_img)
    print(f"Element: {random_element[:random_element.rindex('.')]}")

    path_dir_element_characters = proverka_or_create_dir(path_dir, random_element[:random_element.rindex('.')], '')

    list_element_characters_img = listdir(path_dir_element_characters)

    random_element_characters = choice(list_element_characters_img)
    print(f"Characters: {random_element_characters[:random_element_characters.rindex('.')]}")

if __name__ == "__main__":
    main()