from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page1 = context.new_page()
    page1.goto("https://www.google.com/")
    # page1.wait_for_timeout(10000)
    page2 = context.new_page()
    page2.goto("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=4056429466154034564&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9144878&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1")
    # page2.wait_for_timeout(10000)
    browser.close()