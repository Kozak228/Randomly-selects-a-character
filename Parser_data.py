from time import sleep
from random import randrange

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import get

from Create_and_remove_forders import proverka_or_create_dir

class Parser_data():
    def __init__(self, url):
        self.url = url
        self.path_main_dir = proverka_or_create_dir()

        self.browser = webdriver.Chrome()

    def pars_data(self):
        try:

            self.browser.get(self.url)
            sleep(randrange(9))

            soup = BeautifulSoup(self.browser.page_source, "lxml")

            list_img_tags_element = soup.find_all('img', class_="w-8 h-8")

            list_links_on_img_element = ['https://paimon.moe' + i.get('src') for i in list_img_tags_element[:7]]
            list_names_element = [i.get('alt') for i in list_img_tags_element[:7]]

            path_secondary_dir = proverka_or_create_dir(self.path_main_dir, 'element',"")

            self.download_image(path_secondary_dir, list_links_on_img_element)

            sleep(2)

            for characters_with_elem in range(len(list_names_element)):
                self.browser.find_element(By.XPATH,
                                     f"// *[ @ id = 'sapper'] / main / div / div[2] / div[1] / div[1] / div[2] // div[1] / button[{characters_with_elem + 1}]").click()

                sleep(5)

                soup = BeautifulSoup(self.browser.page_source, "lxml")

                list_img_tag_characters = soup.find_all("img", class_="w-full h-full")

                list_links_on_img_characters = ['https://paimon.moe' + i.get('src') for i in list_img_tag_characters]

                path_secondary_dir = proverka_or_create_dir(self.path_main_dir, list_names_element[characters_with_elem], "")

                self.download_image(path_secondary_dir, list_links_on_img_characters)

                sleep(5)

                self.browser.find_element(By.XPATH,
                                     f"// *[ @ id = 'sapper'] / main / div / div[2] / div[1] / div[1] / div[2] / div[1] / button[{characters_with_elem + 1}]").click()

                sleep(5)

        except Exception as ex:
            print(ex)
        finally:
            self.browser.close()
            self.browser.quit()

    def download_image(self, path_dir, links):
        print('\n')

        cnt_links = len(links)
        cnt_link = 0

        for i in links:
            req = get(i)
            response = req.content

            with open(f'{path_dir}{i[i.rindex("/") + 1:]}', 'wb') as f:
                f.write(response)

            cnt_link += 1
            print(f"Downloading: {cnt_link}/{cnt_links}")

            sleep(0.2)