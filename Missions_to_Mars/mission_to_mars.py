{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from splinter.exceptions import ElementDoesNotExist\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "# identify location of chromedriver and store it as a variable\n",
    "driverPath = !which chromedriver\n",
    "\n",
    "# Setup configuration variables to enable Splinter to interact with browser\n",
    "executable_path = {'executable_path': driverPath[0]}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(news_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Perseverance Rover Is Midway to Mars \n"
     ]
    }
   ],
   "source": [
    "section = soup.find('li', class_=\"slide\")\n",
    "#print(section.prettify())\n",
    "news_title = section.find('div', class_=\"content_title\").text\n",
    "#results_head = soup.find_all('div', class_=\"article_teaser_body\")\n",
    "print(news_title)\n",
    "#print(results_head)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sometimes half measures can be a good thing – especially on a journey this long. The agency's latest rover only has about 146 million miles left to reach its destination.\n"
     ]
    }
   ],
   "source": [
    "news_head = section.find('div', class_='article_teaser_body').text\n",
    "print(news_head)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "# identify location of chromedriver and store it as a variable\n",
    "driverPath = !which chromedriver\n",
    "\n",
    "# Setup configuration variables to enable Splinter to interact with browser\n",
    "executable_path = {'executable_path': driverPath[0]}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "images_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "\n",
    "browser.visit(images_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.click_link_by_id(\"full_image\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.click_link_by_partial_text(\"more info\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/spaceimages/images/largesize/PIA18185_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "image_tags = soup.select_one('figure.lede a img').get(\"src\")\n",
    "print(image_tags)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18185_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "featured_image_url = \"https://www.jpl.nasa.gov\" + image_tags\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "##JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "facts_url = \"https://space-facts.com/mars/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(facts_url)\n",
    "len(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "<class 'pandas.core.frame.DataFrame'>\n"
     ]
    }
   ],
   "source": [
    "print(type(tables))\n",
    "print(type(tables[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df =  tables[1]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>Mars - Earth Comparison</th>\n",
      "      <th>Mars</th>\n",
      "      <th>Earth</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Diameter:</td>\n",
      "      <td>6,779 km</td>\n",
      "      <td>12,742 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.39 × 10^23 kg</td>\n",
      "      <td>5.97 × 10^24 kg</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2</td>\n",
      "      <td>1</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Distance from Sun:</td>\n",
      "      <td>227,943,824 km</td>\n",
      "      <td>149,598,262 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Length of Year:</td>\n",
      "      <td>687 Earth days</td>\n",
      "      <td>365.24 days</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Temperature:</td>\n",
      "      <td>-87 to -5 °C</td>\n",
      "      <td>-88 to 58°C</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "html_table = df.to_html()\n",
    "print(html_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [],
   "source": [
    "# identify location of chromedriver and store it as a variable\n",
    "driverPath = !which chromedriver\n",
    "\n",
    "# Setup configuration variables to enable Splinter to interact with browser\n",
    "executable_path = {'executable_path': driverPath[0]}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemis_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemis_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(browser.html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n"
     ]
    }
   ],
   "source": [
    "browser.click_link_by_partial_text(\"Cerberus\")\n",
    "html = browser.html\n",
    "soup2 = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "hemis_title = soup2.select_one(\"div.content h2\").text\n",
    "print(hemis_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "cerberus_hemis_url = browser.find_by_text(\"Sample\")[\"href\"]\n",
    "print(cerberus_hemis_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced: https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "print(f\"{hemis_title}: {cerberus_hemis_url}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_unenhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.click_link_by_partial_text(\"Schiaparelli\")\n",
    "print(browser.find_by_text(\"Sample\")[\"href\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_unenhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.click_link_by_partial_text(\"Syrtis\")\n",
    "print(browser.find_by_text(\"Sample\")[\"href\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_unenhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.click_link_by_partial_text(\"Marineris\")\n",
    "print(browser.find_by_text(\"Sample\")[\"href\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = 'mongodb://localhost:27017'\n",
    "client = pymongo.MongoClient(conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "db = client.craigslist_db\n",
    "collection = db.items"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
