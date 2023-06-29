import check_validity 
import proxyburp
import base_selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import xml.etree.ElementTree as ET
import burp_history
# def get_burp_history_urls(filename):
#     urls = set()
#     try:
#         tree = ET.parse(filename)
#         root = tree.getroot()
#         items = root.findall(".//item")
#         for item in items:
#             url = item.findtext("url")
#             if url:
#                 urls.add(url)
#     except ET.ParseError as e:
#         print("Error occurred:", str(e))
#     return urls
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
    base_links = base_selenium.find_links_with_same_domain(url, links)
    clicked_links = set()  # Set to keep track of clicked links

    while base_links:
        link = base_links.pop(0)  # Lấy liên kết đầu tiên trong danh sách
        try:
            if link in clicked_links:
                continue  # Bỏ qua liên kết nếu đã được click trước đó

            new_window_script = "window.open('{}', '_blank');".format(link)
            driver.execute_script(new_window_script)
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])
            base_selenium.auto_submit(driver)

            new_links = base_selenium.find_links_with_same_domain(url, driver.page_source)
            for new_link in new_links:
                if new_link not in base_links:
                    base_links.append(new_link)  # Thêm các liên kết mới vào danh sách base_links

            clicked_links.add(link)  # Đánh dấu liên kết đã được click
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print("Error occurred:", str(e))
            print("Program will wait for 10 seconds before continuing.")
            time.sleep(10)
            continue

    burp_api_url = "http://127.0.0.1:8080/burp/"
    urls = burp_history.extract_urls_from_burp_history(burp_api_url)
    for url in urls:
        print("URL:", url)
