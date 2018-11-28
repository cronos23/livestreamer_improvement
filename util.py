import requests
import json

CLIENT_ID = "zjcbgrilhcnzx1mt3fbcrpn7vekw64"


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
    urls = create_stream_urls(followed_list)


def create_stream_urls(follow_list):
    stream_urls = []
    base_url = "twitch.tv/"
    for follow_relation in follow_list:
        stream_urls.append(base_url+follow_relation["to_name"])
    return stream_urls