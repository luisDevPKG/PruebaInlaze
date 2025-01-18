import pytest
import time
from utilities.driver_setup import get_driver
from functions.registration_page import RegistrationPage


class TestRegisterUser:
    @pytest.fixture(scope="function")  # Se ejecutará antes de cada prueba
    def setup(self):
        self.driver = get_driver()
        self.driver.get("https://test-qa.inlaze.com/auth/sign-in")
        self.registration_page = RegistrationPage(self.driver)
        time.sleep(3)
        yield  # Devuelve el control a pytest para ejecutar la prueba.
        self.driver.quit()  # Cierra el navegador para liberar recursos.

    # caso 1 registro exitoso
    def test_successful_registration(self, setup):
        self.registration_page.form_register()
        time.sleep(2)
        self.registration_page.register_name("Prueba QA2")
        self.registration_page.register_email("pruebaQA2@yopmail.com")
        self.registration_page.set_password("QAtest123!")
        self.registration_page.set_confirm_password("QAtest123!")
        time.sleep(1)
        self.registration_page.send_data()
        time.sleep(3)
        assert self.registration_page.is_register_successful() == "Successful registration!", '** ERROR ** No esta generando alerta de registro exitoso'
        assert self.driver.current_url == "https://test-qa.inlaze.com/auth/sign-in", '** ERROR ** No esta redirigiendo al login'

    # caso 2 valida campo full name
    def test_name_validation(self, setup):
        self.registration_page.form_register()
        time.sleep(2)
        self.registration_page.register_name("Prueba")
        self.registration_page.register_email("pruebaQA2@yopmail.com")
        self.registration_page.set_password("QAtest123!")
        self.registration_page.set_confirm_password("QAtest123!")
        time.sleep(1)
        assert not self.registration_page.is_signup_button_enabled(), "El botón debería estar deshabilitado"

    # caso 3 valida campo email
    def test_email_validation(self, setup):
        self.registration_page.form_register()
        time.sleep(2)
        self.registration_page.register_name("Prueba QA2")
        self.registration_page.register_email("")
        self.registration_page.set_password("QAtest123!")
        self.registration_page.set_confirm_password("QAtest123!")
        time.sleep(1)
        assert not self.registration_page.is_signup_button_enabled(), "El botón debería estar deshabilitado"

    # caso 4 valida campo password
    def test_password_validation(self, setup):
        self.registration_page.form_register()
        time.sleep(2)
        self.registration_page.register_name("Prueba QA2")
        self.registration_page.register_email("pruebaQA2@yopmail.com")
        self.registration_page.set_password("")
        self.registration_page.set_confirm_password("QAtest123!")
        time.sleep(1)
        assert not self.registration_page.is_signup_button_enabled(), "El botón debería estar deshabilitado"

    # caso 5 valida campo repeat password
    def test_repeat_password_validation(self, setup):
        self.registration_page.form_register()
        time.sleep(2)
        self.registration_page.register_name("Prueba QA2")
        self.registration_page.register_email("pruebaQA2@yopmail.com")
        self.registration_page.set_password("QAtest123!")
        self.registration_page.set_confirm_password("QAtest123!2")
        time.sleep(2)
        assert self.registration_page.is_alert_active() == "Passwords do not match", '** ERROR ** No valida que las contrasenas coincidan'
        time.sleep(1)
        assert not self.registration_page.is_signup_button_enabled(), "El botón debería estar deshabilitado"

    # caso 6 valida campos obligatorios
    def test_fields_validation(self, setup):
        self.registration_page.form_register()
        time.sleep(2)
        self.registration_page.register_name("")
        self.registration_page.register_email("")
        self.registration_page.set_password("")
        self.registration_page.set_confirm_password("")
        time.sleep(1)
        assert not self.registration_page.is_signup_button_enabled(), "El botón debería estar deshabilitado"