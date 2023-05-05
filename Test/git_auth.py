import allure
from selene import be, have
from selene.support.shared import browser


class GitAuth:
    @allure.step('Переход на стартовую страницу gitHub')
    def open_start_page(self):
        browser.open('https://github.com/')

    @allure.step('клик по кнопке sing_up')
    def click_sing_up_button(self):
        browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()

    @allure.step('Проверка текста хедера')
    def check_auth_form_header(self):
        browser.element('.auth-form-header.p-0').should(have.exact_text('Sign in to GitHub'))

    @allure.step('Открытие меню навигации на мобильных устройствах')
    def open_navigation_menu(self):
        browser.element('.Button--link').should(be.visible).click()
