import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dir = os.getcwd()
confi_file = "\Features\drivers\chromedriver.exe"
driver = webdriver.Chrome(dir + confi_file)
#driver = webdriver.Chrome(options=Options().add_experimental_option("detach", True))
driver.implicitly_wait(10)
driver.maximize_window()

