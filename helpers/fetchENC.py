from helpers.fetchXHR import fetchXHR
import http.client
import json

def fetchENC(url, useragent):
    '''Fetches the enc value from specific xhr of given wcofun episode url'''
    conn = http.client.HTTPSConnection("embed.watchanimesub.net")

    payload = "" # do not remove this

    # fetching XHR
    for i in range(3):
        referer = fetchXHR(url)
        if referer: break
        else:
            print(f">> XHR not found. trying again...({i+1})")
    
    if not referer:
        return

    # extracting parameters
    base_url, params_part = referer.split('?')

    parameters = params_part.split('&')

    v_param = None
    embed_param = None

    for param in parameters:
        key, value = param.split('=')
        if key == 'v':
            v_param = value
        elif key == 'embed':
            embed_param = value

    headers = {
        'User-Agent': useragent,
        'X-Requested-With': "XMLHttpRequest",
        'Referer': referer
        }

    conn.request("GET", f"/inc/embed/getvidlink.php?v={v_param}&embed={embed_param}", payload, headers)

    res = conn.getresponse()
    data = res.read()

    response = data.decode("utf-8")
    enc = json.loads(response)["enc"] # filters the 'enc' value from xml response
    server = json.loads(response)["server"] # filters the 'server' value from xml response
    return enc, server