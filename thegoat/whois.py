from thegoat.config import API_TOKEN, API_URL
import json
from urllib.request import Request, urlopen


class whois:
    def __init__(self, domain, as_json):
        self.domain = domain
        self.as_json = as_json

    def fetch(self, url):
        request = Request(API_URL % (API_TOKEN, self.domain),
                          headers={'User-Agent': 'thegoat-cli'})
        response = urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def lookup(self):
        json = self.fetch(API_URL % (API_TOKEN, self.domain))
        if self.as_json:
            self.result = json
        else:
            self.result = self.get_text(json)

    def get_text(self, json):
        return '\n'.join('%s: %s' % (key, value) for key, value in json.items())
