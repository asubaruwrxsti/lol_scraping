from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json
import os

# //*[@id="bltce2fa2f4ba0cba4f-section_1"]/section/div[2]/section[2]/div[2]
url = "https://www.leagueoflegends.com/en-us/champions/"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

class get_champions():

    def populate_champions(self, dump=True):
        driver.get(url)
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
        
        return self.scraped_champions

class get_champion():

    def __init__(self, champion):
        self.champion_name = champion
        self.champion_url = ""
        self.champion_stats = {}
        self.champion_spells = {}
        self.chamption_spell_images = {}
    
    def scrape_champion(self):
        pass

if __name__ == '__main__':
    champions = get_champions()
    