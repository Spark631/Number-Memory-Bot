
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

#gets the path to the chromedriver
PATH = os.getenv("PATH")
driver = webdriver.Chrome(PATH)

#goes to the website
driver.get("https://humanbenchmark.com/tests/number-memory")

#sets the wait time
almostInf = 10000**10000

while True:
    try:
        #looks for the number displayed
        numberValue = WebDriverWait(driver,almostInf).until(
            EC.presence_of_element_located((By.CLASS_NAME,"big-number"))
        )
        
        #gets the number displayed
        value = numberValue.text

        #looks for the input field
        element = WebDriverWait(driver, almostInf).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        #sends the value into the input field
        #presses first enter to submit the value and then presses enter again to cotinue
        element.send_keys(value, Keys.RETURN, Keys.RETURN)
    except:
        break





