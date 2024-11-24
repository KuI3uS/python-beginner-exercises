import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as chop

logger = logging.getLogger('GitHubTest')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('Starting GitHub Test')

try:
    chrome_options = chop()
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.github.com')
    assert "GitHub" in driver.title, "GitHub title mismatch"

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.send_keys("Selenium" + Keys.RETURN)

    logger.info("Search query submitted.")

    repo_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.repo-list li a"))
    )
    repo_link.click()

    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium")
    )
    logger.info("Repo page loaded.")
finally:
    driver.quit()
    logger.info("GitHub Test completed.")