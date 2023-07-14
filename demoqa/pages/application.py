from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


class Application:
    def __init__(self):
        self.simplified_registration = SimpleUserRegistrationPage()


app = Application()