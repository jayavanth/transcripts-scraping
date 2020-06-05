

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
from slugify import slugify
import os



    

def gettranscripts() :

    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=174&t=24903'
    #EACH EPISODE XPATH - div[@class='postbody']//descendant::p


    #MOCKSERIALNAME 
    fetchserialnamejson = {'name':'Game of Thrones',
     'listofepisodes' : 'link'}

    listoftvserialnamesjson = json.loads(open("listoftvserials.json").read())

    # fetchepisodelinksjson = [{
    #                         "name": "All American", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=902"}, {
    #                         "name": "A Million Little Things", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=853"}, {
    #                         "name": "American Horror Story", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=135"}, {
    #                         "name": "Arrow", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=172"}, {
    #                         "name": "Avatar: The Last Airbender", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=935"}]

    #linksjson = json.loads(open("listoftvserials.json").read())


   



    #CREATE DIRECTORIES FOR EACH OF THE TVSERIAL. EACH EPISODE TRANSCRIPTS WILL BE STORED IN THE TVSERIAL NAME DIRECTORY FOR EACH TVSERIAL
    for each in fetchserialnamejson :

        slugifiedtvserialname = slugify(fetchserialnamejson['name'])

        if(not(os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname))) : 
            os.mkdir(os.getcwd() + "/TVSerials/" + slugifiedtvserialname)

    
    for each in fetchserialnamejson :

        slugifiedtvserialname = slugify(fetchserialnamejson['name'])


        #CHECK IF THE FILE THAT CONTAINS THE LIST OF THE LINKS FOR THE TVSERIAL EXISTS
        if os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + ".json"):
            
            #Load that file
            episodelinksjson = json.loads((open(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + ".json")).read())
            infomessage1 = "List of web links of all episodes successfully loaded for *** "  + slugifiedtvserialname
            logging.info(infomessage1)

        else :
            message2 = "ERROR in getting list of weblinks of episodes for *** " + slugifiedtvserialname
            logging.error(message2)



        #MOCK EPISODE LIST
        mockepisodelinksjson = {} 
        with open(sys.argv[1]) as json_file:
            mockepisodelinksjson = json.load(json_file)

        options = Options()
        #options.headless = True
        options.add_argument("--window-size=1440,900")

        driver = webdriver.Chrome()

        #TODO : Random sleep funciton here
        sleep(random.randrange(27,44))

        message9 = "STARTING SCRAPING now of *** " + slugifiedtvserialname

        logging.info(message9)

        if((os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname))) : 

            message3 = "STARTED fetching the transcripts of *** " + slugifiedtvserialname
            logging.info(message3)

            for eachepisode in mockepisodelinksjson:

                #TODO : Random sleep function here
                sleep(random.randrange(9,17))

                slugifiedepisodename = slugify(eachepisode['name'])

                message4 = "Scraping of" + slugifiedepisodename + "of" + slugifiedtvserialname + "started"
                logging.info(message4)



                with open(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + "/" + slugifiedepisodename + ".txt","w") as writefile :

                    # import ipdb ; ipdb.set_trace()
                    try :
                        driver.get(eachepisode['link'])

                        ep_date = driver.find_elements_by_xpath("//time")
                        ep_date = ep_date[0].get_attribute('datetime')
                        listofpara = driver.find_elements_by_xpath("//div[@class='postbody']//descendant::p")
                        
                        
                        #logging.info("list of para fetched")
                        writefile.write(ep_date)
                        writefile.write("\n")
                        for eachelem in listofpara :
                            
                            writefile.write(eachelem.text)
                            writefile.write("\n")


       
                    except :
                        message5 = slugifiedepisodename + "*** error while getting text of this episode of ***" + slugifiedtvserialname
                        logging.error(message5)


                                         

                
                message6 = slugifiedepisodename + " successfully scraped of *** " + slugifiedtvserialname 
                logging.info(message6)


            message10 = ""
            driver.quit()
            message7 = slugifiedepisodename + "*** Driver gracefully shut down of *** " + slugifiedtvserialname
            logging.info(message7)


        message8 = "Succesfully scraped all the episodes of *** " + slugifiedtvserialname
        logging.info(message8)

    message11 = "Program now shutting down"
    logging.info(message11)     




if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='module-eachepisodetotextfile.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    gettranscripts()

    


    



