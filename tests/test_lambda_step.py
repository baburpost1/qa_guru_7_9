from selene import browser, by, have
import allure


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('/')

@allure.step('Поиск репозитория eroshenkoam/allure-example')
def search_repo(repo):
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('[id="query-builder-test"]').send_keys(repo).press_enter()
    browser.element('[class="Text-sc-17v1xeu-0 qaOIC search-match"]')
    browser.element(by.link_text('eroshenkoam/allure-example')).click()

@allure.step('Переход на страницу с issue')
def open_issue_page():
    browser.element('[id="issues-tab"]').click()

@allure.step("Проверка имени issue")
def assert_issue_name():
    browser.element('[id="issue_81_link"]').should(have.text('issue_to_test_allure_report'))

def test_lambda_step():
    open_main_page()
    search_repo(repo='eroshenkoam/allure-example')
    open_issue_page()
    assert_issue_name()

