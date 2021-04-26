from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):

    # check if page exists
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # check if page exists
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
