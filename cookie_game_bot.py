from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # This is to keep the browser open
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Uses Selenium to find elements
cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")
money = driver.find_element(By.CSS_SELECTOR, '#money')
right_panel = driver.find_elements(By.CSS_SELECTOR, "#rightPanel b")

# Creates dict to contain store item name and price, with special char removed
store = {}
for store_item in right_panel:
    if store_item.text:   # Filters to omit blank text from HTML
        text = store_item.text.split(" - ")
        store[text[0]] = text[1].replace(",","")    # Creates dictionary entry

# Creating while loop to run game bot
game_is_on = True
while game_is_on:
    timer_start = time.time()
    duration = 5  # [seconds]
    while time.time() < (timer_start + duration):   # This while loop does action for duration set above
        cookie_button.click()
    print(f"{duration} seconds have passed. There are {money.text} cookies.")

print(store)


driver.quit()
