from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):

    # test if Home Page exists
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
