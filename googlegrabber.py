

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlencode
from time import sleep

class Grabber():

    def __init__(self, rootURL='https://www.google.com/webhp?hl=en#hl=en&', searchPhrase='google', filterKiller='&filter=0', filename=''):
        # create search url
        self.opts = {'q': searchPhrase}
        self.opts = urlencode(self.opts)
        self.url = rootURL + self.opts + filterKiller
        
        # open browser
        self.browser = webdriver.Firefox()
        
        # load url
        self.browser.get(self.url)
        
    # get h2 a urls and print   
    def getURLs(self):
        # get urls
        # first get h3 tags
        htags = self.browser.find_elements_by_tag_name('h3')
        # then get a tags within a print href
        for tag in htags:
            try: # must catch empty h3 tag
                atag = tag.find_element_by_tag_name('a')
                href = atag.get_attribute('href')
                print(href)
            except: pass
    
    # click the next button
    def clickNext(self):
        try: # no next if we're on the last page
            nextLink = self.browser.find_element_by_link_text('Next')
            nextLink.send_keys(Keys.RETURN)
        except: pass
            
if __name__=='__main__':
    a = Grabber(searchPhrase='pac man')
    a.getURLs()
    sleep(5)
    a.clickNext()
    a.getURLs()
    sleep(30)
    a.clickNext()
    a.getURLs()
     
        
'''
# options
rootURL = 'https://www.google.com/webhp?hl=en#hl=en&'
searchPhrase = 'pac man'
filterKiller = '&filter:0'
'''