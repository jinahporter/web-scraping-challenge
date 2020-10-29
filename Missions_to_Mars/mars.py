from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import time

# identify location of chromedriver and store it as a variable
def init_browser():

    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
    # Setup configuration variables to enable Splinter to interact with browser
    #driverPath = !which chromedriver

    # Setup configuration variables to enable Splinter to interact with browser
    #executable_path = {'executable_path': driverPath[0]}
    #browser = Browser('chrome', **executable_path, headless=False)

def scrape(mars_news_list):
    browser = init_browser()

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.find('li', class_="slide")
    #print(section.prettify())
    news_title = section.find('div', class_="content_title").text
    #results_head = soup.find_all('div', class_="article_teaser_body")
    #print(news_title)
    #print(results_head)

    news_head = section.find('div', class_='article_teaser_body').text
    #print(news_head)

###
## Mars - Image
#def scrape(mars_image):
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(images_url)

    browser.click_link_by_id("full_image")

    browser.click_link_by_partial_text("more info")

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_tags = soup.select_one('figure.lede a img').get("src")
    print(image_tags)

    featured_image_url = "https://www.jpl.nasa.gov" + image_tags
    print(featured_image_url)

###
### Mars --facts
#def scrape(mars_facts):
    facts_url = "https://space-facts.com/mars/"

    ables = pd.read_html(facts_url)
    len(tables)

    print(type(tables))
    print(type(tables[0]))

    df =  tables[1]
    df.head()

    html_table = df.to_html()
    print(html_table)

    df.to_html('table.html')