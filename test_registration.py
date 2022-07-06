# from selenium import webdriver
# from time import sleep
# from selenium_wrapper import SeleniumWrapper
# from config import Config
from registration import RegistrationPage
from homepage import HomePage
def test_registration(setup):
    hp = HomePage(setup)
    hp.home_click_register()
    rp = RegistrationPage(setup)
    rp.reg_select_male()
    rp.reg_enter_fname("anuu")
    rp.reg_enter_lname("sharmaa")
    rp.reg_enter_email("himashu@gamil.com")
    rp.reg_enter_password("password123")
    rp.reg_enter_confirmpassword("password123")
    rp.reg_click_register()

















    # s = SeleniumWrapper(setup)
    # s.click_element(("link text","Register"))
    # sleep(1)
    # s.click_element(("id","gender-male"))
    # sleep(1)
    # s.enter_text(("id","FirstName"),value="Anuj")
    # sleep(1)
    # s.enter_text(("name","LastName"),value="Sharma")
    # sleep(1)
    # s.enter_text(("id","Email"),value="Anujsdfg@gmail.com")
    # sleep(1)
    # s.enter_text(("id","Password"),value="123356")
    # sleep(1)
    # s.enter_text(("id","ConfirmPassword"),value="123356")
    # sleep(1)
    # s.click_element(("name","register-button"))
    # sleep(1)
