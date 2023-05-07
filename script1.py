#python that i used python-3.11.3-amd64
#Name: selenium Version: 4.9.0
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Initialyze the variables for the login
email = "admin@schoox.com"
password = "123456"

# create a Service object
service = Service("C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("http://qatest.schoox.com/login")
time.sleep(2)

#login with user
driver.find_element(By.XPATH, ".//input[@type='email']").send_keys(email)
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
driver.find_element(By.XPATH, ".//button[@type='submit']").click()

#Go to https://qatest.schoox.com/training dont use https - cannot save the password
driver.get("http://qatest.schoox.com/training")
driver.find_element(By.XPATH, ".//i[text()='QA']").click()
time.sleep(2)

#I searched for the names from the courses and printed the results table.
#If any of the courses were not there, it would show an error
website_array = []
element1 = driver.find_element(By.XPATH, "//b[text()='QA course']")
element2 = driver.find_element(By.XPATH, "//b[text()='ΒΑ course']")
element3 = driver.find_element(By.XPATH, "//b[text()='Μάθημα για τους Devs']")
element4 = driver.find_element(By.XPATH, "//b[text()='Μάθημα για automation']")

text1 = element1.text
text2 = element2.text
text3 = element3.text
text4 = element4.text

website_array.append(text1)
website_array.append(text2)
website_array.append(text3)
website_array.append(text4)

print(website_array)

# Find all elements with class name "course_title".
elements = driver.find_elements(By.CLASS_NAME, "course_title")

# Get the number of elements
num_of_elements = len(elements)

# Print the number of elements
print("Number of elements: ", num_of_elements)

#Check  if the list contains only the 4 items
if num_of_elements == 4:
    print("The list contains only the following items")
else:
    print("The list does not contains only the following items")

time.sleep(5)
driver.quit()

# John Ktenidis 07/05/2023

