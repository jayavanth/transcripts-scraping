

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

def step2listofepisodesforeachtvserial():
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

        if((path.exists(os.getcwd() + "/TVSerials" + slugifiedname + ".json"))) : 
            os.remove(os.getcwd() + "/TVSerials/" + slugifiedname + ".json")

        with open(os.getcwd() + "/TVSerials/" + slugifiedname + ".json","w") as writefile :

            try:

                
                

                driver.get(eachtvserial['link'])
                #logging.info("Got the mainpage TVserial",slugifiedname)

                listofpages = []

                firstpage = {
                    'link' : eachtvserial['link']
                }

                listofpages.append(firstpage)


                # logging.info("Now getting and storing all the links in first page")
                # #TODO : Clean the data in listofepisodes below
                # listofepisodes = driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")

                # wrapperlist = []
                
                # #TODO : Get movies link as well
                
                # for elem in listofepisodes: 
                    
                #     #filetowrite.write(elem.text)
                #     #filetowrite.write(elem.get_attribute('href'))
                #     #print (elem.text)
                #     #print( elem.get_attribute('href'))
                #     episodename = elem.text
                #     linkwithsessionid = elem.get_attribute('href')
                #     splittinglink = linkwithsessionid.split("&sid")
                #     link = splittinglink[0]

                #     rawmovie = {
                #         'name' : episodename,
                #         'link' : link
                #     }

                #     wrapperlist.append(rawmovie)



                # logging.info("dumping as json only once")    
                # writefile.write(json.dumps(wrapperlist))


                logging.info("successfully fetched links in the first page. Now see if there are any other pages to traverse")
                


                #listofhrefelements = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a")
                nextpage = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a")
                
                breakpoint()
                
                if(not(nextpage == [])) :
                    url = nextpage.get_attribute('href')

                    if url not in listofpages :
                        listofpages.append(url)
                        sleep(random.randrange(3,7))

                        url.click()



                # temppaginationlist = []
                # for eachelem in listofhrefelements :
                #     pagenum = eachelem.text 
                #     linkwithsessionid = elem.get_attribute('href')
                #     splittinglink = linkwithsessionid.split("&sid")
                #     link = splittinglink[0]

                #     newpage = {
                #         'pagenum' : pagenum,
                #         'link' : link
                #     }

                #     temppaginationlist.append(newpage)


                #funcforeachpage(temppaginationlist)

                

            except:

                logging.error("Error in step 2 traversal of each tvseriallink")

            finally :
                driver.quit()

    logging.info("Step 2 passed successfully")

def funcforeachpage(temppaginationlist) :

    for eachpage in temppaginationlist :

        url = eachpage["link"]

        random.randrange(4,8)


if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='testforpagination.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    step2listofepisodesforeachtvserial()