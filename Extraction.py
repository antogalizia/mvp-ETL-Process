import time
from selenium import webdriver
from Locators import Login
from Locators import Home
import os


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tiendanube.com/")

login = Login()
access = Home()


class Extraction:

    # Log In

    @staticmethod
    def account():
        login_button = login.login_button
        email_button = login.email_button
        pass_button = login.pass_button
        enter_button = login.enter_button
        tn_password = os.environ.get("TN_PASSWORD")
        user = os.environ.get("USER")

        time.sleep(5)
        log = driver.find_element("xpath", login_button)
        log.click()
        email = driver.find_element("id", email_button)
        email.click()
        email.send_keys(user)
        password = driver.find_element("id", pass_button)
        password.click()
        password.send_keys(tn_password)
        enter = driver.find_element("xpath", enter_button)
        enter.click()
        time.sleep(5)

    # Sales access

    @staticmethod
    def sales_access():
        sales_button = access.sales_button
        menu_button = access.menu_button
        all_option_button = access.all_option_button
        filter_button = access.filter_button
        date_button = access.filter_button
        last_week_option = access.last_week_option
        download_data = access.download_csv
        export = access.export

        sales_button = driver.find_element("xpath", sales_button)
        sales_button.click()
        time.sleep(5)
        menu = driver.find_element("xpath", menu_button)
        menu.click()
        all_option = driver.find_element("xpath", all_option_button)
        time.sleep(2)
        all_option.click()
        date = driver.find_element("xpath", date_button)
        date.click()
        last_day = driver.find_element("xpath", last_week_option)
        time.sleep(2)
        last_day.click()
        filter_button = driver.find_element("xpath", filter_button)
        filter_button.click()
        time.sleep(3)
        download_data = driver.find_element("xpath", download_data)
        download_data.click()
        export = driver.find_element("xpath", export)
        export.click()
        time.sleep(30)


















