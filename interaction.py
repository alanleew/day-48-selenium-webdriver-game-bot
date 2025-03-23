from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
website="https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)

articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
articles.click()

# driver.quit()