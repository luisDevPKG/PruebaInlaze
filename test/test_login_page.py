import pytest
import time
from utilities.driver_setup import get_driver
from functions.login_page import LoginPage


class TestLoginUser:
    @pytest.fixture(scope="function")  # Se ejecutará antes de cada prueba
    def setup(self):
        self.driver = get_driver()
        self.driver.get("https://test-qa.inlaze.com/auth/sign-in")
        self.login_user = LoginPage(self.driver)
        time.sleep(3)
        yield  # Devuelve el control a pytest para ejecutar la prueba.
        self.driver.quit()  # Cierra el navegador para liberar recursos.

    # caso 1 login exitoso
    def test_successful_login(self, setup):
        self.login_user.email_user("pruebaQA2@yopmail.com")
        self.login_user.password_user("QAtest123!")
        time.sleep(1)
        self.login_user.send_data()
        time.sleep(3)
        assert self.driver.current_url == "https://test-qa.inlaze.com/panel", '** ERROR ** No esta redirigiendo al login'

    # caso 2 login password no valido
    def test_fail_login(self, setup):
        self.login_user.email_user("pruebaQA2@yopmail.com")
        self.login_user.password_user("QAtest1!")
        time.sleep(1)
        self.login_user.send_data()
        time.sleep(3)
        assert self.login_user.is_alert_active() == "Password doesn't match", '** ERROR ** No esta generando alerta de password incorrecta'
        assert self.driver.current_url == "https://test-qa.inlaze.com/auth/sign-in", '** ERROR ** Inicio sesion con password incorrecta'

    # caso 3 login email no registrado
    def test_fail_email(self, setup):
        self.login_user.email_user("pruebaQA03@yopmail.com")
        self.login_user.password_user("QAtest123!")
        time.sleep(1)
        self.login_user.send_data()
        time.sleep(3)
        assert self.login_user.is_alert_fail_email_active() == "User not found", '** ERROR ** No esta generando alerta de email incorrecta'
        assert self.driver.current_url == "https://test-qa.inlaze.com/auth/sign-in", '** ERROR ** Inicio sesion con email No registrado'

    # caso 4 username
    def test_username(self, setup):
        self.login_user.email_user("pruebaQA2@yopmail.com")
        self.login_user.password_user("QAtest123!")
        time.sleep(1)
        self.login_user.send_data()
        time.sleep(3)
        assert self.driver.current_url == "https://test-qa.inlaze.com/panel", '** ERROR ** No esta redirigiendo al login'
        assert self.login_user.user_name_visible() == "Prueba QA2", '** ERROR ** No se visualiza el nombre del usuario'

    # caso 5 cerrar sesion
    def test_logout(self, setup):
        self.login_user.email_user("pruebaQA2@yopmail.com")
        self.login_user.password_user("QAtest123!")
        time.sleep(1)
        self.login_user.send_data()
        time.sleep(3)
        assert self.driver.current_url == "https://test-qa.inlaze.com/panel", '** ERROR ** No esta redirigiendo al login'
        self.login_user.user_options()
        time.sleep(2)
        self.login_user.logout_button()
        time.sleep(2)
        assert self.driver.current_url == "https://test-qa.inlaze.com/auth/sign-in", '** ERROR ** No funciona el boton logout'

