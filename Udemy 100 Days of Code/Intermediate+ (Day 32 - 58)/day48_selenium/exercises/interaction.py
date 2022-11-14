# Base import
from selenium import webdriver
# Import By function for find_element method
from selenium.webdriver.common.by import By
# Import Keys function for send_keys method (pressing a key on a keyboard i.e. Enter)
from selenium.webdriver.common.keys import Keys
# Import Service to manage ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Import ChromeDriverManager to create webdriver object with chromedriver.exe (executable_path deprecated)
from webdriver_manager.chrome import ChromeDriverManager
# Changing options such as "detach" and extensions
from selenium.webdriver.chrome.options import Options

options = Options()
# Keeps browser open after code is completed
options.add_experimental_option("detach", True)
# Removes USB error and DevTools listening prompts
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(ChromeDriverManager().install())

chrome_driver_path = "/Development/chromedriver.exe"
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Clicking a button by finding by CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# Clicking a button by finding by text contained within <a>/anchor tag
random_article = driver.find_element(By.LINK_TEXT, "Random article")
# random_article.click()

# Entering values into an input area and pressing Enter
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)