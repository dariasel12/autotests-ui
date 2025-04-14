from playwright.sync_api import expect, sync_playwright


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_enabled()
    registration_button.click()

    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()
    expect(dashboard_header).to_have_text('Dashboard')