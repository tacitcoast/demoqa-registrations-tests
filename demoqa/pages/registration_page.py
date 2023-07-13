from selene import browser, have, be

from demoqa import resources


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form/')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        # We check that we have opened the registration form
        browser.all("h5").element_by(have.exact_text("Student Registration Form"))

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        browser.all('#genterWrapper label').element_by(have.exact_text(value)).click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(value)).click()
        return self

    def select_picture(self, value):
        browser.element('#uploadPicture').set_value(resources.path(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(value)).click()
        return self

    def submit_form(self):
        browser.element('#submit').click()
        return self

    def should_have_text(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))

    def close(self):
        browser.element('#closeLargeModal').click()

    def should_be_clean(self):
        browser.element('#firstName').should(be.blank)
