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

# get the HTML content text
# html = driver.page_source

# row is a web element
row_matches = driver.find_elements(By.TAG_NAME, 'tr')

# # store the data in a list
# name_col = []
# advance_col = []
# decline_col = []

# # row is a web element
# for row in row_matches:
#     print(row.text)
#     if row.text[0] == 'Advancing':
#         print('***Found Advancing')

    # name_col = row.find_element(By.XPATH, './/td[1]').text     # //tr/td[1]
    # print(name_col)
    # advance_col = row.find_element(By.XPATH, './/td[2]').text     # //tr/td[2]
    # # print(advance_col)
    # decline_col = row.find_element(By.XPATH, './/td[3]').text     # //tr/td[3]
    # # print(decline_col)

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
        print(cell_texts)

        # Define name with a default value
        name = None


        # If you want to extract specific data, you can access it by its index in the list
        # For example, if the first cell in the row contains a name, you can get it like this:
        # Check if cell_texts is not empty before trying to access its elements
        if cell_texts:
            name = cell_texts[0]
            print(name)

            
        # If the first cell's text is Advancing, increment the counter
        if name == 'Advancing':
            advancing_counter += 1
            # second Advancing, grab the second cell's text
            if advancing_counter == 2:
                print('***Found second Advancing')
                print(cell_texts[1])                # NYSE
                Nyse_UVOL = int(cell_texts[1].replace(',', ''))      # NYSE
                Nas_Comp_UVOL = int(cell_texts[2].replace(',', ''))  # Nasdaq Composite

        else:
            print('No td elements found in this row')

        # If the first cell's text is Declining, increment the counter
        if name == 'Declining':
            declining_counter += 1
            # second Declining, grab the second cell's text
            if declining_counter == 2:
                print('***Found second Declining')
                print(cell_texts[1])                # NYSE
                Nyse_DVOL = int(cell_texts[1].replace(',', ''))      # NYSE
                Nas_Comp_DVOL = int(cell_texts[2].replace(',', ''))  # Nasdaq Composite

        else:
            print('No td elements found in this row')

    except NoSuchElementException:
        print('Element not found')
    except StaleElementReferenceException:
        print('Element is no longer attached to the DOM')
    except TimeoutException:
        print('Wait timed out')

print("NYSE U/D Volume percentage is ", Nyse_UVOL/(Nyse_UVOL + Nyse_DVOL) * 100)
print("Nasdaq Composite U/D Volume percentage is ", Nas_Comp_UVOL/(Nas_Comp_UVOL + Nas_Comp_DVOL) * 100)

# # html_text = requests.get('https://www.wsj.com/market-data/stocks?\
# #                          mod=nav_top_subsection').text

# soup = BeautifulSoup(html, 'lxml')
# # # print(soup.prettify()[:1000])  # Print the first 1000 characters
# with open('./soup.txt', 'w', encoding='utf-8') as f: f.write(str(soup))



# div_class = soup.find('div', id="root")
# # print(div_class[:1000])
# with open('./div_class.txt', 'w', encoding='utf-8') as f:
#     f.write(str(div_class))



# div_class2 = div_class.find_all('div', class_='')
# print(len(div_class2))
# # print(div_class2[:1000])
# with open('./div_class2.txt', 'w', encoding='utf-8') as f:
#     f.write(str(div_class2))




# for element in div_class2:
#     print(element[:1000])
#     market_diary = element.find('div', class_="style--grid--SxS2So51 ")
#     if market_diary:
#         # print(market_diary[:1000])
#         with open('./market_diary.txt', 'w', encoding='utf-8') as f: 
#             f.write(str(market_diary))



# # p190_col = div_class.find('div', class_="style--column--1p190TxH ")
# # print(p190_col[:1000])
# # with open('./p190_col.txt', 'w', encoding='utf-8') as f:
# #     f.write(str(p190_col))




# # adv_row = div_class.find('tbody', class_="WSJTables--table__body--3Y0p0d6H ")
# # print(adv_row)





# # adv_num = soup.find('td', class_="WSJTables--table__cell--2u6629rx\
# #                      WSJTheme--table__cell--3njwWeaF ")
# # print(adv_num)




# # with open('./market_diary.txt', 'r', encoding='utf-8') as \
# #     f: contents = f.read()

# # soup2 = BeautifulSoup(contents, 'lxml')







# # data_table = market_diary.find('table', class_="WSJTables--table--1QzSOCfq \
# #                            WSJTheme--table--Tzxxxq4J ").text
# # print(market_diary)
# # # company_name = job.find('h3', class_ = 'joblist-comp-name').text
# # # print(company_name)
# # print(job)

# # for diary in market_diary:
# #     data_table = diary.find('table', class_="WSJTables--table--1QzSOCfq")
# #     print(data_table)

# # data_table = market_diary[0].find('table', class_="WSJTables--table--1QzSOCfq")


# close the driver
driver.quit()
