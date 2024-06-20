from helpers.fetchEpisodes import fetchLinks
from helpers.dlVideo import download_video
import os
import sys
import time

def main():
    print("===========================")
    print("DLFG - DOWNLOAD FAMILY GUY")
    print("===========================")

    start_season = int(input(">>> please input the starting season you want to download: "))
    end_season = int(input(">>> please input the ending season you want to download: "))

    print() # newline

    # validate input
    if end_season > 22:
        print(">> error: ending season cannot be more than 22. Setting ending season value to 22...")
        end_season = 22

    elif end_season < start_season:
        print(">> error: ending season cannot be less than the starting season.")
        sys.exit(1)
    
    else:
        pass

    # loop through each season in the specified range
    for season in range(start_season, end_season + 1):
        # create directory to download the episodes into
        if not os.path.exists("FamilyGuy"): os.makedirs("FamilyGuy")

        directory = "FamilyGuy/" + "S" + str(season)
        if not os.path.exists(directory):
            print(">> creating directory for season")
            os.makedirs(directory)
        else:
            choose = input(f">>> there is a directory named 'S{season}'. would you want to overwrite it? (y/n): ")
            if choose.lower() == "y":
                pass
            else:
                input(">> quitting...\n\nPress Enter to exit.")
                sys.exit(1)

        print(">> fetching the episode links")
        links_useragent = fetchLinks(season)
        links = links_useragent[0]
        useragent = links_useragent[1] # getting useragent to use it on webscraping
        episode_count = len(links)
        print(f">> there are {episode_count} episodes on season {season}")

        # scan the directory for existing episode files
        existing_files = os.listdir(directory)
        existing_episodes = [int(file.split('E')[1].split('.')[0]) for file in existing_files if file.endswith('.mp4')]
        existing_episodes.sort()
        
        # determine the starting episode number
        if existing_episodes:
            start_episode = existing_episodes[-1] + 1
            print(f">> resuming download from episode {start_episode}")
        else:
            start_episode = 1

        # download remaining episodes
        for i in range(start_episode - 1, len(links)):  # start from the correct index in the links list
            episode_number = i + 1
            filename = f"S{season}E{episode_number}"
            url = links[i]
            
            print(f">> preparing to download {filename} from this link: {url}")
            start_timer = time.time()
            if download_video(url, f"{filename}.mp4", directory, useragent):
                end_timer = time.time()
                print(f">> {filename} downloaded successfully. {episode_number}/{episode_count} ({round(end_timer - start_timer, 2)} seconds)\n")
            else:
                print(f">> error: {filename} failed to download. moving on...\n")

        print(f"\n\n>> Season {season} downloaded successfully.\n\nPress Enter to exit.")

if __name__ == "__main__":
    main()