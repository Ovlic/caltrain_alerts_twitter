import requests
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAFcThQEAAAAAcjxbHPHMueWPV%2FSSFhhRJrKnTtg%3DLAa7WhtTMJoWAjHVFCV076D232Hskt2khXmeEIK4zxOCfxfUQw"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "CaltrainAlerts"
    return r


def connect_to_endpoint(url, params={}):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = "https://api.twitter.com/2/tweets?ids=1572331047249154048&tweet.fields=created_at&expansions=author_id&user.fields=created_at"#"https://api.twitter.com/2/users/919284817/tweets"
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()

# DISCORD BOT TOKEN: MTAyMTU1ODc2NzU4Mzc1NjI5MQ.G4iXKA.mK1zA4IijPWeBguY69w6oEpVG8szOS83ZjVh6o

# Authenticate to Twitter
"""auth = tweepy.OAuthHandler("eBD5DgF363XfIFlt6yeMD2i5V", 
    #"hwfh5G5cInAMNik3NodNd25iIQeyo4odTVWzgOoAPX84zdUX1n")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    """