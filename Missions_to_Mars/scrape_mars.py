from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, time


# Mac
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    #listings = []

    news_url = "https://mars.nasa.gov/news/"

    browser.visit(news_url)
    #time.sleep(3)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.find('li', class_="slide")
    news_title = section.find('div', class_="content_title").text
    #print(news_title)
    #listings.append(news_title)

    news_head = section.find('div', class_='article_teaser_body').text
    #print(news_head)
    #listings.append(news_head)

    # return news_title, news_head


    #### Mars Featured Images
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)
    time.sleep(3)

    browser.click_link_by_id("full_image")
    time.sleep(2)
    browser.click_link_by_partial_text("more info")
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_tags = soup.select_one('figure.lede a img').get("src")
    featured_image_url = "https://www.jpl.nasa.gov" + image_tags
    
    #listings.append(featured_image_url)


    ## Mars Facts Table
    facts_url = "https://space-facts.com/mars/"
    time.sleep(3)

    tables = pd.read_html(facts_url)
    #len(tables)

    df =  tables[1]
    #df.head()

    html_table = df.to_html()
    #print(html_table)
    df.to_html('table.html')

    #listings.append(html_table)

    ##Hemispheres
    hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemis_url)  
    time.sleep(3)  

    soup = BeautifulSoup(browser.html, 'html.parser')

    browser.click_link_by_partial_text("Cerberus")
    time.sleep(2)
    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')

    hemis_title = soup2.select_one("div.content h2").text
    #print(hemis_title)

    cerberus_hemis_url = browser.find_by_text("Sample")["href"]
    hemis1 = {"Name": hemis_title, "img_url": cerberus_hemis_url}

    browser.click_link_by_partial_text("Schiaparelli")
    time.sleep(2)
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')

    hemis_title_2 = soup3.select_one("div.content h2").text

    schiaparelli_hemis_url = browser.find_by_text("Sample")["href"]
    hemis2 = {"Name": hemis_title_2, "img_url": schiaparelli_hemis_url}

    browser.click_link_by_partial_text("Syrtis")
    time.sleep(2)
    html = browser.html
    soup4 = BeautifulSoup(html, 'html.parser')

    hemis_title_3 = soup4.select_one("div.content h2").text
    #print(hemis_title_3)

    syrtis_hemis_url = browser.find_by_text("Sample")["href"]
    hemis3 = {"Name": hemis_title_3, "img_url": syrtis_hemis_url}

    browser.click_link_by_partial_text("Valles")
    time.sleep(2)
    html = browser.html
    soup5 = BeautifulSoup(html, 'html.parser')

    hemis_title_4 = soup5.select_one("div.content h2").text
    #print(hemis_title_4)

    marineris_hemis_url = browser.find_by_text("Sample")["href"]
    hemis4 = {"Name": hemis_title_4, "img_url": marineris_hemis_url}

    # print(cerberus_hemis_url)
    # print(schiaparelli_hemis_url)
    # print(syrtis_hemis_url)
    # print(marineris_hemis_url)

    # listings.append(hemis1, hemis2, hemis3, hemis4)

    return_dict = {"news_title": news_title,"news_head": news_head,"featured_image_url": featured_image_url,"html_table":html_table,"hemisphere_urls":[hemis1, hemis2,hemis3,hemis4]}
    browser.quit()
    return return_dict