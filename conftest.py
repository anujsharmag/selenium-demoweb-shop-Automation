from selenium import webdriver
from time import sleep

from config import Config
from pytest import fixture

@fixture()
def setup():
    driver = webdriver.Chrome(Config.DRIVER_PATH)
    driver.get(Config.URL)
    sleep(6)
    yield  driver
    driver.close()