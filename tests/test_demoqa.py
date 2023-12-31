from selene import browser, have, be
import os


def test_registration_demoqa():
    browser.open('https://demoqa.com/automation-practice-form/')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    # We check that we have opened the registration form
    browser.all("h5").element_by(have.exact_text("Student Registration Form"))

    # Fill in Name, Email, Gender, Mobile
    browser.element('#firstName').should(be.blank).type('Anna')
    browser.element('#lastName').should(be.blank).type('Malinovskaia')
    browser.element('#userEmail').should(be.blank).type('test@demoqa.com')
    browser.all('#genterWrapper label').element_by(have.exact_text('Other')).click()
    browser.element('#userNumber').should(be.blank).type('9115678907')

    # Choosing the date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1989"]').click()
    browser.element('.react-datepicker__day--011').click()

    # Fill Subjects, Hobbies
    browser.element('#subjectsInput').type('ma')
    browser.all("#subjectsWrapper div").element_by(have.exact_text("Maths")).click()
    browser.all('#hobbiesWrapper label').element_by(have.exact_text('Reading')).click()

    # Uploading a picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/kotik.jpeg'))

    # Fill Current Address
    browser.element('#currentAddress').should(be.blank).type('Russia, Moscow, str.Testers')

    # Fill State and City
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    # Click the register button
    browser.element('#submit').click()

    # Check that the modal window has appeared
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # We check that our text is filled in
    browser.element('.table').all('td').even.should(
        have.texts(
            'Anna Malinovskaia',
            'test@demoqa.com',
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

    # Closing the window
    browser.element('#closeLargeModal').click()

    # We check that the form is empty
    browser.element('#firstName').should(be.blank)