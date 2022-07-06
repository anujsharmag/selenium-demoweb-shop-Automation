from wait import wait


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)    #same as find_element("id","FirstName")

    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()
