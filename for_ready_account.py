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

METAMASK_EXT_PATH = "./metamask/10.18.4_0.crx"
EXTENSION_ID = "nkbihfbeogaeaoehlefnkodbefgpgknn"

seeds_array = []

with open("seeds.txt") as file:
    seeds_array = [row.strip() for row in file]

for i in range(len(seeds_array)):
    # Настройка отпечатка
    options = webdriver.ChromeOptions()
    options.add_extension(METAMASK_EXT_PATH)
    options.add_argument("--lang=en-US")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    print("Добавляю кошелек в метамаск")

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

    os.system("echo %s| clip" % seeds_array[i].strip())
    inputs[0].send_keys(Keys.CONTROL, "v")

    inputs[24].send_keys("123qweR!")
    inputs[25].send_keys("123qweR!")
    inputs[26].click()

    browser.find_element(By.XPATH, '//button[text()="Import"]').click()

    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="All Done"]'))
    ).click()

    print("Кошелек добавлен")

    ### ADD bsc to metamask

    print("Добавляю BSC")

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

    sleep(5)

    main_page = browser.current_window_handle

    browser.find_element(By.XPATH, '//span[text()="Add to Metamask"]').click()

    sleep(5)

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
        EC.visibility_of_element_located(
            (By.XPATH, '//button[text()="Switch network"]')
        )
    ).click()

    print("BSC добавлена")

    browser.switch_to.window(main_page)

    ### ELEMENT ->
    print("Перехожу к элементу")

    browser.get("https://element.market/bsc")

    main_page = browser.current_window_handle

    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//button[text()="Connect Wallet"]')
        )
    ).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[text()="MetaMask"]'))
    ).click()

    sleep(5)

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

    browser.get("https://element.market/reward")

    sleep(5)

    main_page = browser.current_window_handle

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[text()="Check-In"]'))
    ).click()

    sleep(5)

    for handle in browser.window_handles:
        if handle != main_page:
            metamask_page = handle

    browser.switch_to.window(metamask_page)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="Sign"]'))
    ).click()

    browser.switch_to.window(main_page)

    sleep(5)

    print("Ежедневная транзакция подписана")

    print(f"{i} - Wallet with seed: {seeds_array[i]} - DONE!")

    browser.quit()
