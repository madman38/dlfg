from helpers.fetchXHR import fetchXHR
import http.client
import json

def fetchENC(url):
    '''Fetches the enc value from specific xhr of given wcofun episode url'''
    conn = http.client.HTTPSConnection("embed.watchanimesub.net")

    payload = "" # do not remove this
    referer = fetchXHR(url)

    # filtering the file name from referer
    start_index = referer.find("file=") + len("file=")
    end_index = referer.find("&", start_index)
    filteredReferer = referer[start_index:end_index][:-4] + ".mp4"  # removing .flv and adding .mp4

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': referer
        }

    conn.request("GET", "/inc/embed/getvidlink.php?v=cizgi%2F"+filteredReferer, payload, headers)

    res = conn.getresponse()
    data = res.read()

    response = data.decode("utf-8")
    enc = json.loads(response)["enc"] # filters the 'enc' value from xml response
    return enc