# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import requests
import time
# beautiful soup
# from bs4 import BeautifulSoup

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


# Function to get data from WSJ
def get_wsj_data():
    # specify the url
    urlpage = 'https://www.wsj.com/market-data/stocks?\
                            mod=nav_top_subsection'

    path = 'C:\\Tony\\Projects\\Classes\\2024_Winter\\CS361_SE_I\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

    # run chrome webdriver from executable path of your choice
    driver = webdriver.Chrome(service=Service(path), options=chrome_options)

    # get web page
    driver.get(urlpage)

    # execute script to scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    # sleep for 25s to load the page content
    time.sleep(25)

    # row is a web element
    row_matches = driver.find_elements(By.TAG_NAME, 'tr')

    # Initialize a counter for detecting multiple Advancing and Declining rows
    advancing_counter = 0
    declining_counter = 0
    Nas_Comp_UVOL = 0
    Nas_Comp_DVOL = 0
    Nyse_UVOL = 0
    Nyse_DVOL = 0

    for row in row_matches:
        try:
            # Find all td elements in this row
            cells = row.find_elements(By.TAG_NAME, 'td')

            # Extract the text from each cell
            cell_texts = [cell.text for cell in cells]

            # Now cell_texts is a list of strings, each string being the text of a cell in the row
            # print(cell_texts)   # test. prints all rows

            # Define name with a default value
            name = None

            # If you want to extract specific data, you can access it by its index in the list
            # For example, if the first cell in the row contains a name, you can get it like this:
            # Check if cell_texts is not empty before trying to access its elements
            if cell_texts:
                name = cell_texts[0]
                # print(name)     # test. prints all rows

            # If the first cell's text is Advancing, increment the counter
            if name == 'Advancing':
                advancing_counter += 1
                # second Advancing, grab the second cell's text
                if advancing_counter == 2:
                    print('***Found second Advancing')
                    # print(cell_texts[1])    # test. prints Advancing rows
                    Nyse_UVOL = int(cell_texts[1].replace(',', ''))      # NYSE
                    Nas_Comp_UVOL = int(cell_texts[2].replace(',', ''))  # Nasdaq Composite

            else:
                # print('No td elements found in this row')   # test. prints all rows
                pass

            # If the first cell's text is Declining, increment the counter
            if name == 'Declining':
                declining_counter += 1
                # second Declining, grab the second cell's text
                if declining_counter == 2:
                    print('***Found second Declining')
                    # print(cell_texts[1])    # test. prints Advancing rows
                    Nyse_DVOL = int(cell_texts[1].replace(',', ''))      # NYSE
                    Nas_Comp_DVOL = int(cell_texts[2].replace(',', ''))  # Nasdaq Composite

            else:
                # print('No td elements found in this row')   # test. prints all rows
                pass

        except NoSuchElementException:
            print('Element not found')
        except StaleElementReferenceException:
            print('Element is no longer attached to the DOM')
        except TimeoutException:
            print('Wait timed out')

    print("NYSE U/D Volume percentage is ", Nyse_UVOL/(Nyse_UVOL + Nyse_DVOL) * 100, " %")
    print("Nasdaq Composite U/D Volume percentage is ", Nas_Comp_UVOL/(Nas_Comp_UVOL + Nas_Comp_DVOL) * 100, " %")

    # close the driver
    driver.quit()
