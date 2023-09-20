from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://itax.kra.go.ke/KRA-Portal/")
    page.locator("#newReg").get_by_role("link", name="Click Here").click()
    page.locator("#cmbTaxpayerType").select_option("INDI")
    page.locator("#modeOfRegsitartion").select_option("ON")
    page.get_by_role("button", name="Next").click()
    
    page.locator("#rdoCiti1").click()
    page.locator("#cmbTxprProfId").select_option("11")
    
    page.locator("#txtTxprKENatId").fill("39794454")
    page.locator("#calKeTxprDOB").fill("10/11/2001")
    
    # ---------------------
    context.close()
    # Do not close the browser here

# Create the playwright instance without a context manager
playwright = sync_playwright().start()

run(playwright)

# Close the playwright instance after your script is done
playwright.stop()
