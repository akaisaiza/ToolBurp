import check_validity 
import proxyburp
import base_selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
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
    url = input_url()
    driver = proxyburp.proxy_config(url)
    links = base_selenium.find_links(driver)
    base_links = base_selenium.find_links_with_same_domain(url,links)
    for link in base_links:
        try:
            new_window_script = "window.open('{}', '_blank');".format(link)
            driver.execute_script(new_window_script)
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])
            base_selenium.auto_submit(driver)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print("Error occurred:", str(e))
            print("Program will wait for 10 seconds before continuing.")
            time.sleep(10)
            continue
    
