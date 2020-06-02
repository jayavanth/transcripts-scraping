

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


# if(not(path.exists(os.getcwd() + "/testdirectory"))) : 
#         os.mkdir(os.getcwd() + "/testdirectory")

# loadedlist = []

# emptylist = []

# if(loadedlist == emptylist) :
# 	print("empty")
# else :
# 	print("loaded")
print(os.getcwd())

# [{
# "name": "Agents of S.H.I.E.L.D.", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=140"}, {
# "name": "All American", "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=902"}]

logging.basicConfig(filename='testos.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
listoftvserialsjson = json.loads(open("listoftvserials.json").read())

for each in listoftvserialsjson :
	print(str(each['name']))
	#print(str(each['link']))

	slugifiedname = slugify(each['name'])

	print(slugifiedname)

	print("******************")

	infomessage = "NOW PRINTING SLUGIFIED NAME -" + slugifiedname
	#logging.info("NOW PRINTING SLUGIFIED NAME -", slugifiedname)
	logging.info(infomessage)