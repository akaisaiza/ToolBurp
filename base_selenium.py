from urllib.parse import urljoin
from tldextract import extract
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import check_validity
from urllib.parse import urlparse


def fill_input(driver):
    """
    This function fills the input tagname
    """
    inputs = driver.find_elements(By.TAG_NAME, "input")
    if inputs :
        for input in inputs:
            input_type = input.get_attribute("type")
            if input_type == "text":
                input.send_keys("gvrvrbrgvfrbr")
                time.sleep(0.5)
            elif input_type == "email":
                input.send_keys("anhhq.workit@gmail.com")
                time.sleep(0.5)
            elif input_type == "password":
                input.send_keys("test")
                time.sleep(0.5)
            elif input_type == "number":
                input.send_keys("12345")
                time.sleep(0.5)
            elif input_type == "checkbox":
                input.click()
                time.sleep(0.5)
            elif input_type == "radio":
                input.click()
                time.sleep(0.5)
            elif input_type == "file":
                input.send_keys("file.txt")
                time.sleep(0.5)
            elif input_type == "date":
                input.send_keys("2023-06-28")
                time.sleep(0.5)
            elif input_type == "time":
                input.send_keys("10:30")
                time.sleep(0.5)
            elif input_type == "color":
                input.send_keys("#ff0000")
                time.sleep(0.5)
            elif input_type == "range":
                input.send_keys("50")
                time.sleep(0.5)

def fill_textarea_select(driver):
    """
    This function fills the textarea tagname
    """
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    if textareas :
        for textarea in textareas:
            textarea.send_keys("test")
            time.sleep(0.5)
    selects = driver.find_elements(By.TAG_NAME, "select")
    for select_element in selects:
        elect = Select(select_element)
        options = select_element.options
        if options:
            select_element.select_by_index(1)
            time.sleep(0.5)
def auto_submit(driver):
    """
    This function auto clicks the button, submit, and a tags
    """
    fill_input(driver)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    submits = driver.find_elements(By.TAG_NAME, "submit")
    links = driver.find_elements(By.TAG_NAME, "a")
    clicked_identifiers = set()  # Set to keep track of clicked class or id
    
    if buttons:
        for button in buttons:
                button.click()
                time.sleep(0.5)

    if submits:
        for submit in submits:
                submit.click()
                time.sleep(0.5)

    if links:
        for link in links:
                link.click()
                time.sleep(0.5)

def find_links(driver):
    """
    This function finds the links
    """
    links = driver.find_elements(By.TAG_NAME, "a")
    absolute_links = []
    if links:
        for link in links:
            relative_link = link.get_attribute("href")
            absolute_link = urljoin(driver.current_url, relative_link)
            if check_validity.check_link_validity(absolute_link):
                # print(absolute_link+"\n")
                absolute_links.append(absolute_link)
    return absolute_links
def find_links_with_same_domain(url, links):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    same_domain_links = []
    for link in links:
        parsed_link = urlparse(link)
        if parsed_link.netloc == domain:
            same_domain_links.append(link)

    return same_domain_links
def is_redirect(driver):
    """
    This function checks if the page is redirected after form submission
    """
    current_url = driver.current_url
    driver.refresh()
    new_url = driver.current_url
    driver.get(current_url)  # Quay lại trang gốc
    return current_url != new_url