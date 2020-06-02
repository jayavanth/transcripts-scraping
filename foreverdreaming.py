
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



# HELPER TEXT COMMENT NOT EXACTLY USED HERE BUT USED WHILE WRITING CODE - Keeping it here for future reference as well
#logging.debug('This is a debug message')
#logging.exception("Exception occurred")
#logging.error("Exception occurred", exc_info=True)
#name = 'John'
#logging.error(f'{name} raised an error')
#logging.warning('Admin logged out')
#logging.info('Admin logged in')

# for element in self.driver.find_elements_by_tag_name('img'):
#        print element.text
#        print element.tag_name
#        print element.parent
#        print element.location
#        print element.size


#Wait functions
#element_to_be_clickable
#text_to_be_present_in_element


# get the form element
    #form = driver.find_element_by_css_selector("form[name='signupForm']")
    # fill the fields
    #form.find_element_by_css_selector("input[name='firstName']").send_keys(student['first_name'])
#wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='Accept']"))).click()
# wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal")))

#filetowrite.write(driver.page_source)
        #maintable = driver.find_element_by_xpath("html/body/div[@id='wrapper']/div[@id='wrapcentre']/div[@id='pagecontent']/div[@class='box community-content category-box']/div[@class='boxbody']/table[@class='tablebg']")   
        #maintable = driver.find_elements(By.XPATH,"/html/body[@class='index']/div[@id='wrapper']/div[@id='wrapcentre']/div[@id='pagecontent']/div[@class='box community-content category-box']/div[@class='boxbody']/table[@class='tablebg']/tbody/tr[4]/td[@class='row2 forums evencol']")

        #maintable = driver.find_element_by_xpath("//table[@class='tablebg']/tbody")
        #button = driver.find_element_by_xpath("//a[@class='forumlink']")
        #button.click()

## HELPER TEXT COMMENT ENDS HERE




if __name__ == '__main__':
    #START OF PROGRAM HERE
    logging.basicConfig(filename='foreverdreaming.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
   
    

    try:
        
        #STEP 1 : Get tv list
        # step1 = step1gettvlistfrommainpage("tvlinks.json")
        # if(step1):
        #   logging.info('Wrote movie-TV links in json format to file successfully')
        # else: 
        #   logging.error("Writing tv-movie links to json not successful")

        #STEP 2 : For each tv serial , populate the episodes and their link

        step2 = step2getonlyonetvserialepisodes(,"tvlinks.json")
        step2 = step2getallepisodesofoneserial("tvlinks.json")

        if(step2):
            logging.info('Got the pages list of each serial')
        else: 
            logging.error("Getting pages list not successful")

        #STEP 3 : Fore each tv serial link, traverse its episodes and scrape it to store it in database

        step3 = step3fetcheachepisode(episodelistfile)
    except:
        logging.error("other error occured in the main program")

    finally: 
        
        logging.info('Main Program successfully exited')


def step2getonlyonetvserialepisodes(allseriallist):
    return True
    
    


    #XPATH FOR EPISODE LINKS ON EACH PAGE - //td[@class='topic-titles row2']/h3/a[@class='topictitle']


def step2getallepisodesofoneserial(allseriallist) :
    

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

    linksjson = json.loads(open("allseriallist").read())



    test = [{
        "name": "Agents of S.H.I.E.L.D.",
        "link": "https://transcripts.foreverdreaming.org/viewforum.php?f=140"
        }]


    # TODO : Change below to linksjson once the code for single case correctly
    for eachtvserial in test :

 
        #logging.info("Now processing eachtvserial["name"]")
        
        try: 
            sleeptime = random.randrange(4,16)
            logging.info("Sleeping for %d seconds",sleeptime)
            sleep(sleeptime)
            

            driver.get(eachtvserial['link'])
            logging.info("Got the mainpage of particular tv serial - ",eachtvserial['link'])


            loggin.info("Now getting and storing all the links in first page")


            logging.info("successfully fetched links in the first page. Now see if there are any other pages to traverse")
            listofpages = driver.find_elements_by_xpath("//b[@class='pagination']")

            for each in listofpages: 
                pageno = each.text
                pagelink = each.get_attribute('href')
                print(pagelink)

                pagearray.push(pagelink)


            logging.info("Fininshed creating pages to traverse. Now traversing each page")

            logging.info("All pages traversed successfully")

        except:

            logging.error("Error in step 2 traversal of each tvseriallink")

        finally :
            driver.quit()


    logging.info("Step 2 passed successfully")
    return True
    



def step1gettvlistfrommainpage(storefile):

    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

    mainpage = 'https://transcripts.foreverdreaming.org/index.php'

    

    with open("storefile","w") as filetowrite :
        
        driver.get(mainpage)

        logging.info('Main page fetched')
        try :

            listoflinks = driver.find_elements_by_xpath("//p[@class='forumdesc subforums']//descendant::a")
            
            wrapperlist = []
            #TODO : Get movies link as well
            
            for elem in listoflinks : 
                
                #filetowrite.write(elem.text)
                #filetowrite.write(elem.get_attribute('href'))
                #print (elem.text)
                #print( elem.get_attribute('href'))
                tvserialname = elem.text
                linkwithsessionid = elem.get_attribute('href')
                splittinglink = linkwithsessionid.split("&sid")
                link = splittinglink[0]

                rawmovie = {
                    'name' : tvserialname,
                    'link' : link
                }

                wrapperlist.append(rawmovie)



            logging.info("dumping as json only once")    
            filetowrite.write(json.dumps(rawmovie))

        except NoSuchElementException as err :
            
            logging.error("No such element Exception occurred")

        except Exception as err :
            logging.error("other exception in Step 1")

        finally :
            driver.quit()

    logging.info("Step 1 completed successfully").

    return True


def step3fetcheachepisode(episode):
    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)

   
    #url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=174&t=24903'
    #EACH EPISODE XPATH - div[@class='postbody']//descendant::p
    
    with open(episode["name"],"w") as writefile:

        try :
            driver.get(episode["link"])
            listofpara = driver.find_elements_by_xpath("//div[@class='postbody']//descendant::p")
            
            
            logging.info("list of para fetched")
            
            for eachelem in listofpara :
                
                writefile.write(eachelem.text)                


       
        except :
            logging.error("error")

        finally :
            driver.quit()
            logging.info("program exited")

#
#/html/body[@class='viewforum f364']/div[@id='wrapper']/div[@id='wrapcentre']/div[@id='pagecontent']/div[@class='box community-content forum-box']/div[@class='boxbody']/table[@class='tablebg']/tbody/tr[10]/td[@class='topic-titles row2']/h3/a[@class='topictitle']
#/html/body[@class='viewtopic f364 t19379']/div[@id='wrapper']/div[@id='wrapcentre']/div[@id='pagecontent']/div[@class='box community-content discussion-box']/div[@class='boxbody']/div/div[@id='p133480']/div/div[@class='postbody']

#/html/body[@class='viewforum f129']/div[@id='wrapper']/div[@id='wrapcentre']/div[@id='pagecontent']/div[@class='box community-content forum-box']/div[@class='boxbody']/table[@class='tablebg']/tbody/tr[7]/td[@class='topic-titles row2']/h3/a[@class='topictitle']
#/html/body[@class='viewtopic f129 t15974']/div[@id='wrapper']/div[@id='wrapcentre']/div[@id='pagecontent']/div[@class='box community-content discussion-box']/div[@class='boxbody']/div/div[@id='p130068']/div/div[@class='postbody']