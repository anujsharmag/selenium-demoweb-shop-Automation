from pytest import mark
from loginpage import LoginPage
from homepage import HomePage

headers="email, password"
data=[("himashu@gmail.com" , "password123"),
       ("myka@gmail.com", "password123")]
@mark.parametrize(headers,data)
def test_login_positive(setup, email, password):
   hp = HomePage(setup)
   hp.home_click_login()
   lp=LoginPage(setup)
   lp.login_enter_email(email)
   lp.login_enter_password(password)
   lp.login_click_login()
   assert hp.is_user_logged_in(email) == False

headers = "email, password, expected_error"
data = [("himashu@gmail.com", "password12", "login was unsuccessful plz corret and try again" ),
        ("myka@.company", "password123", "plz enter valid mail")]
@mark.parametrize(headers,data)
def test_login_negative(setup, email, password,expected_error):
   hp = HomePage(setup)
   hp.home_click_login()
   lp=LoginPage(setup)
   lp.login_enter_email(email)
   lp.login_enter_password(password)
   lp.login_click_login()
   assert hp.is_error_login_error_displayed(expected_error) == False














   # s = SeleniumWrapper(setup)
    # s.click_element(("xpath", "//a[text()='Log in']"))
    # sleep(2)
    # s.enter_text(("id","Email"), value=email)
    # sleep(2)
    # s.enter_text(("id","Password"), value=password)
    # sleep(2)
    # s.click_element(("xpath", "//input[@value='Log in']"))
    # sleep(2)
