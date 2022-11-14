from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "/Development/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/dp/B09RKGQB99/ref=vp_d_pb_TIER3_d3_lp_B07PPD1H64_pd?_encoding=UTF8&pf_rd_p=7ff5771e-3d64-43df-8374-83d5fdf6e104&pf_rd_r=Q1CY0BJ5P79JBN0DQC6Q&pd_rd_wg=1FrC0&pd_rd_i=B095Y6ZF5Q&pd_rd_w=nbE17&content-id=amzn1.sym.7ff5771e-3d64-43df-8374-83d5fdf6e104&pd_rd_r=d7784e61-989f-4fc5-ae07-3fbdbbad8dc3&th=1&language=en_US&currency=EUR")

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price.get_attribute("textContent"))
# text is a selenium command that as I said earlier will get the visible text (will also get styling such as a transform to UPPER).
# innerHTML will get any html inside your element, so if there's a span inside your element you will also get the html for that.
# textContent is just the text inside your element and no html tags, but does not care about visibility as it is a DOM property

driver.quit()