# The Selenium WebDriver is used to automate the Chrome browser
from selenium import webdriver

# Automatically downloads and manages the correct ChromeDriver version
from webdriver_manager.chrome import ChromeDriverManager

# Connects ChromeDriver with Selenium
from selenium.webdriver.chrome.service import Service

# Used to configure Chrome browser settings
from selenium.webdriver.chrome.options import Options



def get_Driver():
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

