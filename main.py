import check_validity 
import proxyburp
import base_selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
logo = """            __  __  __  __  __  __                     
           / /_  __  ___________  ____ _
          / __ \/ / / / ___/ __ \/ __ `/
         / /_/ / /_/ / /  / /_/ / /_/ / 
        /_.___/\__,_/_/  / .___/  
                        /_/             
         hacker is chickens 
"""
def input_url():
    url = input("Target URL: ")
    if check_validity.validate_url(url):
        return url
    else:
        print("URL không hợp lệ.")
if __name__ == "__main__":
    print(logo)
    driver = proxyburp.proxy_config(input_url())
    base_links = base_selenium.find_links(driver)
    for link in base_links:
        new_window_script = "window.open('{}', '_blank');".format(link)
        driver.execute_script(new_window_script)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        base_selenium.auto_submit(driver)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    
