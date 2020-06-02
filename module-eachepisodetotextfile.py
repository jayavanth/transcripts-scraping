

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



    

def gettranscripts() :

    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=174&t=24903'
    #EACH EPISODE XPATH - div[@class='postbody']//descendant::p


    #MOCKSERIALNAME 
    fetchserialnamejson = [
     'name' : 'Game of Thrones',
     'listofepisodes' : 'link'
    ]

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

        if(not(path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname))) : 
        os.mkdir(os.getcwd() + "/TVSerials/" + slugifiedtvserialname)

    
    for each in fetchserialnamejson :

        slugifiedtvserialname = slugify(fetchserialnamejson['name'])


        #CHECK IF THE FILE THAT CONTAINS THE LIST OF THE LINKS FOR THE TVSERIAL EXISTS
        if os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + ".json"):
            
            #Load that file
            episodelinksjson = json.loads((open("os.getcwd()" + "/TVSerials/" + slugifiedtvserialname + ".json")).read())
            infomessage1 = "List of web links of all episodes successfully loaded for *** "  + slugifiedtvserialname
            logging.info(infomessage1)

        else :
            message2 = "ERROR in getting list of weblinks of episodes for *** " + slugifiedtvserialname
            logging.error(message2)



        #MOCK EPISODE LIST
        mockepisodelinksjson =  [{
                                "name": "01x05 - Other Women", "link": "https://transcripts.foreverdreaming.org/viewtopic.php?f=904&t=34919"},{
                                "name": "01x06 - Kappa Spirit","link": "https://transcripts.foreverdreaming.org/viewtopic.php?f=904&t=34920"}, {
                                "name": "01x07 - Out of Scythe", "link": "https://transcripts.foreverdreaming.org/viewtopic.php?f=904&t=34921"}]

        options = Options()
        #options.headless = True
        options.add_argument("--window-size=1440,900")

        driver = webdriver.Chrome(options=options)

        #TODO : Random sleep funciton here
        sleep(random.randrange(27,44))

        message9 = "STARTING SCRAPING now of *** " + slugifiedtvserialname

        logging.info(message9)

        if((path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname))) : 

            message3 = "STARTED fetching the transcripts of *** " + slugifiedtvserialname
            logging.info(message3)

            for eachepisode in mockepisodelinksjson:

                #TODO : Random sleep function here
                sleep(random.randrange(9,17))

                slugifiedepisodename = slugify(eachepisode['episodename'])

                message4 = "Scraping of" + slugifiedepisodename + "of" + slugifiedtvserialname + "started"
                logging.info(message4)



                with open(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + "/" + slugifiedepisodename + ".txt","w") as writefile :

                    try :
                        driver.get(eachepisode['episodelink'])

                        listofpara = driver.find_elements_by_xpath("//div[@class='postbody']//descendant::p")
                        
                        
                        #logging.info("list of para fetched")
                        
                        for eachelem in listofpara :
                            
                            writefile.write(eachelem.text)                


       
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

    


    



