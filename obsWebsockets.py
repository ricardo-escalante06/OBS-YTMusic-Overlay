from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os

load_dotenv()

obs_host = os.getenv("OBS_HOST")
obs_port = os.getenv("OBS_PORT")
obs_password = os.getenv("OBS-PASSWORD")

OBS = obsws(obs_host, obs_port, obs_password)
OBS.connect()

OBS.call(requests.SetCurrentProgramScene(sceneName="Hand Focus"))

OBS.disconnect()