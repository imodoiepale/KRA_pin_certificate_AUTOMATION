from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd

def get_user_input(prompt):
    user_input = input(prompt)
    return user_input

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://itax.kra.go.ke/KRA-Portal/")
    page.get_by_role("cell", name="To verify PIN, Click Here", exact=True).get_by_role("link").click()

    # Prompt the user for PIN input
    pin_input = page.locator('input[name="vo\\.pinNo"]')
    user_pin = get_user_input("Please enter your PIN: ")
    page.locator('input[name="vo\\.pinNo"]').fill(user_pin)

    # Click on the CAPTCHA input field and prompt user for CAPTCHA input
    page.locator("#captcahText").click()
    user_captcha = get_user_input("Please enter the CAPTCHA: ")
    page.locator("#captcahText").fill(user_captcha)

    page.get_by_role("button", name="Consult").click()

    # Extract Taxpayer Details
    taxpayer_details = page.get_by_role("group", name="Taxpayer Details").inner_text()

    # ---------------------
    context.close()
    browser.close()

    return taxpayer_details

if __name__ == "__main__":
    with sync_playwright() as playwright:
        extracted_data = run(playwright)

    # Create a DataFrame with the extracted data
    data = {'Taxpayer Details': [extracted_data]}
    df = pd.DataFrame(data)

    # Specify the filename for the Excel file
    excel_file = 'extracted_data.xlsx'

    # Export the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)

    # Print a message indicating the export is complete
    print(f"Data has been saved to '{excel_file}'")
