from selene import have
from demoqa.pages.registration_page import RegistrationPage


def test_registration_demoqa():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (
        registration_page
        .fill_first_name('Anna')
        .fill_last_name('Malinovskaia')
        .fill_email('tests@demoqa.com')
        .fill_gender('Other')
        .fill_mobile('9115678907')
        .fill_date_of_birth('11', 'January', '1989')
        .fill_subjects('Maths')
        .fill_hobbies('Reading')
        .select_picture('kotik.jpeg')
        .fill_address('Russia, Moscow, str.Testers')
        .fill_state('NCR')
        .fill_city('Delhi')
        .submit_form()
    )

    # THEN
    registration_page.should_have_text('Thanks for submitting the form')
    registration_page.registered_user_data.should(
        have.texts(
            'Anna Malinovskaia',
            'tests@demoqa.com',
            'Other',
            '9115678907',
            '11 January,1989',
            'Maths',
            'Reading',
            'kotik.jpeg',
            'Russia, Moscow, str.Testers',
            'NCR Delhi'
        )
    )

    # WHEN
    registration_page.close()

    # THEN
    registration_page.should_be_clean()
