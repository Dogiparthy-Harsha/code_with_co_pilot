import unittest
from journal import app, entries

class FlaskTestCase(unittest.TestCase):

    # Test if the homepage loads successfully
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Test if a new entry can be added
    def test_add_entry(self):
        tester = app.test_client(self)
        response = tester.post('/add', data=dict(content='Test entry'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # Now check if the entry was added to the backend
        self.assertGreater(len(entries), 0)
        self.assertEqual(entries[-1]['content'], 'Test entry')

if __name__ == '__main__':
    unittest.main()
