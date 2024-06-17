from seleniumwire import webdriver

def fetchXHR(url):
    '''Fetches the referer value from specific xhr headers'''
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    print(">> running selenium on headless mode")
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(url)
        driver.implicitly_wait(10)

        for request in driver.requests:
            if request.response and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                referer = request.headers["Referer"]
                if referer:
                    return referer
                else:
                    return False

    finally:
        driver.quit()
