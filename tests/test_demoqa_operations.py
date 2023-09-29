import time
from selene import browser, have
import os

def test_complete_todo():
    browser.open('/')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Petrov')
    browser.element('#userEmail').type('petrov@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('79287777777')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1999')
    browser.element('.react-datepicker__month-select').type('August')
    browser.element('.react-datepicker__day--009').click()
    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('files/ball.jpg'))
    browser.element('#currentAddress').type('Russia Moscow')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').click()
    #time.sleep(5)
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
    'Ivan Petrov',
    'petrov@mail.ru',
    'Male',
    '7928777777',
    '09 August,1999',
    'Biology',
    'Sports',
    'ball.jpg',
    'Russia Moscow',
    'NCR Noida'))