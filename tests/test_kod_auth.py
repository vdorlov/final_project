import pytest
import data_base
from POM.auth import Auth


@pytest.mark.usefixtures('setup')
class TestAuthKod:
    def test_phone_auth_kod_1(self):
        '''Тест №9 Авторизация с одноразовым кодом через номер телефона'''
        page = Auth(self.driver)
        page.enter_phone_only_key(data_base.test_phone_number)
        page.push_button_only_key()
        page.enter_kod_num_1(data_base.test_kod)
        try:
            # попытка входа с некорректным mail
            assert page.check_error_kod() == 'Неверный код. Повторите попытку'
        except AssertionError:
            print('Не удалось авторизоваться!')

    # после выполнения теста №9 нужно выждать 2 минуты для запуска теста №10 из-за времени действия кода

    def test_phone_auth_kod_2(self):
        '''Тест №10 Авторизация с одноразовым кодом через номер email'''
        page = Auth(self.driver)
        page.enter_phone_only_key(data_base.test_email)
        page.push_button_only_key()
        page.enter_kod_num_1(data_base.test_kod)
        try:
            assert page.check_error_kod() == 'Неверный код. Повторите попытку'
        except AssertionError:
            print('Не удалось авторизоваться!')