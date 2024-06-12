from helpers.fetchENC import fetchENC
import os
import requests

def download_video(url, filename, directory):
    '''Downloads the episode'''
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        'X-Requested-With': "XMLHttpRequest",
    }

    base_url = "https://cdn.cizgifilmlerizle.com/getvid?evid="
    enc = fetchENC(url)

    url = base_url + enc
    print(f">> video link found: {url}\n")
    print(">> downloading episode")

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # save file in the folder
        file_path = os.path.join(directory, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False
