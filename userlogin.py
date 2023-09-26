from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://itax.kra.go.ke/KRA-Portal/")
    page.locator("#logid").click()
    page.locator("#logid").fill("P051619980A")
    page.get_by_role("link", name="Continue").click()
    page.locator("input[name=\"xxZTT9p2wQ\"]").click()
    page.locator("input[name=\"xxZTT9p2wQ\"]").click()
    page.locator("input[name=\"xxZTT9p2wQ\"]").fill("bclitax2023")
    page.get_by_role("textbox", name="Please enter the result of arithmatic expression in Security Stamp").click()
    page.get_by_role("textbox", name="Please enter the result of arithmatic expression in Security Stamp").fill("")
    page.get_by_role("link", name="Login").click()
    page.get_by_role("link", name="Consult and Reprint TCC").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Consult").click()
    page.get_by_role("cell", name="KRANON2751162018", exact=True).click()
    page.get_by_role("cell", name="KRANON2751162018", exact=True).dblclick()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
