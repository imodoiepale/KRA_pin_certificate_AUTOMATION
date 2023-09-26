from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://itax.kra.go.ke/KRA-Portal/")
    page.get_by_role("cell", name="To verify PIN, Click Here", exact=True).get_by_role("link").click()
    page.locator("input[name=\"vo\\.pinNo\"]").click()
    page.locator("input[name=\"vo\\.pinNo\"]").fill("P051411900H")
    page.get_by_role("textbox", name="Please enter the result of arithmatic expression in Security Stamp").click()
    page.get_by_role("textbox", name="Please enter the result of arithmatic expression in Security Stamp").fill("")
    page.get_by_role("button", name="Consult").click()
    
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
