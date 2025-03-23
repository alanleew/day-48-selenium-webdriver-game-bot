from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
website="http://secure-retreat-92358.herokuapp.com"
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)

first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
sign_up_button = driver.find_element(By.TAG_NAME, "button")

first_name_input.send_keys("Alan")
last_name_input.send_keys("Lee")
email_input.send_keys("alan@gmail.com")
# sign_up_button.click()
email_input.send_keys(Keys.RETURN)

# driver.quit()
