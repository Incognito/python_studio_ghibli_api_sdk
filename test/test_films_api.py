# coding: utf-8

"""
    Studio Ghibli API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import pprint

import unittest

import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.api.films_api import FilmsApi  # noqa: E501
from studio_ghibli_api_sdk.rest import ApiException


class TestFilmsApi(unittest.TestCase):
    """FilmsApi unit test stubs"""

    def setUp(self):
        self.api = studio_ghibli_api_sdk.api.films_api.FilmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_films_get(self):
        """Test case for films_get

        Return all films  # noqa: E501
        """
        result = self.api.films_get()
        pprint.pprint(result)
        self.assertTrue(len(result) > 5)

    def test_films_id_get(self):
        """Test case for films_id_get

        Film ID  # noqa: E501
        """
        result = self.api.films_id_get('2baf70d1-42bb-4437-b551-e5fed5a87abe')
        pprint.pprint(result)
        self.assertEqual(result.id, '2baf70d1-42bb-4437-b551-e5fed5a87abe')


if __name__ == '__main__':
    unittest.main()
