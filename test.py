from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape(search):
    browser = init_browser()

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.find('li', class_="slide")
    news_title = section.find('div', class_="content_title").text
    #print(news_title)

    news_head = section.find('div', class_='article_teaser_body').text
    #print(news_head)


    #### Mars Images
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)