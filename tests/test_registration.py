from selene.support.shared import browser
import os

def test_student_registration_form(browser_settings):
    #user's characters
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Sergey')
    browser.element('#lastName').type('Golichenko')
    browser.element('#userEmail').type('pochta@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8800553555')

    #birthday
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="6"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1999"]').click()
    browser.element('.react-datepicker__day--008').click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#subjectsInput').type('Hi, automation is interesting')
    browser.element('#uploadPicture').set_value(os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.path.pardir, 'upload/conflicts.jpg')))

    browser.element('#currentAddress').type('улица Пушкина')
    browser.element('#submit').click()




    browser.config.hold_browser_open = True

