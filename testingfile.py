


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






def testfunction() :


    listoftvserialsjson = json.loads(open("listoftvserials.json").read())

    for eachtvserial in listoftvserialsjson :

            slugifiedtvserialname = slugify(eachtvserial['name'])


            #CHECK IF THE FILE THAT CONTAINS THE LIST OF THE LINKS FOR THE TVSERIAL EXISTS
            if os.path.exists(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + ".json"):
                
                #Load that file
                episodelinksjson = json.loads((open(os.getcwd() + "/TVSerials/" + slugifiedtvserialname + ".json")).read())
                infomessage1 = "List of web links of all episodes successfully loaded for *** "  + slugifiedtvserialname
                logging.info(infomessage1)

            else :
                message2 = "ERROR in getting list of weblinks of episodes for *** " + slugifiedtvserialname
                logging.error(message2)




if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='testingfile.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    testfunction()