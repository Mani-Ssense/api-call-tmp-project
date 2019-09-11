import requests

class ApiClient:
    def get_comments(self):
        r = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")
        return r.json()
