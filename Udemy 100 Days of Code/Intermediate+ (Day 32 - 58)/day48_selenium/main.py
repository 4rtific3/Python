from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set of imports to handle stale element reference exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from datetime import datetime, timedelta
import time

service = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)

save_file = ""

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
toggle_numbers = driver.find_element(By.ID, "toggleNumbers")
toggle_flash = driver.find_element(By.ID, "toggleFlash")
toggle_numbers.click()
toggle_flash.click()

cursor_price = driver.find_element(By.ID, "buyCursor")
grandma_price = driver.find_element(By.ID, "buyGrandma")
factory_price = driver.find_element(By.ID, "buyFactory")
mine_price = driver.find_element(By.ID, "buyMine")
shipment_price = driver.find_element(By.ID, "buyShipment")
lab_price = driver.find_element(By.ID, "buyAlchemy lab")
portal_price = driver.find_element(By.ID, "buyPortal")
tmachine_price = driver.find_element(By.ID, "buyTime machine")

element_ids = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma", "buyCursor"]
web_element_list = [tmachine_price, portal_price, lab_price, shipment_price, mine_price, factory_price, grandma_price, cursor_price]
price_list = [int(i.find_element(By.TAG_NAME, "b").text.split("-")[1].strip().replace(",", "")) for i in web_element_list]

# for i in range(100):
#     cookie.click()
# price_list[7].click()

# if save_file != "":
#     import_save = driver.find_element(By.ID, "importSave")
#     import_save.click()
#     input_save = driver.find_element(By.CSS_SELECTOR, ":focus")
#     input_save.send_keys(save_file)

now = datetime.now()
five_mins = now + timedelta(minutes=5)
clicks = 1000

while now < five_mins:
    for i in range(clicks):
        cookie.click()
    for i in range(8):
        current_cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        while current_cookies > price_list[i]:
            web_element_list[i] = driver.find_element(By.ID, element_ids[i])
            upgrade = WebDriverWait(driver, timeout=5, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, element_ids[i])))
            upgrade.click()
            current_cookies -= price_list[i]
            time.sleep(.025)
    now = datetime.now()

cookies_per_sec = driver.find_element(By.ID, "cps")
stats = f"{clicks}: {cookies_per_sec}"

with open("stats.txt", "w") as df:
    df.append(stats)