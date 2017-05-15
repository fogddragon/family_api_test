# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pathlib2 import Path
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class FamilyAPITestCase(APITestCase):

    def setUp(self):
        self.family_example = {
            "father": {
                "name": "asdasdasdasdsadaa",
                "age": 40
            },
            "mother": {
                "name": "aaa",
                "age": 50
            },
            "childrens": [
                {
                    "name": "bbb",
                    "age": 11,
                    "sex": "male"
                },
                {
                    "name": "ccc",
                    "age": 12,
                    "sex": "male"
                }
            ]
        }

        self.wrong_family_example = {
            "father": {
                "name": "tsfdfs",
                "age": 40
            },
            "mother": {
                "name": "a312a",
                "age": 50
            },
            "childrens": [
                {
                    "name": "bbb",
                    "age": 11,
                    "sex": "male"
                },
                {
                    "name": "ccc",
                    "age": 12,
                    "sex": "male"
                }
            ]
        }

    def test_save_example(self):
        response = self.client.post(
            reverse('family:save_example'), self.family_example, format='json')
        self.assertEqual(response.status_code, 200)
        my_file = Path("example.xml")
        self.assertTrue(my_file.is_file())

    def test_check_family(self):
        response = self.client.post(
            reverse('family:check_family'), self.family_example, format='json')
        self.assertEqual(response.status_code, 200)

    def test_check_family_not_equal_to_example(self):
        response = self.client.post(
            reverse('family:check_family'), self.wrong_family_example, format='json')
        self.assertEqual(response.status_code, 400)

    def test_check_family_wrong_age(self):
        family = self.family_example
        family['father']['age'] = 10
        family['childrens'][0]['age'] = 55
        response = self.client.post(
            reverse('family:check_family'), self.family_example, format='json')
        self.assertEqual(response.status_code, 400)
