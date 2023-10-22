from base.selenium_base import SeleniumBase


class Auth(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://lk.rt.ru/')
        driver.implicitly_wait(20)
        self.telephone = '#username'
        self.e_mail = '#username'
        self.password = '#password'
        self.button_on = '#kc-login'
        self.profile_data = "(//*[@class='color_black text-align-left n-header H2'])[1]"
        self.base_auth = '#standard_auth_btn'
        self.phone_only_key = '#address'
        self.button_only_key = '#otp_get_code'
        self.kod_num_0 = '#rt-code-0'
        self.auth_false = "(//*[@class='card-error__message'])[1]"
        self.error_kod = "(//*[@class='code-input-container__error'])[1]"

    def enter_phone_number(self, number):
        phone_number = self.is_visible('css', self.telephone, 'Номер телефона')
        return phone_number.send_keys(number)

    def enter_email(self, email):
        email_fild = self.is_visible('css', self.e_mail, 'E-mail')
        return email_fild.send_keys(email)

    def enter_password(self, password):
        password_fild = self.is_visible('css', self.password, 'Пароль')
        return password_fild.send_keys(password)

    def enter_phone_only_key(self, number):
        phone_only_key_fild = self.is_visible('css', self.phone_only_key, 'Номер телефона/E-mail')
        return phone_only_key_fild.send_keys(number)

    def push_button_only_key(self):
        button_only_key = self.is_clickable('css', self.button_only_key, 'Получить код')
        return button_only_key.click()

    def enter_kod_num_1(self, number):
        kod_num_1_fild = self.is_visible('css', self.kod_num_0, '1 цифра кода')
        return kod_num_1_fild.send_keys(number)

    def push_button(self):
        button = self.is_clickable('css', self.button_on, 'Войти')
        return button.click()

    def check_profile_data(self):
        return self.is_present('xpath', self.profile_data, 'Добро пожаловать в Личный кабинет').text

    def check_auth_false(self):
        return self.is_present('xpath', self.auth_false, 'Неверный логин или пароль').text

    def check_error_kod(self):
        return self.is_present('xpath', self.error_kod, 'Неверный код. Повторите попытку').text

    def push_base_auth(self):
        base_auth = self.is_clickable('css', self.base_auth, 'Войти с паролем')
        return base_auth.click()

