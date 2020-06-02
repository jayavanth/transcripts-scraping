

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




def step1gettvlistfrommainpage():

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

    mainpage = 'https://transcripts.foreverdreaming.org/index.php'

    

    with open("listoftvserials.json","w") as filetowrite :
        
        driver.get(mainpage)

        logging.info('Main page fetched')
        try :

            listoflinks = driver.find_elements_by_xpath("//p[@class='forumdesc subforums']//escendant::a")
            wrapperlist = []
            
            #TODO : Get movies link as well
            
            for elem in listoflinks : 
                
                #filetowrite.write(elem.text)
                #filetowrite.write(elem.get_attribute('href'))
                #print (elem.text)
                #print( elem.get_attribute('href'))
                tvserialname = elem.text
                linkwithsessionid = elem.get_attribute('href')
                splittinglink = linkwithsessionid.split("&sid")
                link = splittinglink[0]

                rawmovie = {
                    'name' : tvserialname,
                    'link' : link
                }

                wrapperlist.append(rawmovie)



            logging.info("dumping as json only once")    
            filetowrite.write(json.dumps(wrapperlist))

        except NoSuchElementException as err :
            
            logging.error("No such element Exception occurred")

        except Exception as err :
            logging.error("other exception in Step 1")

        finally :
            driver.quit()

    logging.info("Step 1 completed successfully")



if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='listoftvserials.log', filemode='w', level=logging.DEBUG, ormat='%(name)s - %(levelname)s - %(message)s')
    step1gettvlistfrommainpage()
