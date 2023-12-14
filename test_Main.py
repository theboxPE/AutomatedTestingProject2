from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_element_inicio():
    driver = webdriver.Chrome()
    driver.get('https://pelotainvernal.com/')

    time.sleep(2)


def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('https://pelotainvernal.com/')
    
    #list
    web_element = driver.find_elements(By.CLASS_NAME, 'nav-link')
    print("Cantidad elementos clase: ", len(web_element))

    time.sleep(2)


def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    web_element = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    web_element.click()

    time.sleep(2)


def test_element_by_Id():
    driver = webdriver.Chrome()
    driver.get('https://pelotainvernal.com/')

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/section[1]/h4[3]/a").click()

    time.sleep(2)


def test_element_by_xpath():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[1]/a").click()

    time.sleep(2)


def test_element_by_xpath2():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[2]/a").click()

    time.sleep(2)


def test_element_by_xpath3():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[3]/a").click()

    time.sleep(2)


def test_element_by_xpath4():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[4]/a").click()

    time.sleep(2)


def test_element_by_xpath5():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[5]/a").click()

    time.sleep(2)


def test_element_by_xpath_name():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[2]/a").click()
    driver.find_element(By.NAME, "name").send_keys("Wao")

    time.sleep(2)


def test_element_by_xpath_class():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[2]/a").click()
    driver.find_element(By.CLASS_NAME , "form-control").send_keys("Funciona")

    time.sleep(2)


def test_element_by_xpath_xpath():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.XPATH, "/html/body/footer/div/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/section[1]/form/div[3]/div/div/input").send_keys("Eso es lo que se quiere")

    time.sleep(2)


def test_element():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.CLASS_NAME, "navbar-toggler-icon").click()
    driver.find_element(By.CLASS_NAME, "nav-link dropdown-toggle show").click()

    time.sleep(2)


def test_element():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.CLASS_NAME, "navbar-toggler-icon").click()
    driver.find_element(By.XPATH, '//*[@id="w0-collapse"]/ul/li[2]/a').click()

    time.sleep(2)


def test_element2():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.CLASS_NAME, "navbar-toggler-icon").click()
    driver.find_element(By.XPATH, '//*[@id="w0-collapse"]/ul/li[2]/ul/li[3]/a').click()

    time.sleep(2)


def test_element3():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.CLASS_NAME, "navbar-toggler-icon").click()
    driver.find_element(By.XPATH, '//*[@id="w0-collapse"]/ul/li[2]/ul/li[1]/a').click()

    time.sleep(2)


def test_element4():
    driver = webdriver.Chrome()
    driver.get("https://pelotainvernal.com/")

    driver.find_element(By.CLASS_NAME, "navbar-toggler-icon").click()
    driver.find_element(By.XPATH, '//*[@id="w0-collapse"]/ul/li[3]/a').click()

    time.sleep(2)