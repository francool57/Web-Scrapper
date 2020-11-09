from logging import exception
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import common
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import os

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'D:\chromedriver.exe')
driver.minimize_window()

sleep(3)
os.system('cls')
print('loading wait...')
sleep(1)
os.system('cls')
sleep (3)
os.system('cls')
print('''               ---------------------------------------
               |                                     |
               |           * WEB SCRAPPER *          |
               |                                     |
               ---------------------------------------''')
site = input('\n             Reddit-[1]     Twitter-[2]\n   > ')

def Reddit():
    lgn = input('Login? [y/n] ')

    if lgn == 'y':
        username = input('Username: ')
        password = input('Password: ')
        driver.get('https://www.reddit.com/login/') 
        usr_plc = driver.find_element_by_name('username')
        pas_plc = driver.find_element_by_name('password')
        usr_plc.send_keys(username)   
        pas_plc.send_keys(password)
        clk = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div[1]/fieldset[5]/button')
        clk.click()
    else:   
        pass
        driver.get('https://www.reddit.com/')
    search = input('Topic to search:  ')
    secrh = driver.find_element_by_name('q')
    secrh.send_keys(search)
    secrh.send_keys(Keys.ENTER)



def tt():
    sleep(2)
    username = input('Username: ')
    password = input('Password: ')
    driver.get('https://www.twitter.com/login/') 
    usr_plc = driver.find_element_by_name('session[username_or_email]')
    pas_plc = driver.find_element_by_name('session[password]')
    usr_plc.send_keys(username)   
    pas_plc.send_keys(password)
    sleep(2)
    clk = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
    clk.click()
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/span')
        print('--Login error--')
        driver.close()
        exit()
    except NoSuchElementException:
        pass

    emlcd = input('Code sended to acc email:  ')
    inpteml = driver.find_element_by_name('challenge_response')
    inpteml.send_keys(emlcd)

    try :
        driver.find_element_by_xpath('//*[@id="error-message"]')
    except NoSuchElementException:
        pass

    sleep(3)
    print('\n Main page acessed!')
    aws = input('Search or tweet? [s/t] ')
    if aws == 's':
        sleep(2)
        search = input('Topic to search:  ')
        secrh = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        secrh.send_keys(search)
        secrh.send_keys(Keys.ENTER)
    elif aws == 't':
        sleep(2)
        twet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_input = input('Write something to tweet:  ')
        twet.send_keys(tweet_input)
    else:
        pass


try:
    if site == '1':
        Reddit()
    elif site == '2':
        tt()
    else:
        print('\n--Invalid number--')
finally:
    print('\n--Code finished--')
    ws = input('\nClose driver? [y/n]')
    if ws == 'y':
        print('closing driver...')
        sleep(3)
        driver.close()
    else: 
        pass





