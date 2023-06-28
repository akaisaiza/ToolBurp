from urllib.parse import urljoin
from tldextract import extract
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def proxy_config(url):
    proxy_host = "127.0.0.1"
    proxy_port = 8080
    options = Options()
    options.add_argument(f"--proxy-server=http://{proxy_host}:{proxy_port}")
    driver = webdriver.Chrome(seleniumwire_options={
        'proxy': {
        'http': f'http://{proxy_host}:{proxy_port}',
        'https': f'http://{proxy_host}:{proxy_port}',
    },
    'verify_ssl': False  # Disable certificate verification
    }, options=options)
    driver.get(url)
    time.sleep(5)
