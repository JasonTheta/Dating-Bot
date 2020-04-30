from time import sleep
from selenium import webdriver

class OKCBot():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://okcupid.com/login")
        sleep(2)

        usrfld=self.driver.find_element_by_xpath('//*[@id="username"]')
        usrfld.click()
        usrfld.send_keys('Username')

        pw_in=self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.click()
        pw_in.send_key('Passwort')

        next=self.driver.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input')
        next.click()

        
    def like(self):
        like_btn=self.driver.find_element_by_xpath('//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[2]')
        like_btn.click()
        sleep(3)

    def dislike(self):
        dislike_btn=self.driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[1]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[1]')
        dislike_btn.click()

    def testmatch(self):
        
        match=self.driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[1]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[1]/div[4]')
        perc=match.get_attribute('innerHTML')
        try:
            perc     #<span class="cardsummary-reflux-match-pct">63%</span> Match

        except:
            print("Übereinstimmung konnte nicht gefunden werden")
            
        try:    
            h=int(perc[43])+int(perc[44])
            h=int(h)
            if h>=75:
                self.like()
            else:
                self.dislike()
        except:
            print("Konnte nicht swipen")