from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


####################################################
#   README
#
# You need to install selenium 
# you need to set email and password
# in terminal run $python3 -i swipingbot.py
# in python interpreter create new bot via:  bot=OKCBot()
# login via bot.login() 
# you may manually type in your security code from your smartphone
# if you are logged in and doubletake is displayed you can start swiping using bot.testmatch()
# for 1000 testmatch in a row use bot.testmatchloop()
# Enjoy
#
#
# Known Bugs:
#
# cannot find xpath
# the most occuring error is that the bot cannot find the button to select. remeber that zou need to SELECT
# using .find_element_by_xpath('/path'). Sometimes the element is blocked by other element. Sometimes the path changes,
# so you need to go to your browser rightclick the element you couldnt reach and copy xpath and replace it in your script.
# This is why so many steps have to be taken manually, so you can tell where exactly the bot failed.  
#
# infinte loop
# when the swiping bot hit like it proceeds to repeat the message ("One of us!") and cannot move one ... dont know how to fix this.
# let me know on github or per 
#
# if you want to get in contact reach me per mail: contact@theta-computing.net
#
#####################################################

class OKCBot():
    def __init__(self):
        self.driver1 = webdriver.Firefox()
        
        sleep(2)

    def login(self):
        self.driver1.get("https://okcupid.com/login")
        
        sleep(2)

        usrfld=self.driver1.find_element_by_xpath('//*[@id="username"]')
        usrfld.click()
        usrfld.send_keys('example@mail')                                        # <-- setmail here

        pw_in=self.driver1.find_element_by_xpath('//*[@id="password"]')
        pw_in.click()
        pw_in.send_keys('examplepasswort')                                      # <-- set password here

        next=self.driver1.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input')
        next.click()

        
    def like(self):
        try:
            like_btn=self.driver1.find_element_by_xpath('//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[2]')
            like_btn.click()
            sleep(3)
        except:
            print("Fail")

    def dislike(self):                  
        dislike_btn=self.driver1.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div') 
        dislike_btn.click()

    def testmatch(self):
        #scan bio for vegan
        hb=0
        try:
            bio=self.driver1.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div/div[2]/div/div/p')
            selfdescript=bio.get_attribute('innerHTML')
        
            i=0
            hb=0
            for a in selfdescript:
                if selfdescript[i]=="v" or selfdescript[i]=="V":
                    if selfdescript[i+1]=="e" or selfdescript[i+1]=="E":
                        if selfdescript[i+2]=="g" or selfdescript[i+2]=="G":
                            if selfdescript[i+3]=="a" or selfdescript[i+3]=="A":
                                if selfdescript[i+4]=="n" or selfdescript[i+4]=="N":
                                    hb=True
                                    print("One of us!")
                else:
                    hb=False
        except:
            print("No selfdescription")
            hb=False
        try:           
            match=self.driver1.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/span[4]')
            perc=match.get_attribute('innerHTML')    
         
        except:
            print("Fehler")
        if hb==True:
            self.like()
        if hb==False:
            self.dislike()

    def testmatchloop():
        for k in range(1000):
            try:
                self.testmatch()
            except:
                sleep()
            sleep(2)


