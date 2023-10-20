from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://mycourses.ict.mahidol.ac.th/login/index.php")

mahidolAccount = driver.find_element(By.LINK_TEXT, "Mahidol Account Login")
mahidolAccount.click()

wait = WebDriverWait(driver,10)
username_input = driver.find_element(By.NAME,"UserName")
password_input = driver.find_element(By.NAME,"Password")
login_button = wait.until(EC.presence_of_element_located((By.ID,"submitButton")))

username_input.send_keys("your username")
password_input.send_keys("your password")
login_button.click()

# In case it will close the window, using the code below to keep the window activing
# while(0==0):
#    continue
