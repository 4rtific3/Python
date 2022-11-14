from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "/Development/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")

event_dates = []
event_names = []
event_dictionary = {}

dates_raw = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
for i in dates_raw:
    event_dates.append(i.get_attribute("datetime").split("T")[0])

names_raw = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for i in names_raw:
    event_names.append(i.get_attribute("textContent"))
    
for i in range(len(event_dates)):
    event_dictionary[i] = {
        "time": event_dates[i],
        "date": event_names[i]
    }
    
print(event_dictionary)

driver.quit()