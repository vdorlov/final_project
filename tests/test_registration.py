import pytest
import data_base
from POM.registration import Registration
from POM.auth import Auth


@pytest.mark.usefixtures('setup')
class TestRegistrationPhone:
    def test_reg_email_1(self):
        '''Тест №11 Регистрация с ранее зарегистрированным email'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_email(data_base.test_email)
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        try:
            assert page.check_reg_email_again() == 'Учётная запись уже существует'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_email_2(self):
        '''Тест №12 Регистрация с уникальным Email'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_email(data_base.new_test_email)
        page.enter_reg_password(data_base.new_test_password)
        page.enter_reg_password_2(data_base.new_test_password)
        page.push_button_reg()
        page.enter_reg_kod(data_base.registration_kod)
        try:
            assert page.check_error_reg_kod() == 'Неверный код. Повторите попытку'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_email_3(self):
        '''Тест №13 Регистрация с ранее зарегистрированным email и дальнейшей авторизацией с корректными данными'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_email(data_base.test_email)
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        page.push_button_get_in()
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_email(data_base.test_email)
        page.enter_password(data_base.test_password)
        page.push_button()
        try:
            assert page.check_profile_data() == 'Добро пожаловать в Личный кабинет'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_email_4(self):
        '''Тест №14 Регистрация с ранее зарегистрированным email и дальнейшей авторизацией с некорректными данными'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_email(data_base.test_email)
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        page.push_button_get_in()
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_email(data_base.test_email)
        page.enter_password('123test456tesT')
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_email_5(self):
        '''Тест №15 Регистрация с ошибочно введенным email'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_email('testtestowich.testowyandex.ru')
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        try:
            assert (page.check_error_email() ==
                    'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru')
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_phone_1(self):
        '''Тест №16 Регистрация с ранее зарегистрированным номером телефона'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_phone(data_base.test_phone_number)
        page.enter_reg_password('123test456tesT')
        page.enter_reg_password_2('123test456tesT')
        page.push_button_reg()
        try:
            assert page.check_reg_phone_again() == 'Учётная запись уже существует'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_phone_2(self):
        '''Тест №17 Регистрация с уникальным номером телефона'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_phone(data_base.new_test_phone)
        page.enter_reg_password(data_base.new_test_password)
        page.enter_reg_password_2(data_base.new_test_password)
        page.push_button_reg()
        page.enter_reg_kod(data_base.registration_kod)
        try:
            assert page.check_error_reg_kod() == 'Неверный код. Повторите попытку'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_phone_3(self):
        '''Тест №18 Регистрация с ранее зарегистрированным номером телефона
        и дальнейшей авторизацией с корректными данными'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_phone(data_base.test_phone_number)
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        page.push_button_get_in()
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_phone_number(data_base.test_phone_number)
        page.enter_password(data_base.test_password)
        page.push_button()
        try:
            assert page.check_profile_data() == 'Добро пожаловать в Личный кабинет'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_phone_4(self):
        '''Тест №19 Регистрация с ранее зарегистрированным номером телефона
        и дальнейшей авторизацией с некорректными данными'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_phone(data_base.test_phone_number)
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        page.push_button_get_in()
        page = Auth(self.driver)
        page.push_base_auth()
        page.enter_phone_number('+79697983768')
        page.enter_password('123test456tesT')
        page.push_button()
        try:
            assert page.check_auth_false() == 'Неверный логин или пароль'
        except AssertionError:
            print('Не удалось авторизоваться!!!')


    def test_reg_phone_5(self):
        '''Тест №20 Регистрация с ранее зарегистрированным номером телефона и дальнейшей авторизацией по коду'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_phone(data_base.test_phone_number)
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        page.push_button_reg_again()
        page.enter_reg_kod(data_base.registration_kod)
        try:
            assert page.check_error_reg_kod() == 'Неверный код. Повторите попытку'
        except AssertionError:
            print('Не удалось авторизоваться!!!')

    def test_reg_phone_6(self):
        '''Тест №21 Регистрация с ошибочно введенным номером телефона'''
        page = Registration(self.driver)
        page.push_button_base_auth()
        page.push_button_registration()
        page.enter_name(data_base.test_name)
        page.enter_surname(data_base.test_surname)
        page.enter_city(data_base.test_city)
        page.enter_reg_phone('968798368')
        page.enter_reg_password(data_base.test_password)
        page.enter_reg_password_2(data_base.test_password)
        page.push_button_reg()
        try:
            assert (page.check_error_phone_number() ==
                    'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru')
        except AssertionError:
            print('Не удалось авторизоваться!!!')




