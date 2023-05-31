from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())www


# Provide the relative path to the ChromeDriver executable
path = "C:/Users/spand/OneDrive/Desktop/selenium/chromedriver.exe"

s = Service(path)
# Initialize the ChromeDriver with the correct executable path
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
