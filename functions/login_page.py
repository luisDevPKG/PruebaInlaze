from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.XPATH, "//input[@id='email']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.signin_button = (By.XPATH, "//button[contains(.,'Sign in')]")
        self.profile_options = (By.XPATH, "//label[@class='btn btn-ghost btn-circle avatar']")
        self.logout_option = (By.XPATH, "//a[contains(.,'Logout')]")
        self.alert_fail_login = (By.XPATH, "//div[@class='ml-3 text-sm font-normal']")
        self.alert_fail_user = (By.XPATH, "//div[@class='ml-3 text-sm font-normal'][contains(.,'User not found')]")
        self.username = (By.XPATH, "//h2[contains(.,'Prueba QA2')]")

    def email_user(self, email):
        # Esperar que el elemento esté presente y sea visible
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email))
        # se busca el elemento en el navegador, el * se implementa para descomponer las tuplas con el formato (By.XPATH, locator)
        self.driver.find_element(*self.email).send_keys(email)

    def password_user(self, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password))
        self.driver.find_element(*self.password).send_keys(password)

    def send_data(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.signin_button))
        self.driver.find_element(*self.signin_button).click()

    def user_options(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.profile_options))
        self.driver.find_element(*self.profile_options).click()

    def logout_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_option))
        self.driver.find_element(*self.logout_option).click()

    # Validaciones
    def user_name_visible(self):
        username_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username))
        return username_element.text

    def is_alert_active(self):
        alert_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.alert_fail_login))
        return alert_element.text  # Devuelve el contenido de la alerta

    def is_alert_fail_email_active(self):
        alert_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.alert_fail_login))
        return alert_element.text