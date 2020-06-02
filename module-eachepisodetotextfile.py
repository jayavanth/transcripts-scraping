

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


    #MOCKSERIALNAME 
    fetchserialnamejson = [
     'name' : 'Game of Thrones',
     'listofepisodes' : 'link'
    ]

    fetchserialnamejson = [{
                            "name": "All American", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=902"}, {
                            "name": "A Million Little Things", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=853"}, {
                            "name": "American Horror Story", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=135"}, {
                            "name": "Arrow", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=172"}, {
                            "name": "Avatar: The Last Airbender", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=935"}]

    #linksjson = json.loads(open("listoftvserials.json").read())


   



    #CREATE DIRECTORIES FOR EACH OF THE TVSERIAL. EACH EPISODE TRANSCRIPTS WILL BE STORED IN THE TVSERIAL NAME DIRECTORY FOR EACH TVSERIAL
    for each in fetchserialnamejson :

        slugifiedname = slugify(fetchserialnamejson['name'])

        if(not(path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname))) : 
        os.mkdir(os.getcwd() + "/TVSerials/" + slugifiedtvserialname)

    
    for each in fetchserialnamejson :

        slugifiedtvserialname = slugify(fetchserialnamejson['name'])


        #CHECK IF THE FILE THAT CONTAINS THE LIST OF THE LINKS FOR THE TVSERIAL EXISTS
        if os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + ".json"):
            
            
            episodelinksjson = json.loads((open("os.getcwd()" + "/TVSerials/" + slugifiedtvserialname + ".json")).read())
            logging.info("list of episodes successfully loaded for",slugifiedtvserialname)

        else :
            logging.error("ERROR in getting list of episodes for",slugifiedtvserialname)



        #MOCK EPISODE LIST
        mockepisodelinksjson =  [{
                                "name": "01x05 - Other Women", "link": "https://transcripts.foreverdreaming.org/viewtopic.php?f=904&t=34919"},{
                                "name": "01x06 - Kappa Spirit","link": "https://transcripts.foreverdreaming.org/viewtopic.php?f=904&t=34920"}, {
                                "name": "01x07 - Out of Scythe", "link": "https://transcripts.foreverdreaming.org/viewtopic.php?f=904&t=34921"}]

        #TODO : Random sleep funciton here
        sleep(random.randrange(27,44))

        logging.info("STARTING SCRAPING of",slugifiedtvserialname,"now")

        if((path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname))) : 

            logging.info()

            for eachepisode in mockepisodelinksjson:

                #TODO : Random sleep function here
                sleep(random.randrange(13,26))

                slugifiedepisodename = slugify(eachepisode['episodename'])

                logging.info("scraping of", str(slugifiedepisodename),"of", str(slugifiedtvserialname),"started")



                with open(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + "/" + slugifiedepisodename+ ".txt","w") as writefile :

                    try :
                        driver.get(eachepisode['episodelink'])

                        listofpara = driver.find_elements_by_xpath("//div[@class='postbody']//descendant::p")
                        
                        
                        logging.info("list of para fetched")
                        
                        for eachelem in listofpara :
                            
                            writefile.write(eachelem.text)                


       
                    except :
                        logging.error("error while getting text of an episode")

                logging.info(str(slugifiedepisodename),"of", str(slugifiedtvserialname),"successfully scrapped")



        logging.info("All the episodes of", slugifiedtvserialname,"SCRAPED")     




    


    


    for episode in tvserialseries.json:

