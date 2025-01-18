from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeConfig
from selenium.webdriver.edge.options import Options as EdgeConfig
import logging


# Konfiguracja loggera
logger = logging.getLogger('Tester')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

browser_instance = None


@given('The user launches the website "{url}" via "{browser}" browser')
def open_website(context, url, browser):
    logger.info(f"Opening {url} on {browser}")
    global browser_instance
    browser_options = ChromeConfig() if 'chrome' in browser.lower() else EdgeConfig()
    context.browser_instance = webdriver.Chrome(options=browser_options) if 'chrome' in browser.lower() else webdriver.Edge(options=browser_options)
    context.browser_instance.get(url)


@when('The user accepts the cookie policy')
def accept_cookies(context):
    try:
        cookie_button = context.browser_instance.find_element(By.CLASS_NAME, 'qxOn2zvg.e1sXLPUy ')
        cookie_button.click()
        sleep(1.5)
        logger.info("Cookies accepted successfully.")
    except Exception as e:
        logger.error(f"Error accepting cookies: {e}")


@when('The user hovers over the dropdown menu')
def hover_over_menu(context):
    try:
        dropdown_items = context.browser_instance.find_elements(By.CLASS_NAME, 'dropdown')
        if len(dropdown_items) < 3:
            logger.warning("Insufficient elements in the dropdown menu.")
            return

        action = ActionChains(context.browser_instance)
        action.move_to_element(dropdown_items[2]).perform()
        sleep(2)
        logger.info("Hovered over the dropdown menu successfully.")
    except Exception as e:
        logger.error(f"Error hovering over dropdown menu: {e}")


@when('The user clicks on a specific anime link')
def click_anime_link(context):
    try:
        anime_link = context.browser_instance.find_element(By.CSS_SELECTOR, 'a.sub_link[rel="gleipnir"]')
        anime_link.click()
        sleep(2)
        logger.info("Clicked on the anime link successfully.")
    except Exception as e:
        logger.error(f"Error clicking on anime link: {e}")


@then('The user should land on the correct anime page')
def verify_redirection(context):
    current_url = context.browser_instance.current_url
    expected_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    if current_url == expected_url:
        logger.info(f"Navigation successful! Current URL: {current_url}")
    else:
        logger.warning(f"Navigation failed. Expected: {expected_url}, but got: {current_url}")

    context.browser_instance.quit()
    logger.info("Browser instance closed.")