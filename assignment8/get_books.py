#Task 1: Reviewed "robots.txt" for Durham County Library
#Task 2: Document necessary tags
    # search li: class="cp-search-result-item"
    # titles: class="title-content
    # authors: class="author-link"

# Task 3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

try:      
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Enable headless mode
    options.add_argument('--disable-gpu')  # Optional, recommended for Windows
    options.add_argument('--window-size=1920x1080')  # Optional, set window size

    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    title = driver.title # Find the title. Parts of the header are accessed directly, not via find_element(), which only works on the body
    print(f"Title: {title}")

    body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one
    
    links = driver.find_elements(By.CLASS_NAME,"cp-search-result-item")
    # print(links.text)
    results = []

    for items in links:
        #titles
        title = items.find_element(By.CLASS_NAME,"title-content").text
        # print(title.text)
        try:
            #authors
            find_authors = items.find_elements(By.CLASS_NAME,"author-link")
            find_format_year = items.find_elements(By.CLASS_NAME,"display-info-primary")
        except:
            print("No author found!")
        
        #Account for multiple authors
        get_authors = []
        for details in find_authors:
            # append authors
            get_authors.append(details.text)
        # Use ";" for multiple authors
        authors = ";".join(get_authors)
        
        #format and year
        get_format_year = []
        for info in find_format_year:
            get_format_year.append(info.text)
            # print(get_format_year)
        # append title, authors, and year to results
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": get_format_year
        })
        
        final = pd.DataFrame(results)
        print(final)
        
except Exception as e:
    print(f"An exception occurred: {type(e).__name__}{e}")
finally:
    driver.quit()