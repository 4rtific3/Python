from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import configparser, time
from pprint import pprint

config_obj = configparser.ConfigParser()
config_obj.read("../../config.ini")
EMAIL = config_obj["emails"]["GMAIL"]
PASSWORD = config_obj["passwords"]["PERSONAL_OLD"]

service = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)

def save_jobs():
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3363352085&f_TPR=r604800&geoId=104738515&keywords=intern&location=Ireland&refresh=true&sortBy=DD")

    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in.click()
    username = driver.find_element(By.ID, "username")
    username.send_keys(EMAIL)
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASSWORD + Keys.ENTER)

    try:
        # Wait until page has loaded and try to find "Verify" button. If present, program will pause and wait for user input before continuing
        driver.find_element(By.ID, "captcha-challenge")
    except NoSuchElementException:
        pass
    else:
        input("You need to verify on the browser. Press ENTER when done")
    finally:
        # Wait for elements at the bottom of the page (page buttons) to load
        WebDriverWait(driver, timeout=5, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "artdeco-pagination__indicator")))

        # Get the page buttons and get the last page
        pages = driver.find_elements(By.CLASS_NAME, "artdeco-pagination__indicator")
        last_page = int(pages[-1].get_attribute("textContent").strip())
        
        last_7_pages = 3
        
        for page in range(last_page-1):
            
            time.sleep(1)
            WebDriverWait(driver, timeout=5, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "artdeco-pagination__indicator")))
            # Get all the job cards
            search_results = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
            
            # Slowly scroll to bottom of page to load all elements
            for i in range(7):
                driver.execute_script("container = document.querySelector('div.jobs-search-results-list')\ncontainer.scrollBy(0,500)")
                time.sleep(0.5)
            
            # Gets a list of jobs with the keyword "intern", can only get all after page has fully loaded by scrolling
            job_titles_raw = [i.find_elements(By.CSS_SELECTOR, "a.job-card-list__title")[0].get_attribute("textContent").strip() for i in search_results]
            intern_jobs = [i for i in job_titles_raw if "intern" in i.lower()]
            
            # Clicks save on each job
            for job in intern_jobs:
                link = driver.find_element(By.LINK_TEXT, job)
                driver.execute_script("arguments[0].scrollIntoView(true);", link)
                link.click()
                time.sleep(1)
                WebDriverWait(driver, timeout=5, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "jobs-save-button")))
                save_job = driver.find_element(By.CLASS_NAME, "jobs-save-button")
                save_job.click()
                time.sleep(.5)
            
            time.sleep(1)
            driver.execute_script("container = document.querySelector('div.jobs-search-results-list')\ncontainer.scrollBy(0,10000)")
            pages = driver.find_elements(By.CLASS_NAME, "artdeco-pagination__indicator")
            last_page = pages[-1].get_attribute("textContent").strip()
        
            second_page_button = pages[1].get_attribute("textContent").strip()
            second_last_page_button = pages[-2].get_attribute("textContent").strip()
            
            if second_page_button == "…" and second_last_page_button == "…":
                pages[6].click()
            elif second_last_page_button == "…":
                pages[page+1].click()
            elif second_page_button == "…":
                pages[last_7_pages].click()
                last_7_pages += 1
            else:
                pages[page].click()
                
            # Checks if page has no results
            no_results = True
            while no_results == True:
                try:
                    driver.find_element(By.CLASS_NAME, "jobs-search-no-results-banner")
                except NoSuchElementException:
                    no_results = False
                else:
                    no_results = True
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(5)
                    driver.execute_script("window.history.go(1)")
                    time.sleep(5)
    
def unsave_jobs():
    driver.get("https://www.linkedin.com/my-items/saved-jobs/")
    
    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in.click()
    username = driver.find_element(By.ID, "username")
    username.send_keys(EMAIL)
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASSWORD + Keys.ENTER)
    
    try:
        # Wait until page has loaded and try to find "Verify" button. If present, program will pause and wait for user input before continuing
        driver.find_element(By.ID, "captcha-challenge")
    except NoSuchElementException:
        pass
    else:
        input("You need to verify on the browser. Press ENTER when done")
    finally:
        while True:
            # Wait for elements at the bottom of the page (page buttons) to load
            try:
                WebDriverWait(driver, timeout=5, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ember-view")))
                dropdown = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/main/section[2]/div/ul/li[1]/div/div/div[3]/div/div[1]/button")
                dropdown.click()
                time.sleep(0.5)
                unsave = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/main/section[2]/div/ul/li[1]/div/div/div[3]/div/div[1]/div/div/div[4]")
                unsave.click()
                time.sleep(0.5)
            except NoSuchElementException:
                try:
                    next_page = driver.find_element(By.CLASS_NAME, "artdeco-pagination__button--next")
                    next_page.click()
                    time.sleep(1)
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(1)
                except NoSuchElementException:
                    return
    
command = input("Do you want to save or unsave jobs?")
if command == "save":
    save_jobs()
elif command == "unsave":
    unsave_jobs()