from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.support import expected_conditions as EC





def get_data():

    driver = webdriver.Chrome()  # Replace with your browser's driver, e.g., FirefoxDriver
    url = "https://www.imdb.com/title/tt1663202/reviews/?ref_=tt_urv_sm"  # Replace with the actual URL
    driver.get(url)
    driver.maximize_window()

    loop_count=0
    loop_limit=20


    try:
        while loop_count<loop_limit:
            # Check if the button exists and is clickable
            try:
                all_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-base ipc-btn--theme-base ipc-btn--button-radius ipc-btn--on-accent2 ipc-text-button ipc-see-more__button']")))
                # Click the button using JavaScript to handle potential interception
                driver.execute_script("arguments[0].click();", all_button)
                print("Clicked 'ALL' button. Waiting for content to load...")
                time.sleep(5)  # Wait for content to load
            except Exception:
                # If the button no longer exists, exit the loop
                print("'ALL' button no longer exists. Exiting loop.")
                break

            # Optional: Scroll down to load additional content if needed
            loop_count += 1
            driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(10)  # Adjust the sleep time as necessary

        print("Finished loading all content.")
        
        if loop_count == loop_limit:
            print("Maximum loop count reached. Exiting loop.")
        else:
            print("Finished loading all content.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        

    # Parse the fully loaded page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract names and comments
    names = []
    comments = []    



    for tr in soup.find_all('article', {'class': 'sc-f53ace6f-1 cHwTOl user-review-item'}):
        name = tr.find('a', {'class': 'ipc-link ipc-link--base'})
        comment = tr.find('div', {'class': 'sc-a2ac93e5-5 feMBGz'})
        if name is not None and comment is not None:
            names.append(name.text)
            comments.append(comment.text)
            
    # Close the WebDriver
    driver.quit()
    data = pd.DataFrame({
    'names': names,
    'comments': comments})   
    



    
    def remove_emojis(text):
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # Emoticons
            "\U0001F300-\U0001F5FF"  # Symbols & pictographs
            "\U0001F680-\U0001F6FF"  # Transport & map symbols
            "\U0001F700-\U0001F77F"  # Alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric shapes extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"  # Enclosed characters
            "]+",
            flags=re.UNICODE
        )
        return emoji_pattern.sub(r'', text)

    # Apply the function to the 'text' column
    data['comments'] = data['comments'].apply(remove_emojis)
    data.to_csv('/home/khalil/vs_workspace/ETL_project/data.csv', index=False)



#data=get_data()      
