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
                headers = str(request.headers)
                lines = headers.strip().split('\n')
                for line in lines:
                    if line.lower().startswith('referer'):
                        referer = line.split(': ')[1].strip()
                        if referer:
                            return referer
                        else:
                            return False

    finally:
        driver.quit()
