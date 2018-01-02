import time
import json
from selenium import webdriver
from pyvirtualdisplay import Display


def start_driver():
    """Open headless chromedriver"""
    print 'Starting Web driver...'
    display = Display(visible=0, size=(800, 600))
    display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/root/Headless_Network_panel/chromedriver', chrome_options=chrome_options)
    #driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    # print "Sleeping for 4 ..."
    time.sleep(4)
    return driver, display



def get_network(driver):
    """Tell the browser to get a page"""
    driver.get(url)
    print "Please wait, accessing Network  panel on your webpage "+ driver.title + ": "
    time.sleep(20)  
    net = driver.execute_script("return window.performance.getEntries();")
    return net



def parse_url(url):
    """Calling function which calls all other fucntions to parse html"""
    driver, display = start_driver()
    network= get_network(driver)
    loop = 0
    urls = []

    for url in network:
        urls.append(url['name'])

    for url in urls:
        spltAr = url.split("://")
        i = (0,1)[len(spltAr)>1];
        dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower();
        print dm
        print "Sl No : " + str(loop) + "      "+ dm
        loop= loop+1
    close_driver(driver, display)


def close_driver(driver, display):
    """Close chromedriver"""
    print "Closing Web driver..."
    display.stop()
    driver.quit()
    print "Chrome driver closed successfully. "


if __name__ == '__main__':
    loop = 1
    json_data =  json.loads(open('network_headless.json').read())
    for domain in json_data["domain_url"]:
        url = domain
        print "Sl no :  "+str(loop)+" URL : ",url
        print "==================================================="
        parse_url(url)
        loop= loop+1