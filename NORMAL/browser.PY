from playwright.sync_api import Playwright, sync_playwright, expect
import time
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
    
    #lr number
    page.locator("#txtTxprKELocBlockNo").fill("234")
    
    #Building
    page.locator("#txtTxprKELocBuilding").fill("park suites")
    
    
    #scroll
    page.mouse.wheel(0, 1000)
    
    
    #Street/Road
    page.locator("#txtTxprKELocStrtRoad").fill("Maasai rd")
    
    #County
    page.locator("#txtTxprKELocCounty").select_option("30")
    
    #City/Town
    page.locator("#txtTxprKELocCity").fill("234")
    
    #District
    page.locator("#txtTxprKELocDistrict").select_option("93")
    
    #Tax Area/Locality
    
    page.locator("#txtTxprKELocLocality").select_option("664")
    
    # ---------------------------------------------------------------
    
    #Postal Code
    page.locator("#txtTxprKELocpostalCode").select_option("NAIROBI GPO")
    
    #P.O.Box
    page.locator("#txtTxprKELocPOBox").fill("234")
    
    # ---------------------------------------------------------------
    #Mobile No
    page.locator("#txtTxprKELocMobNo1").fill("0700000000")
    
    #Main Email Address
    page.locator("#txtTxprKELocMainEmail").fill("yes@booksmartconsultancy.co.ke")
    
    # ---------------------------------------------------------------
    #Alternative Address?
    page.locator("#cmbIsAlterAdd").select_option("No")
    
    #Bank Account for tax refunds?
    page.locator("#cmbHaveBankAccountDtls").select_option("No")
    
    
    # ---------------------------------------------------------------
    #Are you a partner, director or trustee in any other entity
    page.locator("#cmbIsAlterAdd").select_option("No")
    
    #Bank Account for tax refunds?
    page.locator("#cmbHaveBankAccountDtls").select_option("No")
    
    time.sleep(5)
    
    context.close()
    # Do not close the browser here

# Create the playwright instance without a context manager
playwright = sync_playwright().start()

run(playwright)

# Close the playwright instance after your script is done
playwright.stop()
