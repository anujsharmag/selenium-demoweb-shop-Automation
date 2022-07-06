from selenium_wrapper import SeleniumWrapper
from selenium.common.exceptions import  NoSuchElementException
from time import  sleep

class HomePage(SeleniumWrapper):
    _lnk_register = ("link text","Register")
    _lnk_login = ("link text","Log in")

    def home_click_register(self):
        self.click_element(self._lnk_register)

    def home_click_login(self):
        self.click_element(self._lnk_login)

    def is_user_logged_in(self, email):
        _xpath = f"//a[text()='{email}']"
        for _ in range(10):
            try:
                self.driver.find_element_by_xpath(_xpath).is_displayed()
                return True
            except NoSuchElementException:
                print("got exception..")
                sleep(1)
                continue
        return False

    def is_error_login_error_displayed(self, message):
        _xpath =f"//span[text()='{message}']"
        for _ in range(10):
            try:
                self.driver.find_element_by_xpath(_xpath).is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False