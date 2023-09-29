from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import json

# Remote WebDriver configuration
#options = webdriver.ChromeOptions()
#driver = webdriver.Remote(
#    command_executor="http://selenium:4444/wd/hub",
#    options=options
#)

# Replace this URL with the URL of the page you want to scrape
url = "http://example.com"
#driver.get(url)

# Scrape titles (replace with your actual scraping code)
#titles = driver.find_elements_by_tag_name('h1')
#titles_list = [title.text for title in titles]

# Convert data to JSON
titles_list = ['hahaha']
data = json.dumps({"titles": titles_list})

# Send data to Flask server
server_url = "http://172.17.0.1:5000/recive_data"
requests.post(server_url, json=json.loads(data))

#driver.quit()
