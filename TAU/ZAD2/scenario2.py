import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as chop

logger = logging.getLogger('GoogleTest')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('Starting Google Test')

try:
    chrome_options = chop()
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.google.com')
    assert "Google" in driver.title, "Google title mismatch"

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium tutorial" + Keys.RETURN)

    logger.info("Search query submitted.")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    logger.info("Search results are visible.")
    assert "Selenium" in driver.title, "Search results title mismatch"
finally:
    driver.quit()
    logger.info("Google Test completed.")