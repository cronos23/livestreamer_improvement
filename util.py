import requests
import os
import subprocess

CLIENT_ID = "zjcbgrilhcnzx1mt3fbcrpn7vekw64"  # TODO: Change to dict


def followscraper(user_id):
    headers = {
        'Client-ID': CLIENT_ID
    }
    params = {
        'from_id': user_id
    }
    follows_api_url = "https://api.twitch.tv/helix/users/follows"
    followed_response = requests.get(follows_api_url, params=params, headers=headers)
    followed_list = followed_response.json()["data"]
    return create_stream_urls(followed_list)


def create_stream_urls(follow_list):
    # TODO: Add game name, stream title
    headers = {
        'Client-ID': CLIENT_ID
    }
    live_api_url = "https://api.twitch.tv/helix/streams"
    streams = []
    base_url = "twitch.tv/"
    for follow_relation in follow_list:
        streams.append(follow_relation["to_id"])
    params = {
        "user_id": streams
    }
    online_streams_response = requests.get(live_api_url, params=params, headers=headers)
    online_streams = {}
    for online_relation in online_streams_response.json()["data"]:
        online_streams[online_relation["user_name"]] = base_url + online_relation["user_name"]
    return online_streams


def execute_livestreamer_command(stream_url, configuration):
    for quality in reversed(configuration.quality_order_of_preference):
        try:
            subprocess.check_output("livestreamer "+stream_url+" "+quality, shell=True)
            break
        except subprocess.CalledProcessError:
            pass
        # os.system("livestreamer "+stream_url+" "+quality)
        # break
