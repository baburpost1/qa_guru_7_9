from selene import browser, by, have
from selene.core import configuration

configuration.Config.hold_driver_at_exit = True


def test_selene():
    github = browser.open('/')
    github.element('[data-target="qbsearch-input.inputButton"]').click()
    github.element('[id="query-builder-test"]').send_keys('eroshenkoam/allure-example').press_enter()
    github.element('[class="Text-sc-17v1xeu-0 qaOIC search-match"]')
    github.element(by.link_text('eroshenkoam/allure-example')).click()
    github.element('[id="issues-tab"]').click()
    github.element('[id="issue_81_link"]').should(have.text('issue_to_test_allure_report'))
