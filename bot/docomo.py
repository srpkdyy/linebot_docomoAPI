import os
import json
import random
import requests
import docomo

DOCOMO_ENTRYPOINT = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='
DOCOMO_ACCESS_TOKEN = os.getenv("DOCOMO_API_KEY")
HEADER = {
    "Content-Type": "application/json"
}

def reply(request_text, username):
    reply = "test"
    return reply
    

def make_request(reply_token, reply):

