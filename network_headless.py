import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from ConfigParser import SafeConfigParser
import redis
import sys 
import os

PARSER = SafeConfigParser()
PARSER.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

REDIS_HOST = PARSER.get('redis', 'host')
REDIS_PORT= PARSER.get('redis', 'port')

tempdb = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def start_driver():
    """Open headless chromedriver"""
    print 'Starting Web driver...'
    display = Display(visible=0, size=(800, 600))
    display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/root/tracker_headless/chromedriver', chrome_options=chrome_options)
    #driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    # print "Sleeping for 4 ..."
    time.sleep(4)
    return driver, display


def get_network(driver):
    """Tell the browser to open a tab and access Network tab"""
    driver.get(url)
    print "Please wait, accessing Network  panel on your webpage "+ driver.title + ": "
    time.sleep(20)
    net = driver.execute_script("return window.performance.getEntries();")
    return net



def parse_url(url, redis_list):
    """Calling function which calls all other fucntions to parse html"""
    time.sleep(20)  
    #driver, display = start_driver()
    network= get_network(driver)
    loop = 0
    urls = []
    
    for url in network:
        urls.append(url['name'])

    for url in urls:
        spltAr = url.split("://")
        i = (0,1)[len(spltAr)>1];
        dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower();
        print "Sl No : " + str(loop) + "      "+ dm
        redis_list .append(dm)
        loop= loop+1
    return  redis_list , driver, display


def close_driver(driver, display):
    """Close chromedriver"""
    print "Closing Web driver..."
    print ""
    display.stop()
    driver.quit()
    print "Chrome driver closed successfully. "



if __name__ == '__main__':
    redis_dict = {}
    loop = 1
    json_data =  json.loads(open('domain.json').read())
    driver, display = start_driver()


    for domain in json_data["domain_url"]:
        url = domain
        redis_list = []

        print ""
        print "Sl no :  "+str(loop)+ "                 |                 URL : ",url
        print "======================================================================================="
        redis_list , driver, display = parse_url(url, redis_list)
        print ""
        print "Closing tab for ",driver.title
        print ""
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        loop= loop+1
        print "URL list to be sent to Redis :",redis_list
        #redis_dict[url] = redis_list
        tempdb.set("ad_tracker_domains :"+url, redis_list)

    close_driver(driver, display)
    #print "Final DICT sent to REDIS :", redis_dict
