from selene.support.shared import browser
from selene import have
import os
#import random


def test_student_registration_form():
    #user's characters
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Sergey')
    browser.element('#lastName').type('Automation')
    browser.element('#userEmail').type('pochta@example.com')
    #в данном случае не нужно, но позволяет рандомно кликать по баттонам, если их несколько:
    #browser.element(f"[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']").click()
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8800553555')

    #birthday
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1999"]').click()
    browser.element('.react-datepicker__day--008').click()

    #hobbies and picture
    browser.element('#subjectsInput').type('Maths').press_enter()
    #browser.element(f"[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']").click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.path.pardir, 'upload/conflicts.jpg')))

    #user's adress
    browser.element('#currentAddress').type('улица Пушкина')
    browser.element('#state').click()
    browser.element('#react-select-3-input').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').press_enter()
    browser.element('#submit').click()

    #check results
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Sergey Automation',
        'pochta@example.com',
        'Male',
        '8800553555',
        '08 July,1999',
        'Maths',
        'Sports, Music',
        'conflicts.jpg',
        'улица Пушкина',
        'NCR Delhi'
    ))






