from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

#Initialyze the variables
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

#go to http://qatest.schoox.com/6/steps
driver.get("http://qatest.schoox.com/6/steps")

#find the Category QA and click it
driver.find_element(By.XPATH, ".//div[@class='enroll']").click()
time.sleep(5)

# I use range(4) because the courses are 4 . I find the elements that are in "course_steps_right" class
# I use alert function and accept it using the accept() method
for i in range(4):
    element = driver.find_element(By.XPATH, ".//div[@class='course_steps_right']")
    element.click()
    alert = Alert(driver)
    alert.accept()

#I find the element that is in "top_course_progress"  I extract the text
#then I extract the progress percentage value from a string that contains a progress update message.
#with a code snippet
element2 = driver.find_element(By.CLASS_NAME, "top_course_progress")
progress_text = element2.text
progress_percentage = float(progress_text.split(": ")[1].strip("%"))

# I validate the progress with an  if-else statement that
#checks the value of the progress_percentage variable and prints a message depending on the value.
if progress_percentage == 100.0:
    print("the progress is 100%")
else:
    print("the progress is ",progress_percentage)

time.sleep(5)
driver.quit()

#Second way how to navigate and click elements
     #try:
       #element = WebDriverWait(driver,5).until(
       #  EC.presence_of_element_located(By.XPATH,.//div[@class='course_steps_right']")
       # )
       # element.click()
    #except:
       #driver.quit()

# I couldn't get all four links to turn green in either of the 2 ways
# John Ktenidis 07/05/2023
