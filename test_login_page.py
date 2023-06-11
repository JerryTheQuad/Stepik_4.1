from .pages.login_page import LoginPage

class TestLoginPage():
    def test_guest_should_be_login_url(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()

    def test_guest_see_login_form(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()

    def test_guest_see_register_form(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_register_form()