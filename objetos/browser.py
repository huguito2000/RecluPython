from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import webdriver_manager.chrome
global driver

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=options)
driver.get("https://involveprereclu.involverh.com.mx/login")
