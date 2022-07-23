import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    open_repository_link('eroshenkoam/allure-example')
    open_issues_tab()
    look_for_issue_with_number76('#76')

@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').press_enter()

@allure.step('Переходим по ссылке репозитория {repo}')
def open_repository_link(repo):
    s(by.link_text(repo)).click()

@allure.step('Ищем таб Issues')
def open_issues_tab():
    s('#issues-tab').click()

@allure.step('Проверяем наличие Issue с номером 76')
def look_for_issue_with_number76(number):
    s(by.partial_text(number)).should(be.visible)

