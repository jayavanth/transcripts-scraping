

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
    logging.basicConfig(filename='saveeachepisodetotextfile.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

   
    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=174&t=24903'
    #EACH EPISODE XPATH - div[@class='postbody']//descendant::p
    
    with open("episodecompletetext.txt","w") as writefile:

        try :
            driver.get(url)
            listofpara = driver.find_elements_by_xpath("//div[@class='postbody']//descendant::p")
            
            
            logging.info("list of para fetched")
            
            for eachelem in listofpara :
                
                writefile.write(eachelem.text)                


       
        except :
            logging.error("error")

        finally :
            driver.quit()
            logging.info("program exited")