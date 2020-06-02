

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

def step2listofpagesforeachserial():
    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")
    
    driver = webdriver.Chrome(options=options)

    #USING A MOCKJSON TO CHECK FOR SINGLE CASE
    testjson = [{
        "name": "Agents of S.H.I.E.L.D.",
        "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=140"
        }]



    #linksjson = json.loads(open("listoftvserials.json").read())

    driver = webdriver.Chrome(options=options)

    if(not(path.exists(os.getcwd() + "/TVSerials"))) : 
        os.mkdir(os.getcwd() + "/TVSerials")

    #TODO : Change testjson to linksjson later
    for eachtvserial in testjson :


        slugifiedname = slugify(eachtvserial['name'])

        if os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedname + "-pageslist" + ".json"):
                os.remove(os.getcwd() + "/TVSerials/" + slugifiedname + "-pageslist" + ".json")
        with open(os.getcwd() + "/TVSerials/" + slugifiedname + "-pageslist" + ".json","w") as writefile :

            try:
                
                url = eachtvserial['link']
                listofpages = []
                
                while True :

                    driver.get(url)
                    #logging.info("Got the mainpage TVserial",slugifiedname)

                    

                    page = {
                        'link' : url
                    }

                    listofpages.append(page)


            

                    logging.info("successfully fetched links in the first page. Now see if there are any other pages to traverse")
                    


                    #listofhrefelements = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a")
                    nextpage = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a[last()]")
                    
                    breakpoint()

                    if(not (nextpage == [])) :
                        #url = nextpage.get_attribute('href')

                        for elem in nextpage :
                            url = elem.href
                        sleep(random.randrange(3,7))


                    else :
                        break 

                logging.info("dumping as json only once") 
                writefile.write(json.dumps(listofpages))            
                                       

            except:

                logging.error("Error in traversal of each page of tvseriallink")

            finally :
                driver.quit()

    logging.info("Got the list of all pages  successfully")



if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='listofpaginationpagesforeachtvserial.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    step2listofpagesforeachserial()