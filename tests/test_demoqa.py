import datetime
from demoqa.data.users import User
from demoqa.pages.registration_page import RegistrationPage


def test_registration_user():
    registration_page = RegistrationPage()

    anna = User(
        first_name='Anna',
        last_name='Malinovskaia',
        email='tests@demoqa.com',
        gender='Other',
        mobile='9115678907',
        date_of_birth=datetime.date(1989, 1, 11),
        hobbies='Reading',
        subjects='Maths',
        picture='kotik.jpeg',
        address='Russia, Moscow, str.Testers',
        state='NCR',
        city='Delhi'
    )

    registration_page.open()
    registration_page.register(anna)
    registration_page.should_have_registred(anna)
