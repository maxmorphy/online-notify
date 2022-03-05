import time
from selenium
from plyer import notification

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://web.whatsapp.com/")

                title = f"{txt} is ONLINE",
                message = f"Start a conversation with {txt}. Best of Luck!",
                app_icon = "icon_online.ico",
                timeout = 72000
            )

    elif not 'online' in stateString:
        txt = "Unknown"
