from .configuration import Configuration
from .util import followscraper

class Livestreamer_improve():
    def __init__(self):
        configuration = Configuration()
        currently_online = followscraper(configuration.user_id)
        print("These streamers that you follow are currently online:")