

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
    logging.basicConfig(filename='sampelpaginationforonetvserial.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

   
    test = [{
        "name": "Agents of S.H.I.E.L.D.",
        "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=140"
        }]

    url = test["link"]



    
    driver.get(url)

    try :
        #SAVE THE LINKS OF FIRST PAGE



        #NOW SAVES THE PAGES
        #listofpagination = driver.find_elements_by_xpath("div[@class='postbody']//descendant::p")
        listofpages= driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")
        #print(listofpages)
        logging.info("Got the list of pages")


        #NOW TRAVERSE EACH PAGE TO SAVE THE LINKS IN EACH PAGE

        for eachpage  in listofpagination : 
            
        
            


   
    except :
        logging.error("error")

    finally :
        driver.quit()
        logging.info("program exited")