from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import random, time, string
import selenium

alphabet = string.ascii_letters + string.digits
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


try:
    log_file = open('accs.txt', 'a')
except FileNotFoundError:
    log_file = open('accs.txt', 'w+')

for i in range(int(input("How many email accs to generate? "))):
    driver = webdriver.Chrome(service=service)
    driver.get('https://login.inbox.lv/signup?go=portal')
    while 1:
        try:
            search = driver.find_element(By.ID, "signup_user")
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break

    password = ''.join(random.choice(alphabet) for x in range(16))
    name = ''.join(random.choice(alphabet) for x in range(5))

    with open('first_names.txt', 'r') as f:
        fname = f.readlines()[random.randint(1, 4900)].capitalize().replace('\n', '')
    with open('last_names.txt', 'r') as f:
        surname = f.readlines()[random.randint(1, 88700)][1:].capitalize().replace('\n', '')

    search.send_keys(name)
    search = driver.find_element(By.ID, "signup_password_password")
    driver.implicitly_wait(0.3)
    search.send_keys(password)
    search = driver.find_element(By.ID, "signup_password_passwordRepeat")
    driver.implicitly_wait(0.3)
    search.send_keys(password)
    search = driver.find_element(By.ID, "signup_forename")
    driver.implicitly_wait(0.3)
    search.send_keys(fname)
    search = driver.find_element(By.ID, "signup_surname")
    driver.implicitly_wait(0.3)
    search.send_keys(surname)
    search = driver.find_element(By.ID, "signup_privacy")
    driver.implicitly_wait(0.3)
    search.click()
    search = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[3]/button[2]')
    driver.implicitly_wait(0.3)
    search.click()
    search = driver.find_element(By.ID, "signup_tos")
    driver.implicitly_wait(0.3)
    search.click()
    search = driver.find_element(By.ID, "signup_submit")
    driver.implicitly_wait(0.3)
    search.click()

    while 1:
        try:
            search = driver.find_element(By.ID, 'btn_proceed')
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break

    search.click()

    log = ':'.join([fname, surname, name, password])
    log_file.write(log + '\n')
    print("GENERATED: '" + fname, surname + "' :", "'" + name + "' : '" + password + "'")
    driver.close()

print("FINISHED")
log_file.close()