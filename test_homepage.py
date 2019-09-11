from unittest import TestCase, main
import requests
from run import app


class TestHomePage(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        
        r = self.app.get('/')
        
        self.assertEqual(r.status_code, 200)
        
        self.assertEqual(r.get_data().decode(), 'home page')

