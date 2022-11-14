from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

service = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

inputs = ["f_name", "l_name", "email@email.com"]

for i in range(3):
    active = driver.find_element(By.CSS_SELECTOR, ":focus")
    active.send_keys(inputs[i])
    active.send_keys(Keys.ENTER)