import ytMusicApi
import obsWebsockets
import time
import keyboard


TempTitle = ytMusicApi.get_Song_title()
OBS_Manager = obsWebsockets.OBSWebsockets()

running = True

while running:

    obs_scene_name = OBS_Manager.get_scene_name()
    SongTitle = ytMusicApi.get_Song_title()

    # print("NewSong: " + SongTitle)
    # print("OldSong: " + TempTitle)
    # this is a test

    if keyboard.is_pressed("f8"):
        running = False
        OBS_Manager.disconnect()
        print("Program ending")
        break

    if (SongTitle != TempTitle):
        TempTitle = SongTitle
        OBS_Manager.set_text("MusicText", SongTitle)

        #Preshow Update
        thumbnail_url = ytMusicApi.get_Song_thumbnail()
        ytMusicApi.download_thumbnail(thumbnail_url)
        #time.sleep(1)
        OBS_Manager.set_image_source("MusicThumbnail", "D:/Downloads/OBS-Music-Popup/thumbnail.jpg")

        print("Showing Music on Stream")
        OBS_Manager.set_source_visibility(obs_scene_name, "Music", True)
        time.sleep(4)
        OBS_Manager.set_source_visibility(obs_scene_name, "Music", False)
        time.sleep(1)
        ytMusicApi.delete_thumbnail()
    else:
        print("No new song :(")
    
    time.sleep(1)

