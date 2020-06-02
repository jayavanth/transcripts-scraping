
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


if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='fastest-foreverdreaming.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

    test = {
        "name": "Agents of S.H.I.E.L.D.",
        "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=140"
        }


    test2 = {

        "name": "The X-Files",
        "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=174"
        }


    driver.get(test2['link'])
    logging.info("Got the mainpage of particular tv serial")

    try : 

        pagearray = []

        #logging.info("Got the mainpage of particular tv serial - ",test['link'])

        
        #listofpages = driver.find_elements_by_xpath("//b[@class='pagination']")
        listofpages= driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")
        #print(listofpages)
        logging.info("Got the list of pages")
        
        with open("testepisodefile.txt","w") as pagesfile :

            episodelinkslist = []

            for eachelem in listofpages: 
                #pageno = eachelem.text
                episodename = eachelem.text
                rawpagelink = eachelem.get_attribute('href')
                pagelink = rawpagelink.split("&sid")


                
                #rawepisodelinks = {
                #    'text' : episodename,
                #    'plink' : pagelink[0]
                #}

                episodelinkssimplified = {
                    'text' : episodename,
                    'plink' : pagelink[0]
                }

                #episodelinks = json.dumps(rawepisodelinks)
                #wrapper = { "data" : episodelinks}
                #pagesfile.write(str(wrapper))

                episodelinkslist.append(episodelinkssimplified)


            logging.info("dumping as json only once")
            pagesfile.write(json.dumps(episodelinkslist))


    except NoSuchElementException as err :
            
        logging.error("No such element Exception occurred")

    except exception as e :

        logging.error("Error",e)

    finally : 
        driver.quit()
        logging.info('Program exited')

