from helpers.fetchENC import fetchENC
import os
import requests

def download_video(url, filename, directory, useragent):
    '''Downloads the episode'''
    headers = {
        'User-Agent': useragent,
        'X-Requested-With': "XMLHttpRequest",
    }

    enc, server = fetchENC(url, useragent)

    if enc:
        url = server + "/getvid?evid=" + enc
        print(f">> video link found: {url}\n")
        print(">> downloading episode")
    else:
        return False

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # save file in the folder
            file_path = os.path.join(directory, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False
    except:
        return False