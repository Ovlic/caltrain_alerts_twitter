
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()
BEARER_TOKEN = getenv('TWITTER_TOKEN')

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "CaltrainAlerts"
    return r


def connect_to_endpoint(url, params={}):
    response = requests.request("GET", url, auth=bearer_oauth, json=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_tweets():
    #url = "https://api.twitter.com/2/tweets/search/recent?query=from%3ACaltrainAlerts%20OR%20from%3AOvlic_&max_results=10&tweet.fields=author_id,created_at,id,text"
    url = "https://api.twitter.com/2/tweets/search/recent?query=from%3ACaltrainAlerts%20OR%20from%3AOvlic_&max_results=10&tweet.fields=author_id,created_at,id,source,text&expansions=referenced_tweets.id"
    json_response = connect_to_endpoint(url)
    return json_response
    # print(json.dumps(json_response, indent=4, sort_keys=True))

def test_tweets():
    url = "https://api.twitter.com/2/tweets/1575113398421180416?tweet.fields=created_at,id"
    json_response = connect_to_endpoint(url)
    return json_response

    "https://api.twitter.com/2/tweets/search/recent"
    "query=from:TwitterDev"
    "tweet.fields=created_at"
    "expansions=author_id"
    "user.fields=created_at"

def testrecent():
    url = "https://api.twitter.com/2/tweets/search/recent?query=from%3ACaltrainAlerts&max_results=10&tweet.fields=author_id,created_at,id,source,text"
    json_response = connect_to_endpoint(url)
    return json_response

def tco_to_link(url):
    resp = requests.head(url)
    if resp.status_code == 301:
        return resp.headers["Location"]
    else:
        return None

# Authenticate to Twitter
