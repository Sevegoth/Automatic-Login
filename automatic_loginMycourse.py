from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC

# "E:\Programming_Language\Python\Lib\site-packages\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://mycourses.ict.mahidol.ac.th/login/index.php")

mahidolAccount = driver.find_element(By.LINK_TEXT, "Mahidol Account Login")
mahidolAccount.click()

wait = WebDriverWait(driver,10)
username_input = driver.find_element(By.NAME,"UserName")
password_input = driver.find_element(By.NAME,"Password")
login_button = wait.until(EC.presence_of_element_located((By.ID,"submitButton")))

username_input.send_keys("u6488154")
password_input.send_keys("gzmtgzs52nm")
login_button.click()

while(0==0):
    continue
