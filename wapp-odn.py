import time
from selenium import webdriver
from plyer import notification

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
confirm = input("Done? (Y/N) : ")

                timeout = 72000
            )

    elif not 'online' in stateString:
        txt = "Unknown"
