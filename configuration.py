import yaml
import requests
import json
from .util import CLIENT_ID


class Configuration():
    def __init__(self):
        self.__read_configuration()

    @property
    def user_id(self):
        return self._user_id

    @property
    def quality_order_of_preference(self):
        return self._quality_order_of_preference

    def __read_configuration(self):
        with open("config.yml", 'rw') as configfile:
            cfgdata = yaml.load(configfile)
            if cfgdata["ask_on_startup"]:
                self.__user_configure()
                yaml.dump({"user_id": self._user_id,
                           "quality_order_of_preference": self._quality_order_of_preference,
                           "ask_on_startup": "No"}, configfile)
            else:
                self._user_id = cfgdata.user_id
                self._quality_order_of_preference = cfgdata.quality_order_of_preference


    def __user_configure(self):
        print("Your settings have not been configured yet. Set them here in the console,"
              " or edit the config.yml by hand.")
        self._user_id = self.__get_user_id()
        self._quality_order_of_preference = self.__get_quality()

    @staticmethod
    def __get_user_id():
        username = input("Please enter the name of your twitch.tv account: ")
        headers = {
            'Client-ID': CLIENT_ID
        }
        params = {
            'login': username
        }
        user_id_api_url = "https://api.twitch.tv/helix/users"
        user_data_response = requests.get(user_id_api_url, params=params, headers=headers)
        user_id = user_data_response.json()["data"][0]["id"]
        # TODO: error handling
        return user_id

    @staticmethod
    def __get_quality():
        preferred_quality = False
        quality_list = ["160p", "360p", "480p", "720p", "1080p", "720p60", "1080p60"]
        while preferred_quality not in quality_list:
            preferred_quality = input("Please enter your preferred stream quality. Leave blank for 1080p60 or enter s"
                                      "to (s)how options")
            if preferred_quality == "s":
                for i in quality_list:
                    print(i)
            if not preferred_quality:
                preferred_quality = "1080p60"
        return quality_list[:(quality_list.index(preferred_quality))]
