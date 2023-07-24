from selene import browser, have, be
from demoqa.data.users import User
from demoqa.pages import resources


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td')
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('#genterWrapper label')
        self.mobile = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('#hobbiesWrapper label')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form/')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")


    def register(self, anna: User):
        self.first_name.type(anna.first_name)
        self.last_name.type(anna.last_name)
        self.email.type(anna.email)
        self.gender.element_by(have.exact_text(anna.gender)).click()
        self.mobile.type(anna.mobile)
        self.fill_date_of_birth(anna.date_of_birth)
        self.subjects.type(anna.subjects).press_enter()
        self.hobbies.element_by(have.text(anna.hobbies)).click()
        self.picture.set_value(resources.path(anna.picture))
        self.address.type(anna.address)
        self.fill_state(anna.state)
        self.fill_city(anna.city)
        self.submit.click()
        return self

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(value)).click()
        return self

    def should_have_registred(self, anna: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{anna.first_name} {anna.last_name}',
            f'{anna.email}',
            f'{anna.gender}',
            f'{anna.mobile}',
            '{0} {1},{2}'.format(anna.date_of_birth.strftime("%d"),
                                 anna.date_of_birth.strftime("%B"),
                                 anna.date_of_birth.year),
            f'{anna.subjects}',
            f'{anna.hobbies}',
            f'{anna.picture}',
            f'{anna.address}',
            f'{anna.state} {anna.city}'
        ))

        browser.element('#closeLargeModal').click()
        browser.element('#firstName').should(be.blank)
