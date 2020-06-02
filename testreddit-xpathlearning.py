from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import logging
import sys
import json
import random


if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='testreddit-xpathlearning.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    ##driver = webdriver.Chrome(options=options)

    ##url = 'https://reddit.com/r/nys'

    #driver.get(url)

    #listofheadings = driver.find_elements_by_xpath("_eYtD2XCVieq6emjKBH3m")
    
    #for eachheading in listofheadings : 
    #	print(eachheading.txt)

   

    linksjson = json.loads(open('testreddit.txt').read())

    


    #driver.quit()

