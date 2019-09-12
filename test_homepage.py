from unittest import TestCase, main
from run import app


class TestHomePage(TestCase):
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


if __name__ == "__main__":
    main()
