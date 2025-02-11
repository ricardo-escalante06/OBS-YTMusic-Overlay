from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os

load_dotenv()

obs_host = os.getenv("OBS_HOST")
obs_port = os.getenv("OBS_PORT")
obs_password = os.getenv("OBS-PASSWORD")

class OBSWebsockets:

    ws = None

    def __init__(self):
        # Connect to websockets
        self.ws = obsws(obs_host, obs_port, obs_password)
        self.ws.connect()
        print("Connected to OBS Websockets!\n")

    def disconnect(self):
        self.ws.disconnect()

    def set_source_visibility(self, scene_name, source_name, source_visible=True):
        response = self.ws.call(requests.GetSceneItemId(sceneName=scene_name, sourceName=source_name))
        myItemID = response.datain['sceneItemId']
        self.ws.call(requests.SetSceneItemEnabled(sceneName=scene_name, sceneItemId=myItemID, sceneItemEnabled=source_visible))

    def set_text(self, source_name, new_text):
        self.ws.call(requests.SetInputSettings(inputName=source_name, inputSettings = {'text': new_text}))

    def get_scene_name(self):
        response = self.ws.call(requests.GetCurrentProgramScene())
        scene_name = response.datain['sceneName']
        return scene_name
    
    def set_image_source(self, source_name, image_path):
        self.ws.call(requests.SetInputSettings(inputName=source_name, inputSettings={'file': image_path}, overlay=False))