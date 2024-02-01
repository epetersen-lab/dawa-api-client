# -*- coding: utf-8 -*-

import unittest
import responses
import dawa_api_client


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.responses = responses.RequestsMock()
        self.responses.start()

        self.api = dawa_api_client.DAWA()

    def tearDown(self) -> None:
        self.addCleanup(self.responses.stop)
        self.addCleanup(self.responses.reset)

    def test_mock_adgangsadresser(self):
        url = f"{self.api.base_url}/adgangsadresser"

        # Empty response (no results from query)
        self.responses.add(method=responses.GET, url=url, body="[]")
        resp = self.api.adgangsadresser(struktur="mini", vejnavn="Gade", husnr="1")
        self.assertEqual([], resp)

    def test_mock_adgangsadresser_not_found(self):
        url = f"{self.api.base_url}/adgangsadresser"

        # Empty response (no results from query)
        self.responses.add(method=responses.GET, url=url, body="[]")
        resp = self.api.adgangsadresser(struktur="mini", vejnavn="Gade", husnr="1")
        self.assertEqual([], resp)

        # ResourceNotFoundError
        error = r"""{
                    "type": "ResourceNotFoundError",
                    "title": "The resource was not found",
                    "details": {
                        "id": "0254b942-f3ac-4969-a963-d2c4ed9ab943"
                    }
        }"""
        self.responses.add(method=responses.GET, url=url, body=error, status=404)
        with self.assertRaises(
            dawa_api_client.ApiError
        ) as exception_context:
            self.api.adgangsadresser()
        self.assertEqual(exception_context.exception.type, "ResourceNotFoundError")
        self.assertEqual(
            exception_context.exception.title, "The resource was not found"
        )
        self.assertEqual(
            exception_context.exception.details,
            {"id": "0254b942-f3ac-4969-a963-d2c4ed9ab943"},
        )

    def test_mock_adgangsadresser_query_parameter_format_error(self):
        url = f"{self.api.base_url}/adgangsadresser"

        # Empty response (no results from query)
        self.responses.add(method=responses.GET, url=url, body="[]")
        resp = self.api.adgangsadresser(struktur="mini", vejnavn="Gade", husnr="1")
        self.assertEqual([], resp)

        # QueryParameterFormatError
        error = r"""{
                            "type": "QueryParameterFormatError",
                            "title": "One or more query parameters was ill-formed.",
                            "details": [
                                [
                                    "vejpunkt_id",
                                    "String does not match pattern ^([0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12})$: 2"
                                ]
                            ]
                }"""
        self.responses.add(method=responses.GET, url=url, body=error, status=400)
        with self.assertRaises(
            dawa_api_client.ApiError
        ) as exception_context:
            self.api.adgangsadresser()

        self.assertEqual(exception_context.exception.type, "QueryParameterFormatError")
        self.assertEqual(
            exception_context.exception.title,
            "One or more query parameters was ill-formed.",
        )
        self.assertEqual(
            exception_context.exception.details,
            [
                [
                    "vejpunkt_id",
                    "String does not match pattern ^([0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12})$: 2",
                ]
            ],
        )
