from base.selenium_base import SeleniumBase


class Registration(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://start.rt.ru/')
        driver.implicitly_wait(20)
        self.button_base_auth = '#standard_auth_btn'
        self.button_registration = '#kc-register'
        self.name = "(//*[@name='firstName'])[1]"
        self.surname = "(//*[@name='lastName'])[1]"
        self.city = "(//*[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange'])[1]"
        self.reg_phone = '#address'
        self.reg_email = '#address'
        self.reg_password = '#password'
        self.reg_password_2 = '#password-confirm'
        self.button_reg = "(//*[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn'])[1]"
        self.reg_profile_data = "(//*[@class='color_black text-align-left n-header H2'])[1]"
        self.reg_phone_again = "(//*[@class='card-modal__title'])[1]"
        self.reg_email_again = "(//*[@class='card-modal__title'])[1]"
        self.reg_kod = '#rt-code-0'
        self.error_reg_kod = "(//*[@class='code-input-container__error'])[1]"
        self.button_get_in = "(//*[@name='gotoLogin'])[1]"
        self.button_reg_again = "(//*[@name='registration_confirm_btn'])[1]"
        self.error_phone_number = "(//*[@class='rt-input-container__meta rt-input-container__meta--error'])[1]"
        self.error_email = "(//*[@class='rt-input-container__meta rt-input-container__meta--error'])[1]"

    def enter_name(self, name):
        name_fild = self.is_visible('xpath', self.name, 'Имя')
        return name_fild.send_keys(name)

    def enter_surname(self, surname):
        surname_fild = self.is_visible('xpath', self.surname, 'Имя')
        return surname_fild.send_keys(surname)

    def enter_city(self, city):
        city_fild = self.is_visible('xpath', self.city, 'Фамилия')
        return city_fild.send_keys(city)

    def enter_reg_phone(self, number):
        reg_phone_fild = self.is_visible('css', self.reg_phone, 'Номер телефона')
        return reg_phone_fild.send_keys(number)

    def enter_reg_email(self, email):
        reg_email_fild = self.is_visible('css', self.reg_email, 'Номер телефона')
        return reg_email_fild.send_keys(email)

    def enter_reg_password(self, password):
        reg_password_fild = self.is_visible('css', self.reg_password, 'Пароль')
        return reg_password_fild.send_keys(password)

    def enter_reg_password_2(self, password):
        reg_password_2_fild = self.is_visible('css', self.reg_password_2, 'Подтверждение пароля')
        return reg_password_2_fild.send_keys(password)

    def push_button_base_auth(self):
        button_base_auth_fild = self.is_clickable('css', self.button_base_auth, 'Войти с паролем')
        return button_base_auth_fild.click()

    def push_button_registration(self):
        button_registration_fild = self.is_clickable('css', self.button_registration, 'Зарегестрироваться')
        return button_registration_fild.click()

    def push_button_reg(self):
        button_reg_fild = self.is_clickable('xpath', self.button_reg, 'Регистрация')
        return button_reg_fild.click()

    def push_button_get_in(self):
        button_get_in_fild = self.is_clickable('xpath', self.button_get_in, 'Войти')
        return button_get_in_fild.click()

    def push_button_reg_again(self):
        button_reg_again_fild = self.is_clickable('xpath', self.button_reg_again, 'Зарегистрироваться с другими данными')
        return button_reg_again_fild.click()

    def check_reg_profile_data(self):
        return self.is_present('xpath', self.reg_profile_data, 'Добро пожаловать в Личный кабинет').text

    def check_reg_phone_again(self):
        return self.is_present('xpath', self.reg_phone_again, 'Учётная запись уже существует').text

    def check_reg_email_again(self):
        return self.is_present('xpath', self.reg_email_again, 'Учётная запись уже существует').text

    def enter_reg_kod(self, kod):
        reg_kod_fild = self.is_visible('css', self.reg_kod, 'Фамилия')
        return reg_kod_fild.send_keys(kod)

    def check_error_reg_kod(self):
        return self.is_present('xpath', self.error_reg_kod, 'Неверный код. Повторите попытку').text

    def check_error_phone_number(self):
        return self.is_present('xpath', self.error_phone_number,
                               'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru').text

    def check_error_email(self):
        return self.is_present('xpath', self.error_email,
                               'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru').text


