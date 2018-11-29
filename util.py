import requests
import subprocess

HEADERS = {
    'Client-ID': "zjcbgrilhcnzx1mt3fbcrpn7vekw64"
}


def followscraper(user_id):
    params = {
        'from_id': user_id,
        'first': 100
    }
    follows_api_url = "https://api.twitch.tv/helix/users/follows"
    followed_response = requests.get(follows_api_url, params=params, headers=HEADERS)
    followed_list = followed_response.json()["data"]
    return create_stream_urls(followed_list)


def create_stream_urls(follow_list):
    # TODO: Add game name, stream title
    live_api_url = "https://api.twitch.tv/helix/streams"
    base_url = "twitch.tv/"
    streams = []
    for follow_relation in follow_list:
        streams.append(follow_relation["to_id"])
    params = {
        "user_id": streams
    }
    online_streams_response = requests.get(live_api_url, params=params, headers=HEADERS)
    online_streams = {}
    for online_relation in online_streams_response.json()["data"]:
        online_streams[online_relation["user_name"]] = base_url + online_relation["user_name"]
    return online_streams


def execute_livestreamer_command(stream_url, configuration):
    for quality in reversed(configuration.quality_order_of_preference):
        try:
            subprocess.check_output("streamlink "+stream_url+" "+quality, shell=True)
            break
        except subprocess.CalledProcessError:
            pass
