from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
website="https://www.python.org"
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)

ul = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
li = ul.find_elements(By.TAG_NAME, "li")

times = [event.find_element(By.TAG_NAME, "time").text for event in li]
names = [event.find_element(By.TAG_NAME, "a").text for event in li]

# This does the same as the code below. Just wanted to practice dictionary comprehension.
dict = {}
for i in range(len(times)):
    dict[i] = {'time': times[i],
               'name': names[i]}
print(dict)

dict_comp = {i:{'time': times[i],'name': names[i]} for i in range(len(times))}
print(dict_comp)

# driver.close()
driver.quit()

