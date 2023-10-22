import pytest
import data_base
from POM.auth import Auth

@pytest.mark.usefixtures('setup')
class TestAuthEmail:
    def test_email_auth_1(self):
        '''Тест №5 авторизация с корректным email'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_email(data_base.test_email)
        page.enter_password(data_base.test_password)
        page.push_button()
        try:
            assert page.check_profile_data() == 'Добро пожаловать в Личный кабинет'
        except AssertionError:
            print('Не удалось авторизоваться!')


    def test_email_auth_2(self):
        '''Тест №6 авторизация с некорректным паролем'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_email(data_base.test_email)
        page.enter_password('123test456tesT')
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!')


    def test_email_auth_3(self):
        '''Тест №7 авторизация с некорректным email'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_email('testtestovich.testow@yandex.ru')
        page.enter_password(data_base.test_password)
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!')


    def test_email_auth_4(self):
        '''Тест №8 авторизация с некорректным email и паролем'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_email('testtestovich.testow@yandex.ru')
        page.enter_password('123test456tesT')
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!')
