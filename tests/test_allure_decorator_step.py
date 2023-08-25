from selene import browser, by, have
import allure
from allure import severity_level

@allure.tag("web")
@allure.severity(severity_level.CRITICAL)
@allure.label("batya", "Baburkin AN")
@allure.feature("Проверка Issue в репозитории")
@allure.story("Поиск нужного issue  в репозитории")
@allure.link("https://github.com", name="Testing")
def test_allure_decorators():
    with allure.step("Открыть главную страницу"):
        browser.open('/')

    with allure.step('Поиск репозитория eroshenkoam/allure-example'):
        browser.element('[data-target="qbsearch-input.inputButton"]').click()
        browser.element('[id="query-builder-test"]').send_keys('eroshenkoam/allure-example').press_enter()
        browser.element('[class="Text-sc-17v1xeu-0 qaOIC search-match"]')
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переход на страницу с issue'):
        browser.element('[id="issues-tab"]').click()

    with allure.step("Проверка имени issue"):
        browser.element('[id="issue_81_link"]').should(have.text('issue_to_test_allure_report'))