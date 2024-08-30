from bs4 import BeautifulSoup #install BeautifulSoup prior to running the code
from selenium import webdriver #install selenium prior to running the code
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

#for holding the result list
element_list = []

for page in range(1, 3, 1):
    page_url= "INSERT URL HERE" #insert the url for the site you want to scrape
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url) 
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])
with open('info.txt', 'w') as file:
    for element in element_list:
        file.write(f"Title: {element[0]}, Price: {element[1]}, Description: {element[2]}, Rating: {element[3]}\n")

print(element_list)

driver.close()

