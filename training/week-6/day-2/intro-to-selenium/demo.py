from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# make sure you install selenium and webdriver-manager

# Instantiate a driver object, which will open a web browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome("./chromedriver.exe") => DEPRECATED

# Call the get() method passing in the URL you want to go to
driver.get("https://google.com/")
print(driver.title)  # text in the browser tab => HTML <title>Pixabay</title> => Google

# find_element: returns a single object that represents the first occuring element in the HTML document
# that match what we are finding elements by
google_search_input_element = driver.find_element(By.NAME, "q")

google_search_input_element.send_keys("python tutorials")  # keyboard input "python tutorials"

# find_elements: returns a list of elements that match what we are finding elements by
google_search_button_within_dropdown = driver.find_elements(By.NAME, "btnK")[0]  # We start @ indx 0 (first occurance)
google_search_button_within_dropdown.click()


time.sleep(10)  # pause execution for 10 secs (or else the browser closes immediately)

driver.quit()  # terminate the browser
