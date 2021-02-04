from urllib.request import Request, urlopen
from config import API_TOKEN
import json

API_PATH = 'https://api.mahdyar.me/whois/lookup?token=%s&domain=%s'

class whois:
    def __init__(self, domain, as_json):
        self.domain = domain
        self.as_json = as_json

    def fetch(self, url):
        request = Request(API_PATH % (API_TOKEN, self.domain), headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def lookup(self):
        json = self.fetch(API_PATH % (API_TOKEN, self.domain))
        if self.as_json:
            self.json = json
        else:
            self.text = self.get_text(json)

    def get_text(self, json):
        return '\n'.join('%s: %s' % (key, value) for key, value in json.items())