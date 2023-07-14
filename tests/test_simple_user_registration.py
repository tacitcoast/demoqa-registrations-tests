from demoqa.data.users import User
from demoqa.pages.application import app
from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_registration_user():
    # GIVEN
    anna = User(full_name='Anna Malinovskaia',
                email='tests@demoqa.com',
                current_address='Portugal, Lisbon',
                permanent_address='Russia, Moscow')

    app.simplified_registration.open()

    # WHEN
    app.simplified_registration.register(anna)

    # THEN
    app.simplified_registration.should_have_registred(anna)
