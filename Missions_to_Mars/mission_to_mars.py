from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import time

# In[3]:
def scrape():
    
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    if browser.is_element_present_by_tag('li', wait_time=10):

        soup = BeautifulSoup(browser.html, 'html.parser')

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

    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)
    
    if browser.is_element_present_by_id('full_image', wait_time=10):

        soup = BeautifulSoup(browser.html, 'html.parser')

    browser.click_link_by_id("full_image")
    time.sleep(2)
    browser.click_link_by_partial_text("more info")

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_tags = soup.select_one('figure.lede a img').get("src")
    #print(image_tags)

    featured_image_url = "https://www.jpl.nasa.gov" + image_tags
    #print(featured_image_url)


    facts_url = "https://space-facts.com/mars/"

    tables = pd.read_html(facts_url)
    len(tables)

    print(type(tables))
    print(type(tables[0]))

    df =  tables[1]
    df.head()

    html_table = df.to_html()
    print(html_table)

    df.to_html('table.html')


    hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemis_url)

    browser.click_link_by_partial_text("Cerberus")
    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')

    hemis_title = soup2.select_one("div.content h2").text
    #print(hemis_title)

    cerberus_hemis_url = browser.find_by_text("Sample")["href"]
    print(cerberus_hemis_url)

    print(f"{hemis_title}: {cerberus_hemis_url}")

    browser.click_link_by_partial_text("Schiaparelli")
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')

    hemis_title_2 = soup3.select_one("div.content h2").text
    print(hemis_title_2)

    schiaparelli_hemis_url = browser.find_by_text("Sample")["href"]

    print(schiaparelli_hemis_url)
    print(f"{hemis_title_2}: {schiaparelli_hemis_url}")

    browser.click_link_by_partial_text("Syrtis")
    html = browser.html
    soup4 = BeautifulSoup(html, 'html.parser')

    hemis_title_3 = soup4.select_one("div.content h2").text
    print(hemis_title_3)

    syrtis_hemis_url = browser.find_by_text("Sample")["href"]

    print(f"{hemis_title_3}: {syrtis_hemis_url}")

    browser.click_link_by_partial_text("Valles")
    html = browser.html
    soup5 = BeautifulSoup(html, 'html.parser')

    hemis_title_4 = soup5.select_one("div.content h2").text
    #print(hemis_title_4)

    marineris_hemis_url = browser.find_by_text("Sample")["href"]
    print(f"{hemis_title_4}: {marineris_hemis_url}")
    
    return_dict = {
        "news_title": news_title,
        "news_head": news_head,
        "featured_img": featured_image_url,
        "table": html_table,
        "Hemisphere_urls": [hemis_url, schiaparelli_hemis_url, syrtis_hemis_url, marineris_hemis_url]}
        #print(f"{hemis_title}: {cerberus_hemis_url},\n{hemis_title_2}: {schiaparelli_hemis_url},\n{hemis_title_3}: {syrtis_hemis_url},\n{hemis_title_4}: {marineris_hemis_url}")

    browser.quit()

    return return_dict