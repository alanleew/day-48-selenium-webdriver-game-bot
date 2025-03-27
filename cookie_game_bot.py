from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # This is to keep the browser open
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Uses Selenium to find elements
cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")
money = driver.find_element(By.CSS_SELECTOR, '#money')

def choose_store_item():
    """Returns the item name to allow Selenium to click according to the button name"""
    right_panel = driver.find_elements(By.CSS_SELECTOR, "#rightPanel b")
    store = {}  # Creates dict to contain store item and price
    for store_item in right_panel:
        if store_item.text:  # Filters to omit blank text from HTML
            text = store_item.text.split(" - ")
            store[text[0]] = int(text[1].replace(",", "")) # Adds entry to dict

    # Iterates from highest to lowest price to return the item name
    for key, value in reversed(store.items()):
        if int(money.text.replace(",", "")) > value:
            chosen_item = driver.find_element(By.CSS_SELECTOR, f"#buy{key}")
            chosen_item.click()
            return

game_is_on = True  # Creating while loop to run game bot
game_timer_start = time.time()
game_duration = 60 # [seconds]
while game_is_on:
    click_timer_start = time.time()
    if (click_timer_start - game_timer_start) < game_duration:
        click_duration = 10 # [seconds]
        while time.time() < (click_timer_start + click_duration):  # This while loop does action for duration set above
            cookie_button.click()
        # print(f"{duration} seconds have passed. There are {money.text} cookies.")
        choose_store_item()
    else:
        print(f"{game_duration} seconds have passed.\nYou ended with {money.text} cookies!")
        break

driver.quit()
