from helpers.fetchEpisodes import fetchLinks
from helpers.dlVideo import download_video
import os
import sys

season = int(input("""===========================
DLFG - DOWNLOAD FAMILY GUY
===========================
                  
Please input the season you want to download: """))

# create directory to download the episodes into
if not os.path.exists("FamilyGuy"): os.makedirs("FamilyGuy")

directory = "FamilyGuy/"+"S"+str(season)
if not os.path.exists(directory):
    print(">> creating directory for season")
    os.makedirs(directory)

else:
    choose = input(f">>> This season is already downloaded or there is a directory named 'S{season}'. Would you want to overwrite it? (y/n): ")
    if choose.lower() == "y":
        pass
    else:
        input(">> quitting...\n\nPress Enter to exit.")
        sys.exit(1)

print(">> fetching the episode links")
links = fetchLinks(season)

i = 1 # episode counter for filename
for url in links:
    filename = f"S{season}E{i}"
    print(f">> preparing to download {filename} from this link: {url}")
    if download_video(url, f"{filename}.mp4", directory):
        print(f">> {filename} downloaded successfully.\n")

    else:
        print(f">> error: {filename} failed to download.\n")

    i+=1

print(f"\n\n>> Season {season} downloaded successfully.")