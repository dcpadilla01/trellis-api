from django.test import TestCase, Client
from django.urls import reverse
from numberstotextapp.utils.number_to_english import number_to_english


class NumberToEnglishApiTest(TestCase):
    def setUp(self):

        self.client = Client()

    def test_get_num_to_english(self):

        response = self.client.get(reverse("num_to_english"), {"number": "123"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "num_in_english": number_to_english("123")})

    def test_post_num_to_english(self):
        response = self.client.post(reverse("num_to_english"), {"number": "123"}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "num_in_english": number_to_english("123")})


class NumberToEnglishFunctionTest(TestCase):

    def test_number_to_english(self):

        self.assertEqual(number_to_english("3891.29"), "three thousand eight hundred ninety one point two nine")
        self.assertEqual(number_to_english("91.29"), "ninety one point two nine")
        self.assertEqual(number_to_english("0.29"), "zero point two nine")
        self.assertEqual(number_to_english("-91.29"), "negative ninety one point two nine")

