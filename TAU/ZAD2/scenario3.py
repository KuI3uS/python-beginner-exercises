import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as chop

logger = logging.getLogger('AmazonTest')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('Starting Amazon Test')

try:
    chrome_options = chop()
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.amazon.com')
    assert "Amazon" in driver.title, "Amazon title mismatch"

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_input.send_keys("Laptop" + Keys.RETURN)

    logger.info("Search query submitted.")

    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-title-instructions-style"))
    )
    product_link.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-button"))
    )
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()

    logger.info("Product added to cart.")
finally:
    driver.quit()
    logger.info("Amazon Test completed.")