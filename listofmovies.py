
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
import os
from slugify import slugify
from os import path

def listofmovies():
    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")
    
    driver = webdriver.Chrome(options=options)

    
    moviejson = [{
        "name": "LIST OF ALL MOVIES",
        "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=150"
        }]


    



    

    driver = webdriver.Chrome(options=options)

    if(not(path.exists(os.getcwd() + "/Movies"))) : 
        os.mkdir(os.getcwd() + "/Movies")

    #TODO : Change testjson to linksjson later
    for eachtvserial in moviejson :


        slugifiedname = slugify(eachtvserial['name'])

        if os.path.exists(os.getcwd() + "/Movies/" + slugifiedname + ".json"):
                os.remove(os.getcwd() + "/Movies/" + slugifiedname + ".json")


        
        with open(os.getcwd() + "/Movies/" + slugifiedname + ".json","w") as writefile :
            try:
                
                url = eachtvserial['link']
                listofpages = []
                loopcondition = True
                pagenumberflag = 1
                

                driver.get(url)
                #logging.info("Got the mainpage TVserial",slugifiedname)

                
                listofepisodes = driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")

                page = {
                    'link' : url
                }

                listofpages.append(page)


                episodeswrapperlist = []

                logging.info("now getting episode list of links on root page")

                for elem in listofepisodes: 
                    
                    
                    episodename = elem.text
                    linkwithsessionid = elem.get_attribute('href')
                    splittinglink = linkwithsessionid.split("&sid")
                    link = splittinglink[0]

                    rawmovie = {
                        'name' : episodename,
                        'link' : link
                    }

                    episodeswrapperlist.append(rawmovie)

                

                logging.info("successfully fetched links in the root page. Now see if there are any other pages to traverse")
                pagenumberflag = pagenumberflag + 1 

                

                
                nextpage = driver.find_elements_by_xpath("//div[@class='box extra-content control-box top']//b[@class='pagination']//descendant::a[position()=last()]")
                

                while True : 
                    sleep(random.randrange(7,16))
                    #TODO : increase the random number range
                  

                    if( nextpage[0].text != "»") :
                        break

                    if(not(nextpage == [])):

                        nextpage[0].click()

                    else : 
                        break 

                    

                    logging.info("Now getting and storing all the links in traversed page")
                    #TODO : Clean the data in listofepisodes below
                    listofepisodes = driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")

                    for elem in listofepisodes: 
                    
                  
                        episodename = elem.text
                        linkwithsessionid = elem.get_attribute('href')
                        splittinglink = linkwithsessionid.split("&sid")
                        link = splittinglink[0]

                        rawmovie = {
                            'name' : episodename,
                            'link' : link
                        }

                        episodeswrapperlist.append(rawmovie)

                    

                    logging.info("moving to next page")
                    nextpage = driver.find_elements_by_xpath("//div[@class='box extra-content control-box top']//b[@class='pagination']//descendant::a[position()=last()]")

                    
                    

              


                logging.info("dumping as json only once")    
                writefile.write(json.dumps(episodeswrapperlist))

             

            except:

                logging.error("Error in traversal of each page of movielink")

            finally :
                driver.quit()
                logging.info("driver gracefully closed")


    logging.info("Got the list of all pages  successfully")



if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='listofmovies.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    listofmovies()