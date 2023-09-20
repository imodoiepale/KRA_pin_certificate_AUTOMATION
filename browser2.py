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
    page.locator("#cmbTxprProfId").select_option("11")
    page.get_by_role("group", name="National Id. Details").get_by_label("National Id. Number").fill("39794454")
    page.get_by_role("group", name="Individual Data").get_by_label("Date of Birth").fill("10/11/2001")
    page.locator("#txtTxprKELocBlockNo").fill("234")
    page.locator("#txtTxprKELocStrtRoad").click()
    page.locator("#txtTxprKELocStrtRoad").fill("maasai rd")
    page.locator("#txtTxprKELocBuilding").click()
    page.locator("#txtTxprKELocBuilding").fill("park suits")
    page.locator("#txtTxprKELocCity").click()
    page.locator("#txtTxprKELocCity").fill("nairobi")
    page.locator("#txtTxprKELocDistrict").select_option("93")
    page.locator("#txtTxprKELocLocality").select_option("664")
    page.locator("#txtTxprKELocDescAddr").click()
    page.locator("#txtTxprKELocDescAddr").fill("park suits ")
    page.locator("#txtTxprKELocpostalCode").select_option("NAIROBI GPO")
    page.locator("#txtTxprKELocPOBox").click()
    page.locator("#txtTxprKELocPOBox").fill("1020 parklands")
    
    page.get_by_role("textbox", name="Please Provide Only Numeric Value.").fill("1020")
    page.locator("input[name=\"customVo\\.KETreContactDtlsDTO\\.mobileNumber1\"]").fill("+25470000000")
    
    page.locator("#txtTxprKELocMainEmail").fill("yes@booksmartconsultancy.co.ke")
    
    page.get_by_label("Do you have an Alternative Address?").select_option("No")
    page.locator("#cmbHaveBankAccountDtls").select_option("No")
    
    page.get_by_role("textbox", name="Main Email Address").fill("ij@gmail.com")
    page.get_by_label("Do you wish to declare your Bank Account for tax refunds?").click()
    page.locator("#file").click()
    page.locator("#file").set_input_files("id.docx")
    page.get_by_role("button", name="Next").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
