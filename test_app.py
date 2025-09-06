import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import threading
import time
from app import app

@pytest.fixture(scope="module")
def app_url():
    def run_app():
        app.run(host='0.0.0.0', port=5001)

    flask_thread = threading.Thread(target=run_app)
    flask_thread.daemon = True
    flask_thread.start()
    time.sleep(1) 
    return "http://127.0.0.1:5001"

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    web_driver = webdriver.Chrome(options=chrome_options)
    yield web_driver
    web_driver.quit()

def test_homepage_title(driver, app_url):
    driver.get(app_url)
    welcome_text = driver.find_element(By.TAG_NAME, "h1").text
    assert "Welcome to the Python Test App!" in welcome_text
