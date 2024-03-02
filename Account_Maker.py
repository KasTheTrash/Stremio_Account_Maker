from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


### Use this section only if you want to permanently add a username or password via xml format ###
##################################################################################################
#
## Specify the XML file from which we will read the data
#filename = "data.xml"
#
## Read the data from the XML file
#tree = ET.parse(filename)
#root = tree.getroot()
#
## Find the value of the <username> tag
#email = root.find("username").text
#
##################################################################################################


# Setting up Chrome options
#chrome_options = Options()
#chrome_options.add_argument('--headless')

# Initializing the Chrome WebDriver
driver = webdriver.Chrome()#(options=chrome_options)

# Target URL
url = 'https://www.stremio.com/login'
driver.get(url)

# Filling in the login form
email = driver.find_element(By.ID, "email")
email.send_keys("Your email address")

password = driver.find_element(By.ID, "password")
password.send_keys("Your password")

try:
    # Clicking the sign-in button
    button = driver.find_element(By.ID, "sign-in-button")
    button.click()

    # Waiting for potential error message
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.email-error.error"))
    )

    email_error_element = driver.find_element(By.CSS_SELECTOR, "div.email-error.error")
    if email_error_element.text == "User not found":
        # Clicking the sign-up link if user not found
        sign_up_link = driver.find_element(By.CSS_SELECTOR, ".sign-up-link")
        sign_up_link.click()

        # Filling in the registration form
        email = driver.find_element(By.ID, "email")
        email.send_keys("stremio@Strddemio.com")

        password = driver.find_element(By.ID, "password")
        password.send_keys("password")    

        passwordConfirm = driver.find_element(By.ID, "passwordConfirm")
        passwordConfirm.send_keys("password")

        termsandconditions = driver.find_element(By.CSS_SELECTOR, ".tos-consent")  
        termsandconditions.click()

        privacypolicy = driver.find_element(By.CSS_SELECTOR, ".pp-consent")  
        privacypolicy.click()

        # Marketing consent (uncomment if needed)
        # marketing = driver.find_element(By.CSS_SELECTOR, "marketing-consent")  
        # marketing.click()

        # Clicking the register button
        register = driver.find_element(By.ID, "register-button")
        register.click()

except Exception as error:
    print("An error occurred:", error)

# Adding a sleep to keep the browser open for demonstration purposes
time.sleep(100)

# Closing the WebDriver
driver.quit()
