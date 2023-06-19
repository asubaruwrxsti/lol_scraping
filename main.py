from typing import Any
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json
import os

# //*[@id="bltce2fa2f4ba0cba4f-section_1"]/section/div[2]/section[2]/div[2]
main_page_url = "https://www.leagueoflegends.com/en-us/champions/"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

class get_champions():

    def populate_champions(self, dump=True):
        driver.get(main_page_url)
        champion_wrapper = driver.find_element(By.XPATH, '//*[@id="bltce2fa2f4ba0cba4f-section_1"]/section/div[2]/section[2]/div[2]')
        champions = champion_wrapper.find_elements(By.TAG_NAME, 'a')
        for champion, i in zip(champions, range(len(champions))):
            self.scraped_champions.append({champion.text: champion.get_attribute('href')})
        
        if dump:
            with open('champions.json', 'w') as f:
                json.dump(self.scraped_champions, f)
        
        driver.quit()
    
    def clean_files(self):
        os.remove('champions.json')
    
    def update_champions(self):
        self.clean_files()
        self.populate_champions()

    def __init__(self):
        self.scraped_champions = []
        
        if not os.path.exists('champions.json'):
            self.populate_champions()
        else:
            with open('champions.json', 'r') as f:
                self.scraped_champions = json.load(f)
        
    def get_champions(self):
        return self.scraped_champions

class get_champion():

    def __init__(self, champion):
        self.champion_name = list(champion.keys())[0]
        self.champion_url = list(champion.values())[0]
        self.champion_abilities = {}
        self.champion_images = {}
    
    # //*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]
    def scrape_champion_abilities(self):
        driver.get(self.champion_url)
        abilities = driver.find_elements(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]')
        for ability in abilities:
            print(ability.text)

    def scrape_champion_images(self):
        pass

    def dump_champion(self):
        pass
    
    def scrape_champion(self):
        driver.get(self.champion_url)
        self.scrape_champion_abilities()
        self.scrape_champion_images()
        self.dump_champion()

if __name__ == '__main__':
    all_champions = get_champions().get_champions()
    for champion in all_champions:
        champion = get_champion(champion)
        champion.scrape_champion()
        break