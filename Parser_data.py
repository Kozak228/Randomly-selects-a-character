from time import sleep
from random import randrange

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from Create_and_remove_forders import proverka_or_create_dir_data
from Write_file import write_file

class Parser_data():
    def __init__(self, url):
        self.url = url

        self.name_file = 'data'
        self.dict_all_links_data = {}

        self.path_main_dir = proverka_or_create_dir_data()

        self.browser = webdriver.Chrome()

    def pars_data(self):
        try:
            self.browser.get(self.url)
            sleep(randrange(9))

            soup = BeautifulSoup(self.browser.page_source, "lxml")

            list_img_tags_element = soup.find_all('img', class_="w-8 h-8")

            list_links_on_img_element = ['https://paimon.moe' + i.get('src') for i in list_img_tags_element[:7]]
            list_names_element = [i.get('alt') for i in list_img_tags_element[:7]]

            self.dict_all_links_data['names_element'] = list_names_element
            self.dict_all_links_data['links_on_img_element'] = list_links_on_img_element

            sleep(2)

            for characters_with_elem in range(len(list_names_element)):
                self.browser.find_element(By.XPATH,
                                     f"// *[ @ id = 'sapper'] / main / div / div[2] / div[1] / div[1] / div[2] // div[1] / button[{characters_with_elem + 1}]").click()

                sleep(5)

                soup = BeautifulSoup(self.browser.page_source, "lxml")

                list_img_tag_characters = soup.find_all("img", class_="w-full h-full")

                list_links_on_img_characters = ['https://paimon.moe' + i.get('src') for i in list_img_tag_characters]

                self.dict_all_links_data[list_names_element[characters_with_elem]] = list_links_on_img_characters

                sleep(3)

                self.browser.find_element(By.XPATH,
                                     f"// *[ @ id = 'sapper'] / main / div / div[2] / div[1] / div[1] / div[2] / div[1] / button[{characters_with_elem + 1}]").click()

                sleep(1)

            write_file(self.dict_all_links_data, self.name_file, self.path_main_dir)

        except Exception as ex:
            print(ex)
        finally:
            self.browser.close()
            self.browser.quit()
