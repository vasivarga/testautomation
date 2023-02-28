# importam webdriver din libraria selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# constanta cu linkul pe care il vom deschide in browser
LINK = "https://formy-project.herokuapp.com/form"

# vom crea o instanta de WebDriver (de tip Chrome) pentru a putea naviga si interactiona
# cu elemente web in browserul Google Chrome
driver = webdriver.Chrome()

# instructiune pentru a deschide un URL
driver.get(LINK)

# instructiune pentru a maximiza fereastra
driver.maximize_window()

# vom declara o variabila pe care o initializam cu un Webelement
input_first_name = driver.find_element(By.ID, 'first-name')

print(type(input_first_name).__name__)
time.sleep(10)
