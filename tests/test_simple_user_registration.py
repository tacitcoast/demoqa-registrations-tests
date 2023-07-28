from allure_commons.types import Severity
from demoqa.data.users import User2
from demoqa.pages.application import app
import allure
from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage

@allure.title('Successful fill registration form')
@allure.tag("WEB")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Anna Malinovskaia")
@allure.feature("Регистрационная короткая форма студента")
@allure.story("Пользователь может зарегестрироваться")
def test_registration_user():
    # GIVEN
    anna = User2(full_name='Anna Malinovskaia',
                email='tests@demoqa.com',
                current_address='Portugal, Lisbon',
                permanent_address='Russia, Moscow')


    with allure.step('Open registration form'):
        app.simplified_registration.open()

    # WHEN
    with allure.step('Fill registration form'):
        app.simplified_registration.register(anna)

    # THEN
    with allure.step('Check results'):
        app.simplified_registration.should_have_registred(anna)