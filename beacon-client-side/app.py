from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import requests
import json


def scrape():
    url = "https://www.dhl.com/nl-nl/home/traceren.html?tracking-id=awdwa&submit=1"
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    try:
        driver = webdriver.Remote(
            command_executor="http://0.0.0.0:4444/wd/hub",
            options=options
        )
        driver.get(url)
        print("Page HTML:", driver.page_source)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.c-tracking-result-message--content"))
        ).text
        print("Tracking Result:", element)
        data = {
            "tracking_id": "awdwa",
            "tracking_result": element
        }
        send(data)
    except WebDriverException as e:
        print("The page crashed. Error:", str(e))
    except Exception as e:
        print("An error occurred while scraping:", str(e))
    finally:
        driver.quit()


def send(data):
    server_url = "http://172.17.0.1:5000/receive_data"
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post(
            server_url, data=json.dumps(data), headers=headers)
        print("Response from server:", response.text)
    except Exception as e:
        print("An error occurred while sending data to the server:", str(e))


if __name__ == "__main__":
    print("Starting scraping process...")
    scrape()
    print("Scraping process completed.")
