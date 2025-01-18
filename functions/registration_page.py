from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_link = (By.XPATH, "//a[contains(.,'Sign up')]")
        self.full_name = (By.XPATH, "//input[@id='full-name']")
        self.email = (By.XPATH, "//input[@id='email']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.confirm_password = (By.XPATH, "//input[@id='confirm-password']")
        self.signup_button = (By.XPATH, "//button[contains(.,'Sign up')]")
        self.alert = (By.XPATH, "//span[contains(.,'Passwords do not match')]")
        self.alert_successful = (By.XPATH, "//div[@class='ml-3 text-sm font-normal'][contains(.,'Successful registration!')]")

    def form_register(self):
        # Esperar que el elemento esté presente y sea visible
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.signup_link))
        # se busca el elemento en el navegador, el * se implementa para descomponer las tuplas con el formato (By.XPATH, locator)
        self.driver.find_element(*self.signup_link).click()

    def register_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.full_name))
        self.driver.find_element(*self.full_name).send_keys(name)

    def register_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email))
        self.driver.find_element(*self.email).send_keys(email)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password))
        self.driver.find_element(*self.password).send_keys(password)

    def set_confirm_password(self, confirm_password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.confirm_password))
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)

    def send_data(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.signup_button))
        self.driver.find_element(*self.signup_button).click()

    # Validaciones
    def is_register_successful(self):
        alert_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.alert_successful))
        return alert_element.text  # Devuelve el contenido de la alerta

    def is_signup_button_enabled(self):
        # Localizar el botón
        signup_button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.signup_button))
        return signup_button_element.is_enabled()  # Devuelve si el botón está habilitado

    def is_alert_active(self):
        alert_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.alert))
        return alert_element.text  # Devuelve el contenido de la alerta

