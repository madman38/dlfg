from seleniumwire import webdriver
from selenium.webdriver.common.by import By

def fetchLinks(season):
    '''Fetches the episode links from given season number'''
    if type(season) != int: return "error: season must be an integer"
    else: pass
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    print(">> running selenium on headless mode")
    driver = webdriver.Firefox(options=options)

    driver.get(f"https://www.wcofun.net/anime/family-guy-season-{season}") # you can change this if you want to download another cartoon from wcofun

    # fetching and returning user agent to use it on web scraping
    for request in driver.requests:
        if request.response:
            useragent = request.headers["User-Agent"]
    try:
        sidebar_right3_div = driver.find_element(By.XPATH, '//*[@id="sidebar_right3"]')

        child_divs = sidebar_right3_div.find_elements(By.XPATH, './/*')

        links = []
        for div in child_divs:
            # check if the div contains any links
            div_links = div.find_elements(By.TAG_NAME, 'a')
            for link in div_links:
                href = link.get_attribute('href')
                links.append(href)

        links = links[::-1] # reversing the list for the actual episode order
        return links, useragent
    
    except: return
    finally: driver.quit()