


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
    

    #USING A MOCKJSON TO CHECK FOR SINGLE CASE
    #testjson = [{
    #    "name": "All American",
    #   "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=902"
    #    }]

    
    



    linksjson = json.loads(open("listoftvserials.json").read())

    
    if(not(path.exists(os.getcwd() + "/TVSerials"))) : 
        os.mkdir(os.getcwd() + "/TVSerials")

    #TODO : Change testjson to linksjson later
    for eachtvserial in linksjson :

        
        options = Options()
        #options.headless = True
        options.add_argument("--window-size=1440,900")
    
        driver = webdriver.Chrome(options=options)
        slugifiedname = slugify(eachtvserial['name'])

        if os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedname + ".json"):
                os.remove(os.getcwd() + "/TVSerials/" + slugifiedname + ".json")

        infomessagefetchlinksnewserial = "FETCHING ALL THE LINKS FOR A NEW TVSERIAL - " + slugifiedname
        logging.info(infomessagefetchlinksnewserial)

        #with open(os.getcwd() + "/TVSerials/" + slugifiedname + "-pageslist" + ".json","w") as writefile :
        with open(os.getcwd() + "/TVSerials/" + slugifiedname + ".json","w") as writefile :
            try:
                
                infomessage10 = slugifiedname + "Opened file to store the links for this TVserial"
                logging.info(infomessage10)

                url = eachtvserial['link']
                listofpages = []
                loopcondition = True
                pagenumberflag = 1
                
                infomessage11 = slugifiedname + "now sleeping for 25-40 seconds"
                logging.info(infomessage11
                    )
                sleep(random.randrange(25,40))
                driver.get(url)
                #logging.info("Got the mainpage TVserial",slugifiedname)

                
                listofepisodes = driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")

                #page = {
                #    'link' : url
                #}

                #listofpages.append(page)


                episodeswrapperlist = []

                infomessage12 = slugifiedname + "now getting episode list of links on root page"
                logging.info(infomessage12)

                for elem in listofepisodes: 
                    
                    #filetowrite.write(elem.text)
                    #filetowrite.write(elem.get_attribute('href'))
                    #print (elem.text)
                    #print( elem.get_attribute('href'))
                    episodename = elem.text
                    linkwithsessionid = elem.get_attribute('href')
                    splittinglink = linkwithsessionid.split("&sid")
                    link = splittinglink[0]

                    rawmovie = {
                        'name' : episodename,
                        'link' : link
                    }

                    episodeswrapperlist.append(rawmovie)

                
                infomessage2 = slugifiedname + " - Successfully fetched links in the root page. Now see if there are any other pages to traverse"
                logging.info(infomessage2)
                pagenumberflag = pagenumberflag + 1 

                

                #listofhrefelements = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a")
                #nextpage = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a")
                nextpage = driver.find_elements_by_xpath("//div[@class='box extra-content control-box top']//b[@class='pagination']//descendant::a[position()=last()]")
                #nextpage = driver.find_elements_by_xpath("//div[@class='box extra-content control-box top']//b[@class='pagination']//descendant::a")
                #breakpoint()

                while True : 
                    infomessage3 = slugifiedname + " - now sleeping for 8-15 seconds"
                    logging.info(infomessage3)
                    sleep(random.randrange(8,15))

                    # if(int(nextpage[0].text,base = 10) < pagenumberflag):

                    #     break

                    if( nextpage[0].text != "»") :
                        break

                    if(not(nextpage == [])):

                        nextpage[0].click()

                    else : 
                        break 

                    
                    infomessage4 = slugifiedname + " - Now getting and storing all the links in traversed page"
                    logging.info(infomessage4)
                    #TODO : Clean the data in listofepisodes below
                    listofepisodes = driver.find_elements_by_xpath("//td[@class='topic-titles row2']/h3/a[@class='topictitle']")

                    for elem in listofepisodes: 
                    
                    #filetowrite.write(elem.text)
                    #filetowrite.write(elem.get_attribute('href'))
                    #print (elem.text)
                    #print( elem.get_attribute('href'))
                        episodename = elem.text
                        linkwithsessionid = elem.get_attribute('href')
                        splittinglink = linkwithsessionid.split("&sid")
                        link = splittinglink[0]

                        rawmovie = {
                            'name' : episodename,
                            'link' : link
                        }

                        episodeswrapperlist.append(rawmovie)

                    
                    infomessage5 = slugifiedname + " - moving to next page" 
                    logging.info(infomessage5)
                    nextpage = driver.find_elements_by_xpath("//div[@class='box extra-content control-box top']//b[@class='pagination']//descendant::a[position()=last()]")

                    pagenumberflag = pagenumberflag + 1
                    #breakpoint()
                    #if(nextpage == []) :
                    #   break 


                # for eachpage in nextpage : 
                #     sleep(random.randrange(7,16))
                #     eachpage.click()
                #     nextpage = driver.find_elements_by_xpath("/html/body[@class='viewforum f140']/div[@id='wrapper']/div[@id='wrapcentre']/div[@class='box extra-content control-box top']/div[@class='boxbody clearfix']/div[@class='pull-left nowrap']/b[@class='pagination']//descendant::a")
                #     breakpoint()




                # if(not (nextpage == [])) :
                #     #url = nextpage.get_attribute('href')

                #     for elem in nextpage :
                #         url = elem.href
                #     sleep(random.randrange(7,16))

                infomessage6 = " Dumping as json only once into file for all the links in " + slugifiedname 
                logging.info(infomessage6)    
                writefile.write(json.dumps(episodeswrapperlist))

                # logging.info("dumping as json only once") 
                # writefile.write(json.dumps(listofpages))            
                                       

            except:
                infomessage7 = slugifiedname + "Error in traversal of each page of tvseriallink"
                logging.error(infomessage7)

            finally :
                driver.quit()
                infomessage9 = slugifiedname + "Driver gracefully closed"
                logging.info(infomessage9)

        infomessage8 = "ALL THE LINKS FETCHED successfully for" + slugifiedname
        logging.info(infomessage8)

    logging.info("COMPLETED GETTING LINKS FOR ALL THE TVSERIALS IN THE FILE.")



if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='listofepisodesforeachtvserial.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    step2listofpagesforeachserial()

    




