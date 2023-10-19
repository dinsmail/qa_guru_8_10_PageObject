from demoga_tests.data.users import User
from demoga_tests.pages.registration_page import RegistrationPage


def test_forms_demoga_praktika():
    registration_page = RegistrationPage()

    user = User(
        first_name='Dinara',
        last_name='Kokhanovskaya',
        email='dinkokh@example.com',
        gender='Female',
        phone_number='9090909090',
        month_of_birth='July',
        year_of_birth='1984',
        day_of_birth='27',
        subject='Computer Science',
        hobby='Music',
        picture='image.png',
        current_address='460000,Russia, Orenburg, Solynoy',
        state='Uttar Pradesh',
        city='Agra'
    )

    registration_page.open()

    registration_page.register(user)

    registration_page.user_should_registered(user)
