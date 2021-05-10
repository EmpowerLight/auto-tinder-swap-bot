from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

EMAIL = input("Enter your email: ")
PASSWORD = input("Enter your password: ")

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

tinder_endpoint = "https://tinder.com/"

driver.get(url=tinder_endpoint)
time.sleep(5)

sign_in_field = driver.find_element_by_class_name("button")
sign_in_field.click()
time.sleep(10)

facebook_login_field = driver.find_element_by_xpath(
    '//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/div[2]/button'
)

facebook_login_field.click()
time.sleep(10)

# switch window to facebook login page
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element_by_name("email")
email.send_keys(EMAIL)
password = driver.find_element_by_name("pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(30)

# allow location
location_allow_field = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[1]')
location_allow_field.click()
time.sleep(5)

# disallow notification
notification_disallow_field = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[2]')
notification_disallow_field.click()
time.sleep(5)

# allow cookie
cookie_accept_field = driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[2]/div/div/div[1]/button')
cookie_accept_field.click()

time.sleep(20)
count = 0
while count <= 100:
    time.sleep(5)
    try:
        print("called")
        like_button_field = driver.find_element_by_xpath(
            '//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'
        )
        like_button_field.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(5)
    count += 1

driver.quit()
