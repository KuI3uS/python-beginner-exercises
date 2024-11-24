import logging
from asyncio import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options as chop
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edg
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('Start of the test scenario')

DRIVER_NAMES = ['Chrome', 'Edge']

for driver_name in DRIVER_NAMES:
    try:
        if 'Chro' in driver_name:
            logger.info(f'Starting test with {driver_name} browser')
            chrome_options = chop()
            driver = webdriver.Chrome(options=chrome_options)
        else:
            logger.info(f'Starting test with {driver_name} browser')
            edge_options = edg()
            driver = webdriver.Edge(options=edge_options)

        driver.get('https://www.youtube.com')

        # Akceptowanie plików cookies
        try:
            accept_cookies = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Accept")]'))
            )
            accept_cookies.click()
            logger.info("Cookies accepted")
        except Exception:
            logger.warning("Cookies accept button not found or skipped")

        # Szukanie wideo
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_input.send_keys("Gleipnir Anime Trailer")
        search_input.send_keys(Keys.RETURN)

        logger.info("Searching for video...")

        # Kliknięcie w pierwszy wynik
        video_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="video-title"]'))
        )
        video_link.click()
        logger.info("Clicked on video")

        # Sprawdzanie URL
        sleep(2)  # Alternatywnie dynamiczne sprawdzenie URL
        current_url = driver.current_url
        expected_url = "https://www.youtube.com/watch?v="
        assert expected_url in current_url, f"URL mismatch. Expected part: {expected_url}, got: {current_url}"

        logger.info(f"Correct transfer to the video page: {current_url}")

    except Exception as e:
        logger.error(f"Test failed for {driver_name}: {e}")
    finally:
        driver.quit()
        logger.info(f"End of the test scenario for {driver_name} browser")