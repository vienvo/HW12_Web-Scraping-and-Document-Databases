#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import splinter
from splinter import Browser


# In[2]:


# Create path for Chrome Driver.
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[3]:


# Visit site mars.nasa.gov/news
browser.visit('https://mars.nasa.gov/news/')

# Create BeautifulSoup object; parse with 'html'
soup=bs(browser.html)
type(soup)


# In[4]:


# Inspect Information - too long to print out.
# print(soup.prettify)


# In[5]:


# Scrap all content_title
results = soup.find_all('div', class_='content_title')
# print(results)


# In[6]:


# Take first news title
news_title=results[0].text
print(news_title)


# In[7]:


# Scrap all news paragraph
results_p = soup.find_all('div', class_='rollover_description_inner')
# print(results_p)


# In[8]:


# Take first news paragraph
news_p=results_p[0].text
print(news_p)


# # JPL Mars Space Images - Featured Image

# In[9]:


# Visit site www.jpl.nasa.gov
browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')


# In[10]:


# Click on full_image
browser.find_by_id('full_image').click()


# In[11]:


# Create BeautifulSoup object; parse with 'html'
soup=bs(browser.html)
type(soup)


# In[12]:


# Inspect Information - too long to print out.
# print(soup.prettify)


# In[13]:


# Find feature image URL
results_pics = soup.find_all('article')
print(results_pics)


# In[14]:


# Find exact position of feature image URL
pics_string = str(results_pics[0])
position_1 = pics_string.find("('/")
position_2 = pics_string.find("')")
print(position_1)
print(position_2)


# In[15]:


portion_url = (pics_string[(position_1 + 3):(position_2)])


# In[17]:


featured_image_url = "https://www.jpl.nasa.gov/" + portion_url
print(featured_image_url)


# # Mars Weather

# In[18]:


#Visit Tweeter for Mars Weather tweet
browser.visit('https://twitter.com/marswxreport?lang=en')


# In[19]:


# Create BeautifulSoup object; parse with 'html'
soup=bs(browser.html)
type(soup)


# In[20]:


# Inspect Information - too long to print
# print(soup.prettify)


# In[21]:


# Find latest weather tweet
results_weather = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
weather_string = str(results_weather[0].text)


# In[22]:


# Inspect tweet
print(weather_string)
position_3=weather_string.find('pic.')
print(position_3)


# In[23]:


# Mars weather
mars_weather = weather_string[0:165]
print(mars_weather)


# # Mars Facts

# In[24]:


# url to space-facts
url = 'https://space-facts.com/mars/'


# In[25]:


# Create table for html
tables = pd.read_html(url)
tables


# In[26]:


# Create DataFrame
df = tables[0]
df.columns = ['Description', 'Value']
df


# In[27]:


# Convert DataFrame to HTML table string
html_table = df.to_html()
html_table


# # Mars Hemispheres

# In[118]:


#Visit Astrogeology for Mars Weather tweet
browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


# In[119]:


# List to store results:
hemisphere_image_urls = []


# In[120]:


# List of links to click through
links = ['Cerberus Hemisphere Enhanced', 'Schiaparelli Hemisphere Enhanced', 'Syrtis Major Hemisphere Enhanced', 'Valles Marineris Hemisphere Enhanced']


# In[121]:


# Loop through list of items:
for link in links:
     
    # Click through each link
    browser.click_link_by_partial_text(link)
    
    # Create Soup object
    soup=bs(browser.html)
    
    # Find title of Mars Hemispheres
    title = soup.find('h2', class_='title').text
    
    # Find link to image of Mars Hemispheres
    results_tif = soup.find_all('dd')
    url_tif=str(results_tif[1])
    pos_1 = url_tif.find('"')+1
    pos_2 = url_tif.find('tif"')+3
    img_url = url_tif[pos_1:pos_2]
    
    # Store results to dictionary
    hemisphere_image_urls.append({'title':title, 'img_url':img_url})
    
    #Visit Astrogeology for Mars Weather tweet
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    


# In[122]:


hemisphere_image_urls


# In[123]:


browser.quit()


# In[ ]:




