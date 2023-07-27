from selene import have, command, be
from selene.support.shared import browser
from demoqa.data.users import User2


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.currentAddress = browser.element('#currentAddress')
        self.permanentAddress = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/text-box')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_full_name(self, value):
        self.full_name.should(be.blank).type(value)

    def fill_email(self, value):
        self.email.should(be.blank).type(value)

    def fill_current_address(self, value):
        self.currentAddress.should(be.blank).type(value)

    def fill_permanent_address(self, value):
        self.permanentAddress.should(be.blank).type(value)

    def submit(self):
        self.submit_button.click()

    def register(self, anna: User2):
        self.fill_full_name(anna.full_name)
        self.fill_email(anna.email)
        self.fill_current_address(anna.current_address)
        self.fill_permanent_address(anna.permanent_address)
        self.submit_button.click()
        return self

    def should_have_registred(self, anna: User2):
        output = browser.element('#output')
        output.perform(command.js.scroll_into_view).should(be.present)
        output.element('#name').should(have.text(anna.full_name))
        output.element('#email').should(have.text(anna.email))
        output.element('#currentAddress').should(have.text(anna.current_address))
        output.element('#permanentAddress').should(have.text(anna.permanent_address))
        return self