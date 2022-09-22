import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

load_dotenv()

PATH1 = "./element/metamask/10.18.4_0.crx"
PATH2 = "./element/xpath/1.0.2_0.crx"
SEED = os.getenv("SEED")


EXTENSION_ID = "nkbihfbeogaeaoehlefnkodbefgpgknn"

# Настройка отпечатка
options = webdriver.ChromeOptions()
options.add_extension(PATH1)
options.add_extension(PATH2)
options.add_argument("--lang=en-US")
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

browser.get(
    "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome"
)

sleep(1)

window_name = browser.window_handles[1]
browser.switch_to.window(window_name=window_name)
browser.close()

metamask_window = browser.window_handles[0]
browser.switch_to.window(window_name=metamask_window)

browser.find_element(By.XPATH, '//button[text()="Get Started"]').click()
browser.find_element(By.XPATH, '//button[text()="No Thanks"]').click()
browser.find_element(By.XPATH, '//button[text()="Import wallet"]').click()

inputs = browser.find_elements(By.XPATH, "//input")

os.system("echo %s| clip" % SEED.strip())
inputs[0].send_keys(Keys.CONTROL, "v")

inputs[24].send_keys("123qweR!")
inputs[25].send_keys("123qweR!")
inputs[26].click()

browser.find_element(By.XPATH, '//button[text()="Import"]').click()

WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="All Done"]'))
).click()

### ADD bsc to metamask

browser.get("https://chainlist.org/")

main_page = browser.current_window_handle

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//span[text()="Connect Wallet"]'))
).click()

sleep(2)

for handle in browser.window_handles:
    if handle != main_page:
        metamask_page = handle

browser.switch_to.window(metamask_page)

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Next"]'))
).click()
WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Connect"]'))
).click()

browser.switch_to.window(main_page)

chainlist_inputs = browser.find_elements(By.XPATH, "//input")
chainlist_inputs[0].send_keys("bsc")

sleep(2)

main_page = browser.current_window_handle

browser.find_element(By.XPATH, '//span[text()="Add to Metamask"]').click()

sleep(2)

for handle in browser.window_handles:
    if handle != main_page:
        metamask_page = handle

browser.switch_to.window(metamask_page)
browser.maximize_window()

sleep(5)

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Approve"]'))
).click()
WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Switch network"]'))
).click()

browser.switch_to.window(main_page)

### ELEMENT ->
browser.get(os.getenv("INV_LINK"))

main_page = browser.current_window_handle

WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Accept invitation"]'))
).click()
WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//span[text()="MetaMask"]'))
).click()


sleep(2)

for handle in browser.window_handles:
    if handle != main_page:
        metamask_page = handle

browser.switch_to.window(metamask_page)

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Next"]'))
).click()
WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Connect"]'))
).click()

browser.switch_to.window(main_page)

sleep(5)

main_page = browser.current_window_handle

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Accept invitation"]'))
).click()
WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Confirm"]'))
).click()

sleep(10)

for handle in browser.window_handles:
    if handle != main_page:
        metamask_page = handle

browser.switch_to.window(metamask_page)

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Sign"]'))
).click()

browser.switch_to.window(main_page)

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Done"]'))
).click()

sleep(100000)
