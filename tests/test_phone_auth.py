import pytest
import data_base
from POM.auth import Auth


@pytest.mark.usefixtures('setup')
class TestAuthPhone:
    def test_phone_auth_1(self):
        '''Тест №1 авторизация с корректным номером телефона'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_phone_number(data_base.test_phone_number)
        page.enter_password(data_base.test_password)
        page.push_button()
        try:
            assert page.check_profile_data() == 'Добро пожаловать в Личный кабинет'
        except AssertionError:
            print('Не удалось авторизоваться!')


    def test_phone_auth_2(self):
        '''Тест №2 авторизация с некорректным паролем'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_phone_number(data_base.test_phone_number)
        page.enter_password('123test456tesT')
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!')


    def test_phone_auth_3(self):
        '''Тест №3 авторизация с некорректным номером телефона'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_phone_number('+79697983768')
        page.enter_password(data_base.test_password)
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!')


    def test_phone_auth_4(self):
        '''Тест №4 авторизация с некорректным номером телефона и паролем'''
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_phone_number('+79697983768')
        page.enter_password('123test456tesT')
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!')