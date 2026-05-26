#Task 6
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import csv

try:      
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Enable headless mode
    options.add_argument('--disable-gpu')  # Optional, recommended for Windows
    options.add_argument('--window-size=1920x1080')  # Optional, set window size

    driver.get("https://owasp.org/Top10/2025/")
    title = driver.title # Find the title.
    print(f"Title: {title}")

    body = driver.find_element(By.CSS_SELECTOR,'body') 
    
    # <h3></h3>
    # <ol></ol>
    main_title = driver.find_element(By.XPATH,"//h3")
    ol_div = driver.find_element(By.XPATH,".//h3/following-sibling::ol")
    lis = ol_div.find_elements(By.CSS_SELECTOR,"li")
    
    top_ten = []
    for items in lis:
        try:
            titles = items.find_element(By.CSS_SELECTOR,"a")
            hrefs = titles.get_attribute('href')
        except:
            print("Incorrect titles and links!")
            
        final_hrefs = []
        final_hrefs.append(hrefs)

        # place title & href links in dict
        top_ten.append({
            "Title": titles.text,
            "Hrefs": hrefs
        })
        print(top_ten)
        
        #save to csv file:
        with open("assignment8/owasp_top_10.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(top_ten)
            
except Exception as e:
    print(f"An exception occurred: {type(e).__name__}{e}")
finally:
    driver.quit()