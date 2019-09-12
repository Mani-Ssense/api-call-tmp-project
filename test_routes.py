from unittest import TestCase, main
from run import app
import requests

class TestRoutes(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        r = self.app.get('/')
        
        self.assertEqual(r.status_code, 200)
        
        self.assertEqual(r.get_data().decode(), 'home page')

    def test_hello_view(self):
        r = self.app.get('/hello-view/mani')
        
        self.assertEqual(r.status_code, 200)
        
        self.assertTrue('Hello MANI' in r.get_data().decode())

    def test_get_json(self):
        r = self.app.get('/json')        
        self.assertEqual(r.json['health'], 'passed')

        res = requests.get('http://localhost:5000/json')
        self.assertEqual(res.json()['health'], 'passed')


if __name__ == "__main__":
    main()
