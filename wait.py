from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait

#overriding
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        return False

def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        #WebDriver wait (Dynamic wait)
        wait = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)    #actual func gets executed "click_element" or "enter_text"
    return wrapper


